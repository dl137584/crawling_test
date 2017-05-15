# HTML을 파싱하기 위해 관련 모듈을 불러옴.
from html.parser import HTMLParser
from urllib import parse

# HTMLParser를 종속하게하는 링크를 찾는 class
class LinkFinder(HTMLParser):
    #Initializing
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    #웹페이지에서 tag를 다루는 함수를 정의
    def handle_starttag(self, tag, attrs):
        # print(tag)
        if tag == 'a':
            for(attribute, value) in attrs:
                if(attribute == 'href'):
                    url = parse.urljoin()
                    self.links.add(url)

    def page_links(self):
        return self.links

    #error
    def error(selfself, messgae):
        pass

# finder는 LinkFinder로부터 생성했고, 웹페이지에서 찾을 태그가 feed() 안에 들어가게 됨.
# finder = LinkFinder()
# finder.feed('<HTML><head><title> TITLE TEST </title></head?'
#             '<body><h1> Parse TEST </h1></body></html>')