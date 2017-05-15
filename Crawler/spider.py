# for crawling
# 아래는 웹(www)을 다룰 때 가장 흔하게(필수적으로) 사용하는 모듈임.
from urllib.request import urlopen
from Crawler.link_finder import LinkFinder
from Crawler.general import *

class Spider:
    # Define Class variables (shared among all instances)
    project_name = ''   # 어느 사이트를 크롤링할지
    base_url = ''       # 해당 사이트 기본주소
    domain_name = ''    # 만약 도메인 네임을 특정 웹 사이트 내로 한정하지 않는다면, 인터넷 전체를 링크 타서 크롤링하게 된다.
    queue_file = ''
    crawled_file = ''
    queue = set()       #waiting list
    crawled = set()

    # Initialize Spider Class
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)

    # boot() 함수는 클래스에 귀속되어있을 필요가 없음
    # static method로 선언한 시점에서 boot(self)라고 써줄 이유가 없어짐.
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.Crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        # 기존에 crawled 된 리스트에 page_url이 존재한다면 크롤링할 필요x
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            # 해당 url을 앞으로 크롤링해야할 웨이팅리스트(queue)에 추가하도록 함
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        # urlopen 모듈을 사용해 웹페이지를 연결하면 기계가 이해할 수 있는 바이트 단위로 데이터를 가지고 온다.
        # so, we need converting
        html_string = ''

        # 파이썬에서 네트웍을 이용할 때는 try-except를 이용하는 것이 좋음.
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html; charset=utf-8':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string) # 이렇게함으로써 page_links()를 일일이 호출할 필요가 없어짐.
        except:
            print('Error: can not crawl page')
            return set()
        return finder.page_links()

    # 웹페이지에서 찾아낸 일크들을 waiting list에 추가
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue

            # following code가 존재하지 않는다면 크롤링하고자 하는 사이트에서 외부 사이트로 접속하는 링크까지 크롤링하 수도 있음.
            # In english, to avoid crawling the entire tistoty.com
            if Spider.domain_name not in url:
                continue

            Spider.queue.add(url)

    # queue에 있는 것들을 파일로 저장
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)