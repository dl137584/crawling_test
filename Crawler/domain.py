# 특정한 조건을 주어 크롤링하기 위한 도메인 네임
# https://creativeworks.tistory.com의 도메인 네임은 tistory.com이다.
from urllib.parse import urlparse

# Get domain name (tistory.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# Get Personal Bog Domain anem (creativeworks.tistory.com)
def get_blog_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-3] + '.' + results[-2] + '.' + results[-1]
    except:
        return ''

# Get sub domain name (ex - mail.google.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc     # network location
    except:
        return ''

# print(get_domain_name('https://www.daum.net'))
