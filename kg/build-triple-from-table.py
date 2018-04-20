import glob
import os
import re
import pickle as pkl
pages=glob.glob('../info-table/*')

# pattern=re.compile(r'[\u4e00-\u9fa5]+')
print(len(pages),pages[0])


class entity:
	def __init__(self):
		self.name=''
		self.attr=dict()
	def set_name(self,name):
		self.name=name
	def add_attr(self,attr,name):
			self.attr[attr]=name
attrs=[]
entities=[]
for page in pages:
	name=page.split('/')[-1][:-4]
	lines=open(page).readlines(0)
	ent=entity()
	ent.name=name
	for line in lines:
		arrs=line.split('$$')
		attrs.append(arrs[0])
		ent.add_attr(arrs[0],arrs[1])
	entities.append(ent)
	break
print(len(attrs),len(entities))
pkl.dump(attrs,open('./attrs.bin','wb'))
pkl.dump(entities,open('./entities.bin','wb'))