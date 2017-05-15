# 하나의 Spider로 처리하는건 비효율적이므로 threading을 불러온다.
import threading
from queue import Queue
from Crawler.spider import Spider
from Crawler.domain import *
from Crawler.general import *

PROJECT_NAME = 'creativeworks'
HOMEPAGE = 'http://nyamtutorial.tistory.com/'

DOMAIN_NAME = get_blog_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'      # 크롤한 링크들이 저장됨
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'  # queue.txt의 링크를 크롤링했다면 crawled.txt에 들어가고, 이 링크를 다시 크롤하지 않도록 돕는다.
NUMBER_OF_THREADS = 4   # 몇개의 스파이더(thread)를 사용할지
queue = Queue()         # Queue()는 threading을 사용.
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME) #구동