
import urllib
import urllib.request
import urllib.parse
import pymysql
# import http.client.HTTPResponse
from pprint import p
import re
import os


# db conn data
def __conn_data():
    return ['localhost', 'root', '']

# connect to db 
def connect(data):
    return pymysql.connect(*data)

# get main page



# get page list by pagination 

# get page content 
def get_page(url):
    return urllib.request.urlopen(url)

# save page content 


# store page to db
def save_page(url, content):
    '''Insert or update page
        table(id, url, content, timestamp)
     '''

class ParserException(Exception):
    pass

# start parser
def start_parse(url):
    # DB = connect(__conn_data)
    authors = author_groups(url)
    sort_authors = sorted(authors, key = lambda a: int(a))
    p(sort_authors)
    dir = os.path.dirname(os.path.realpath(__file__))
    save_path = dir + '/authors.txt'
    str_list = [' '.join(sort_authors[i : i+10]) for i in range(0, len(sort_authors), 10)]
    p('a: {}, srta: {}'.format(len(authors), len(sort_authors)))
    with open(save_path, 'w') as file:
        p(str_list)
        file.write('\n'.join(str_list))
        file.flush()

def url_decode(enstr):
    return urllib.parse.unquote(enstr)

def parse_page(url, regex):
    resp = get_page(url)
    if resp.getcode() != 200:
        raise ParserException('cant load main page')
    text = str(resp.read())
    p('loaded page {}, size = {}'.format(url_decode(url), len(text)))
    regex1 = regex[0] if isinstance(regex, tuple) else regex
    pages = re.findall(regex1, text)
    res = (True, pages)
    if len(pages) == 0 and isinstance(regex, tuple) and len(regex) > 1:
        pages = re.findall(regex[1], text)
        res = (False, pages)
    return res

# get page list of author pages
def author_groups(main_url):
    group_expr = r'<entry>.*?<link href="(/opds/authors(?:index)?/[^"]+)"'
    auth_expr = r'<entry>.*?<link href="/opds/author/([\d]+)"'
    pagesA = parse_page(main_url, r'<entry>.*?<link href="(/opds/authors(?:index)?/[^"]+)"')[1]
    p('***')
    p([url_decode(s) for s in pagesA])
    stopper = 3
    author_list = []
    for page_url in pagesA[0:3]:
        sub_pagesAa = parse_page(BASE_URL + page_url, r'<entry>.*?<link href="(/opds/authors(?:index)?/[^"]+)"')[1]
        p('*** ***')
        p([url_decode(s) for s in sub_pagesAa])
        for sub_page_url in sub_pagesAa[0:3]:
            sub_pagesAaa = parse_page(BASE_URL + sub_page_url, 
            (r'<entry>.*?<link href="(/opds/authors(?:index)?/[^"]+)"',
            r'<entry>.*?<link href="/opds/author/([\d]+)"'))
            p('*** *** ***')
            p([url_decode(s) for s in sub_pagesAaa[1]])
            if not sub_pagesAaa[0]:
                # if authors
                author_list.extend(sub_pagesAaa[1])
                break
            # if yet one level of grouping
            for sub2_url in sub_pagesAaa[1]:
                authors = parse_page(BASE_URL + sub2_url, 
                r'<entry>.*?<link href="/opds/author/([\d]+)"')
                author_list.extend(authors[1])
    return author_list

def author_list(page_url):
    pass # ??

# get page list of menu lvlv 2
def author_sub_group(group_url):
    url_list = parse_page(group_url, r'<entry>.*?<link href="(/opds/authors(?:index)?/[^"]+)"')
    return url_list
BASE_URL = 'http://flibusta.is'
start_page = 'http://flibusta.is/opds/authorsindex'

start_parse(start_page)

# dir = os.path.dirname(os.path.realpath(__file__))
# p(dir)

# res = re.findall(r'<([\w]+),(\w+)>', '<a,a><bbbb,bb><ccd,ddd>') #  [('a', 'a'), ('bbbb', 'bb'), ('ccd', 'ddd')]
# p(res)
