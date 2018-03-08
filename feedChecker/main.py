#!/usr/bin/env python
import datetime
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
    saved_xml = feedparser.parse(r'feed.xml')
    if( has_argv(check_name="--offline") ):
        print("[info] Offline mode is enabled. Not downlaod feed from remote.")
        sys.exit(0)

    # fresh_xml = feedparser.parse('https://inside.teu.ac.jp/feed/')
    fresh_xml = feedparser.parse(r'feed2.xml')
    if(fresh_xml == saved_xml):
        print("[info] Update was not found.")
        sys.exit(0)

    feeder = {'fresh': Feeder(), 'saved': Feeder()}
    feeder['fresh'].set(parsed_feed=fresh_xml)
    feeder['saved'].set(parsed_feed=saved_xml)

    # feeder = Feeder()
    # feeder.show(items=['title', 'author'])

    for fresh in feeder['fresh'].get():
        for saved in feeder['saved'].get():
            if(fresh==saved):
                break
        else:
            print("New Content: \n\t" + str(fresh))

if __name__ == '__main__':
    main()
