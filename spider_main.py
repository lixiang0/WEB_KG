import url_manager, html_downloader, html_parser
import pickle
import os
import sys
from multiprocessing.dummy import Pool as ThreadPool
import threading





class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while urls.has_new_url():
            global i
            lock.acquire()
            new_url = urls.get_new_url()
            lock.release()
            print('craw %d : %s' % (len(urls.old_urls), new_url))
            html_cont = downloader.download(new_url)
            new_urls, _ = parser.parse(new_url, html_cont)
            lock.acquire()
            urls.add_new_urls(new_urls)
            lock.release()


if __name__=='__main__':
    root_url = 'http://baike.baidu.com'
    lock=threading.Lock()
    urls = url_manager.UrlManager()
    downloader = html_downloader.HtmlDownloader()
    parser = html_parser.HtmlParser()
    try:
        if os.path.exists('urls.bin'):
            urls=pickle.load(open('urls.bin','rb'))
            MyThread().start()
            MyThread().start()
            MyThread().start()
            MyThread().start()
        else:
            urls.add_new_url(root_url)
            MyThread().start()
            MyThread().start()
            MyThread().start()
            MyThread().start()
    except:
        print('error!', sys.exc_info()[0])
    finally:
        pickle.dump(urls, open('urls.bin', 'wb'))
        print('done')