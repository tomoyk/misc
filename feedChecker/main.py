#!/usr/bin/env python
import feedparser
import sys
from feeder import Feeder

argv=sys.argv
argv.sort()

def has_argv(check_name):
    for a in argv:
        # Has check_param on argv
        if( a==check_name ):
            return True
    return False

def main():
    saved_feed = feedparser.parse(r'feed.xml')
    if( has_argv(check_name="--offline") ):
        print("[info] Offline mode is enabled. Not downlaod feed from remote.")
        sys.exit(0)

    # fresh_feed = feedparser.parse('https://inside.teu.ac.jp/feed/')
    fresh_feed = feedparser.parse(r'feed2.xml')
    if(fresh_feed == saved_feed):
        print("[info] Update was not found.")
        sys.exit(0)

    feeder = {'fresh': Feeder(), 'saved': Feeder()}
    feeder['fresh'].set(parsed_feed=fresh_feed)
    feeder['saved'].set(parsed_feed=saved_feed)

    # feeder = Feeder()
    # feeder.show(items=['title', 'author'])

    Feeder.fetchDiff(target=feeder['fresh'].get(), base=feeder['saved'].get())

if __name__ == '__main__':
    main()
