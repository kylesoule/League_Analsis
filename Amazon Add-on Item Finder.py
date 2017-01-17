from HTMLparser import HTMLParser
import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

#response = opener.open("https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=pop+funko")
#html_doc = response.read()


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data

#parser = MyHTMLParser()
#parser.feed(str(html_doc))