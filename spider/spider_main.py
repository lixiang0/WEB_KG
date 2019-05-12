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
                LOCK.acquire()
                new_url = urls.get_new_url()
                LOCK.release()
                print('craw %d' % (len(urls.old_urls)))
                html_cont = downloader.download(new_url)
                new_urls, _ = parser.parse(new_url, html_cont)
                LOCK.acquire()
                urls.add_new_urls(new_urls)
                LOCK.release()
        except:
            print('save state')
            pickle.dump(urls, open('urls.bin', 'wb'))


if __name__=='__main__':
    PATH='urls.pkl'
    root_url = 'http://baike.baidu.com'
    LOCK=threading.Lock()
    urls = url_manager.UrlManager()
    downloader = html_downloader.HtmlDownloader()
    parser = html_parser.HtmlParser()
    threads=[]
    count_thread=1
    if os.path.exists(PATH):
        urls=pickle.load(open(PATH,'rb'))
    else:
        urls.add_new_url(root_url)
    length=len(urls.new_urls)
    print(f'build urls,length={length}')
    for i in range(count_thread):
        print(f'build thread {i}...')
        threads.append(MyThread())
    try:
        for t in threads:
            t.start()
            t.join()
    except:
        for t in threads:
            t.terminate()
        print('error!', sys.exc_info()[0])
    finally:
        print('finished,saving state')
        pickle.dump(urls, open(PATH, 'wb'))
