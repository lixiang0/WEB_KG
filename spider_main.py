# coding:utf-8
import url_manager, html_downloader, html_parser
import pickle
import os
import sys


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()

    def craw(self, root_url):
        count = len(self.urls.old_urls)
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print('craw %d : %s' % (count, new_url))
            html_cont = self.downloader.download(new_url)
            # print(html_cont)
            new_urls, _ = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            # print('mark')
            count = count + 1

if __name__=='__main__':
    root_url = 'http://baike.baidu.com'
    obj_spider = SpiderMain()
    if os.path.exists('urls.bin'):
        obj_spider.urls=pickle.load(open('urls.bin','rb'))
    try:
        obj_spider.craw(root_url)
    except:
        print('error!', sys.exc_info()[0])
    finally:
        pickle.dump(obj_spider.urls, open('urls.bin', 'wb'))
