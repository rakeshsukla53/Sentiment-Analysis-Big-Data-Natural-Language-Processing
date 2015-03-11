__author__ = 'rakesh'

import feedparser
#from  urlib.request import urlopen
import time

oldList = ''

def extractFiles(links):
    textfile = []

    global oldList

    for line in links:
        file = line[:86] + '.txt'
        if oldList != file:
            textfile.append(file)
        else:
            break
    if len(textfile) >= 1:
        print textfile

    if len(textfile) >= 1:
        oldList = textfile[0]


    newFile = open('newList', 'a')
    for line in textfile:
        newFile.write(line)
        newFile.write('\n')
    newFile.close()

    lines_seen = set() # holds lines already seen
    outfile = open('compareList', "w")
    for line in open('newList', "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()


    return textfile

def main():


    while True:

        feed = feedparser.parse('http://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=4&company=&dateb='
                        '&owner=only&start=0&count=40&output=atom')
        links = []
        for item in feed.entries:

            if '(Issuer)' in item['title']:
                line = item['links'][0]
                RSSlinks = line['href']
                links.append(RSSlinks)
        #print(links)
        extractFiles(links)
        time.sleep(1)

main()

