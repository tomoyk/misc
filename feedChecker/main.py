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
        # print_entry(parsed_xml=saved_xml)
        sys.exit(0) 

    # fresh_xml = feedparser.parse('https://inside.teu.ac.jp/feed/')
    fresh_xml = feedparser.parse(r'feed2.xml')
    if(fresh_xml == saved_xml):
        print("[info] Update was not found.")
        sys.exit(0)

    # print_entry(parsed_xml=fresh_xml)
    # debug:: print(fresh_xml['entries'][0])
    
    # 差分をもとめる  
    # a=list(saved_xml['entries'])
    # b=list(fresh_xml['entries'])
    # print(a[0]['content'][0]['value'])
    # sys.exit(0)
    # a_sort = sorted(a)
    # b_sort = sorted(b)
    # print(set(a) - set(b))

    feeder = Feeder()
    feeder.set(parsed_xml='fresh_xml')
    # feeder.print(items=['title', 'author'])
    for i in feeder.get():
        for k,v in i.items():
            print(k + "\n\t" + v)
            

if __name__ == '__main__':
    main()
