import url_manager, html_downloader, html_parser
import pickle
import os
import sys
import threading





class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
    def terminate(self):
        self._running = False
    def run(self):
        try:
            while urls.has_new_url() and self._running:
                global i
                lock.acquire()
                new_url = urls.get_new_url()
                lock.release()
                print('craw %d' % (len(urls.old_urls)))
                html_cont = downloader.download(new_url)
                new_urls, _ = parser.parse(new_url, html_cont)
                lock.acquire()
                urls.add_new_urls(new_urls)
                lock.release()
        except:
            print('save state')
            pickle.dump(urls, open('urls.bin', 'wb'))


if __name__=='__main__':
    root_url = 'http://baike.baidu.com'
    lock=threading.Lock()
    urls = url_manager.UrlManager()
    downloader = html_downloader.HtmlDownloader()
    parser = html_parser.HtmlParser()
    list_thread=[]
    count_thread=12
    for i in range(count_thread):
        list_thread.append(MyThread())
    try:
        if os.path.exists('urls.bin'):
            urls=pickle.load(open('urls.bin','rb'))
        else:
            urls.add_new_url(root_url)
        for th in list_thread:
            th.start()
            th.join()
    except:
        for th in list_thread:
            th.terminate()
        print('error!', sys.exc_info()[0])
    finally:
        print('save state')
        pickle.dump(urls, open('urls.bin', 'wb'))
