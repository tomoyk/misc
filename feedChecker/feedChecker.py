#!/usr/bin/env python
import datetime
import feedparser
import os
import sys
import urllib.request

argv=sys.argv
argv.sort()

def has_argv(check_name):
    for a in argv:
        # Has check_param on argv
        if( a==check_name ):
            return True
    return False

def print_entry(parsed_xml):
    for entry in parsed_xml['entries']:
        # Convert "Tue, 06 Mar 2018 05:20:30 +0000" => Type(Date)
        entry_date_raw = entry['published']
        entry_date = datetime.datetime.strptime(entry_date_raw, '%a, %d %b %Y %H:%M:%S %z')
        print(str(entry_date.strftime('%Y/%m/%d')) + '\t', end='')

        print(entry['title'])
        print(entry['author'] + '  \t', end='')
        
        # Convert from internal-uri to externa-uri
        entry_uri = entry['links'][0]['href']
        if( has_argv(check_name="--inside") ):
            print(entry_uri)
        else:
            outside_uri = entry_uri.replace("//inside.teu.ac.jp/", "//service.cloud.teu.ac.jp/inside2/")
            print(outside_uri)

        for i in range(50):
            print("- ", end='')
        print()
        # debug:: break
    
def download(uri, file_name):
    urllib.request.urlretrieve(uri, file_name)

def main():
    saved_xml = feedparser.parse(r'feed.xml')
    if( has_argv(check_name="--offline") ):
        print("[info] Offline mode is enabled. Not downlaod feed from remote.")
        print_entry(parsed_xml=saved_xml)
        sys.exit(0) 

    # fresh_xml = feedparser.parse('https://inside.teu.ac.jp/feed/')
    fresh_xml = feedparser.parse(r'feed2.xml')
    if(fresh_xml == saved_xml):
        print("[info] Update was not found.")
        sys.exit(0)

    print_entry(parsed_xml=fresh_xml)
    # debug:: print(fresh_xml['entries'][0])

    # 差分をもとめる  

if __name__ == '__main__':
    main()
