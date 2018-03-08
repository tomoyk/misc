#!/usr/bin/env python
import feedparser
import os
import sys
import urllib.request
from feeder import Feeder

argv=sys.argv
argv.sort()

def has_argv(check_name):
    for a in argv:
        # Has check_param on argv
        if( a==check_name ):
            return True
    return False

def download(uri, file_name):
    urllib.request.urlretrieve(uri, file_name)

def main():
    try:
        os.remove('feed_old.xml')
        os.rename('feed.xml', 'feed_old.xml')
        download(uri='https://inside.teu.ac.jp/feed/', file_name='feed.xml')
    except Exception as e:
        with open('console.log', mode='a', encoding='utf-8') as fd:
            fd.write(str(e) + '\n')
        sys.exit(1)

    saved_feed = feedparser.parse(r'feed_old.xml')
    if( has_argv(check_name="--offline") ):
        print("[info] Offline mode is enabled. Not downlaod feed from remote.")
        feeder = Feeder()
        feeder.set(parsed_feed=saved_feed)
        feeder.show(items=['title', 'uri'])
        sys.exit(0)

    fresh_feed = feedparser.parse(r'feed_old.xml')
    if(fresh_feed == saved_feed):
        print("[info] Update was not found.")
        sys.exit(0)

    feeder = {'fresh': Feeder(), 'saved': Feeder()}
    feeder['fresh'].set(parsed_feed=fresh_feed)
    feeder['saved'].set(parsed_feed=saved_feed)

    new_entries = Feeder.fetch_diff(target=feeder['fresh'].get(), base=feeder['saved'].get())
    # debug:: print(str(new_entries))
    for entry in new_entries:
        body = entry['title'] + ' (' + entry['date'] +  ')\n' + entry['uri'] + '\n'
        Feeder.notify_slack(message=body)

if __name__ == '__main__':
    main()
