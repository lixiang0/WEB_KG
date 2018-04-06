import re
from scrapy.selector import Selector

import pickle as pk
import glob
from pathlib import Path
import os

pages=glob.glob('/data/ruben/data/webpages/*')
savepath='./paged.bin'
print(len(pages))
print(pages[0])
paged=[]
if os.path.exists(savepath):
	paged=pk.load(open(savepath,'rb'))
	print('load state')
try:
	for page in pages:
		if page in paged:
			continue
		contents = open(page,'r').read()
		info_data = {}
		# print(contents)
		#用Xpath提取出<div class="para"></div>中的所有内容
		selector=Selector(text=contents)
		line=selector.xpath('//div[contains(@class, "main-content")]')
		title=line.xpath('//h1/text()').extract()
		para=''.join(word for word in line.xpath('//div[contains(@class, "para")]/text()').extract() if len(word)>1)
		print('process file:'+str(title))
		output = open('./info-para/'+''.join(title)+'.txt','w')
		output.write(para)
		output.close()
		paged.append(page)
except:
	pk.dump(paged,open(savepath,'wb'))
	print('save state done')