
import feedparser
import json
import time

while True:

    feed = feedparser.parse('http://www.huffingtonpost.com/feeds/index.xml')

    for item in feed.entries:
        print item['title']
        print item['link']   #with the help of this you can extract the files and and its title
        time.sleep(5)

#you can use urllib2 and beautiful soup , scappy but feed parser is highly efficient for RSS Feeds





