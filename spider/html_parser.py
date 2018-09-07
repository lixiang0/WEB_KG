
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import os
class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.htm
        links = soup.find_all('a', href=re.compile(r'/item/%[A-Z0-9]+'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            # print(new_full_url)
            new_urls.add(new_full_url)
        # print(new_urls)
        return new_urls

    def _save_new_data(self, page_url, soup,html_cont):
        res_data = False
        if '?force=1' in page_url:
            #multiple items
            print('multiple items')
            return not res_data
        #error items
        title_node =''
        try:
            title_node=soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        except:
            return not res_data
        #second title
        title_sub__text=''
        try:
            title_sub__text = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h2').get_text()
        except:
            title_sub__text=''
        filename = title_node.get_text() + title_sub__text
        path='../webpages/'#custom diectory for webpages
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + filename.replace('/',''), 'w') as f:
            f.write(html_cont.decode('utf-8'))
            print('Save to disk filename:'+f.name+"")
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        # print(soup.prettify())
        new_urls = self._get_new_urls(page_url, soup)
        is_saved = self._save_new_data(page_url, soup,html_cont)
        return new_urls, is_saved
