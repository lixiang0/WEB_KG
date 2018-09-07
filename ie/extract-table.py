import re
from scrapy.selector import Selector

import pickle as pk
import glob
from pathlib import Path
import os


# <div class="basic-info cmn-clearfix">
# <dl class="basicInfo-block basicInfo-left">
# <dt class="basicInfo-item name">中文名</dt>
# <dd class="basicInfo-item value">
# 托普卡帕故宫
# </dd>
# <dt class="basicInfo-item name">外文名</dt>
# <dd class="basicInfo-item value">
# Topkapı Sarayı
# </dd>
# </dl>

#<dl class="basicInfo-block basicInfo-right">
# <dt class="basicInfo-item name">灭亡时间</dt>
# <dd class="basicInfo-item value">
# 1921年
# </dd>
# <dt class="basicInfo-item name">文&nbsp;&nbsp;&nbsp;&nbsp;物</dt>
# <dd class="basicInfo-item value">
# <a target="_blank" href="/item/%E7%93%B7%E5%99%A8">瓷器</a>、官服、武器、盾牌
# </dd>
# <dt class="basicInfo-item name">建议游玩时长</dt>
# <dd class="basicInfo-item value">
# 1-2天
# </dd>
# </dl></div>

pages=glob.glob('../webpages/*')
savepath='./paged-table.bin'
print(len(pages))
print(pages[0])
paged=[]
if os.path.exists(savepath):
	paged=pk.load(open(savepath,'rb'))
	print('load state')
try:
	for page in pages:
		print('page:',page)
		if page in paged:
			continue
		contents = open(page,'r').read()
		info_data = {}
		
		#用Xpath提取出<div class="para"></div>中的所有内容
		selector=Selector(text=contents)
		title=''.join(selector.xpath('//h1/text()').extract()).replace('/','')
		names=selector.xpath('//dt[contains(@class,"basicInfo-item name")]').extract()
		values=selector.xpath('//dd[contains(@class,"basicInfo-item value")]').extract()
		print(len(names),len(values))
		lines=''
		for i,name in enumerate(names):
			#name
			temp=Selector(text=name).xpath('//dt/text()|//dt/a/text()').extract()
			name=''.join(temp).replace('\n','')
			#value
			temp=Selector(text=values[i]).xpath('//dd/text()|//dd/a/text()').extract()
			value=''.join(temp).replace('\n','')

			lines+=name+'$$'+value+'\n'
			print(name,value)
		print('process file:'+str(title))
		output = open('./info-table/'+title+'.txt','w')
		output.write(lines)
		output.close()
		paged.append(page)
except Exception as e:
	print('exception:',str(e))
	pk.dump(paged,open(savepath,'wb'))
	print('save state done')
pk.dump(paged,open(savepath,'wb'))
print('save state done')


