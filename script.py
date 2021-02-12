#!/usr/bin/python3

import argparse
from sys import argv
from apiclient.discovery import build

def query(query , api , cse):
    s = build("customsearch" , "v1" , developerKey = api).cse()
    results = s.list(q = query , cx = cse).execute()
    return results['items']
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d" , help="List of dorks")
    parser.add_argument("-a" , help="Google API key")
    parser.add_argument("-c" , help="Custom Search Id")
    parser.add_argument("-o" , help="Output file")
    args = parser.parse_args()
    
    api = args.a
    csi = args.c
    dorks = args.d
    output = args.o

    f = open(dorks)
    w = open(output , "w+")
    lines = f.readlines()
    results = []

    for i in lines:
       for j in query(i.strip() , api , csi):
           print(j['link'])
           w.write(j['link'])
           w.write('\n')

    w.close()
    f.close()

main()