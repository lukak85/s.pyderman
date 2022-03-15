from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url + 'robots.txt'
        self.page_url = page_url + 'robots.txt'
        self.links = set()

    # check the tag
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    # if the url is relative, not complete it adds the prefix
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links
    
    def error(self, message):
        pass

