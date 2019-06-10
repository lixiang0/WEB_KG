
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import os
import urllib
class HtmlParser(object):
    def _get_new_urls(self, soup):
        sets = set()
        # /view/123.htm
        #<a target="_blank" href="/item/%E6%9D%8E%C2%B7%E5%A1%94%E7%8E%9B%E9%9C%8D%E7%91%9E/5486870" data-lemmaid="5486870">李·塔玛霍瑞</a>
        links = soup.find_all('a',href=re.compile('/item/*'))
        for link in links:
            temp=BeautifulSoup(str(link), 'lxml').find('a')['href']#.replace('https://baike.baidu.com','')
            result=urllib.parse.unquote(temp)
            #print(result)
            #result=re.findall('/item/*', result)
            # print(result)
            item=result#[0]#.replace('/[0-9]+','').split('/')[2].replace('#hotspotmining','')
            # print(item)
            sets.add(urljoin('https://baike.baidu.com/item',item))
            # print(urllib.parse.unquote(urljoin('https://baike.baidu.com', '/'.join(temp.find('a')['href'].split('/')[:5]))) )
            # maps[temp.find('a').contents[0]]=urllib.parse.unquote(urljoin('https://baike.baidu.com', '/'.join(temp.find('a')['href'].split('/')))) 
        return sets

    def _save_new_data(self, soup,html_cont):
        is_saved = False
        # <input id="query" nslog="normal" nslog-type="10080015" name="word" type="text" autocomplete="off" autocorrect="off" value="谁与争锋">
        title=soup.find('title').contents[0]#,{'name':'word'})['value']
        path=os.path.join('.','webpages')#custom diectory for webpages
        if not os.path.exists(path):
            os.mkdir(path)
        with open(os.path.join(path ,title+'.html'), 'w') as f:
            f.write(html_cont.decode('utf-8'))
        return is_saved

    def parse(self, html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup((html_cont), 'lxml')
        sets = self._get_new_urls( soup)
        # print(sets)
        is_saved = self._save_new_data( soup,html_cont)
        return sets, is_saved


if __name__ == "__main__":
    import html_downloader
    dd=html_downloader.HtmlDownloader()
    content=dd.download('https://baike.baidu.com')
    parser = HtmlParser()
    import time
    start=time.time()
    new_urls, _ = parser.parse(content)
    cost=time.time()-start
    # print('\n'.join(new_urls),str(cost))
    print(new_urls)
