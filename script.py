#!/usr/bin/python3

import argparse
import time
import sys
from apiclient.discovery import build

def banner():
    print("-"*50)
    print("DORKY by ev1l._.m0rty")
    print("https://github.com/mrjoker05")
    print("-"*50)
    print()

def query(query , api , cse , f):
    try:
        s = build("customsearch" , "v1" , developerKey = api).cse()
        #results = s.list(q = query , cx = cse, start=21).execute()
        results = s.list(q = query , cx = cse).execute()
        return results['items']
    except:
        print("\n[!] Daily Limit of API key reached. Try tomorrow\n")
        f.close()
        sys.exit()
    
def main():
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument("-d" ,"--dork" , help="List of dorks" , required = True)
    parser.add_argument("-a" , "--api" , help="Google API key", required = True)
    parser.add_argument("-c" , "--csi" , help="Custom Search Id", required = True)
    parser.add_argument("-o" , "--output" , help="Output file")
    args = parser.parse_args()
    
    api = args.api
    csi = args.csi
    dorks = args.dork
    output = args.output

    f = open(dorks)
    try:
        w = open(output , "w+")
    except:
        pass
    
    lines = f.readlines()
    results = []

    for i in lines:
       for j in query(i.strip() , api , csi ,f):
           print(j['link'])
           try:
               w.write(j['link'])
               w.write('\n')
           except:
               pass

    try:
        w.close()
    except:
        pass
    
    f.close()

main()
