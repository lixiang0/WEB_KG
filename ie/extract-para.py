import re
from scrapy.selector import Selector

import pickle
import glob
from pathlib import Path
import os,sys
import threading

print('loading pages')
pages=glob.glob('../webpages/*')
print('loading pages done.')
savepath='./paged.bin'

print(len(pages))
print(pages[0])
paged=[]
if os.path.exists(savepath):
	paged=pickle.load(open(savepath,'rb'))
	print('load state')
lock=threading.Lock()
fail_file=open('./fail_para.txt','w')
class MyThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self._running = True
	def terminate(self):
		self._running = False
	def extract(self,page):
		#用Xpath提取出<div class="para"></div>中的所有内容
		line=Selector(text=open(page,'r').read()).xpath('//div[contains(@class, "main-content")]')
		title=line.xpath('//h1//text()').extract()
		para=re.sub('\[[0-9]+\]', '', ''.join(word for word in line.xpath('//div[contains(@class, "para")]//text()').extract() if len(word)>1))
		# print(para)
		print('process file:'+str(title))
		output = open('./info-para/'+''.join(title).replace('/','')+'.txt','w')
		output.write(para)
		output.close()
	def run(self):
		try:
			while(True):
				if len(pages)>0:
					lock.acquire()
					page=pages[0]
					pages.remove(page)
					lock.release()
					self.extract(page)
					lock.acquire()
					paged.append(page)
					lock.release()
		except Exception as e:
			print('fail to extract..',str(e))
			fail_file.write(page)



list_thread=[]
try:
	print('start...')
	for i in range(12):
	    list_thread.append(MyThread())
	for th in list_thread:
	    th.start()
	    th.join()
except:
    for th in list_thread:
        th.terminate()
    print('error!', sys.exc_info()[0])
finally:
    print('save state')
    pickle.dump(paged, open('paged.bin', 'wb'))
    fail_file.close()


