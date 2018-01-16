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
                print('craw %d : %s' % (len(urls.old_urls), new_url))
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
    th1 = MyThread()
    th2 = MyThread()
    th3 = MyThread()
    th4 = MyThread()
    try:
        if os.path.exists('urls.bin'):
            urls=pickle.load(open('urls.bin','rb'))
        else:
            urls.add_new_url(root_url)
        th1.start()
        th2.start()
        th3.start()
        th4.start()
        th1.join()
        th2.join()
        th3.join()
        th4.join()
    except:
        th1.terminate()
        th2.terminate()
        th3.terminate()
        th4.terminate()
        print('error!', sys.exc_info()[0])
    finally:
        print('save state')
        pickle.dump(urls, open('urls.bin', 'wb'))