import re
from scrapy.selector import Selector


import glob
from pathlib import Path


pages=glob.glob('/data/ruben/data/webpages/*')
print(len(pages))
print(pages[0])

for page in pages:
	contents = open(page,'r').read()
	info_data = {}
	# print(contents)
	#用Xpath提取出<div class="para"></div>中的所有内容
	selector=Selector(text=contents)
	line=selector.xpath('//div[contains(@class, "main-content")]')
	title=line.xpath('//h1/text()').extract()
	para=''.join(word for word in line.xpath('//div[contains(@class, "para")]/text()').extract() if len(word)>1)
	output = open('./info/'+''.join(title)+'.txt','w')
	output.write(para)
	output.close()
	break