# 开源web知识图谱项目

- 爬取百度百科中文页面
- 抽取三元组
- 构建中文知识图谱

![./kg.png]()

### 环境

- python 3.6
- requests:网络请求
- re:url匹配
- bs4:网页解析
- pickle:进度保存
- threading:线程
- neo4j:知识图谱图数据库
- pip install neo4j-driver：neo4j python驱动

### 目錄

- spider/ 抓取網頁
- ie/ 抽取網頁信息
- kg/ 抽取三元組

### 执行：

```
python spider_main.py
```

### 网页保存路径：

我的是：```/data/webpages```,如需修改更改```html_parser.py```文件下的路径即可。
### 运行log:

```
craw 68357 : http://baike.baidu.com/item/%E8%BF%87%E9%80%9F%E7%BB%AF%E9%97%BB
Save to disk filename:webpages/非常主播
craw 68358 : http://baike.baidu.com/item/%E5%B8%82%E5%9C%BA%E8%A7%84%E6%A8%A1
Save to disk filename:webpages/市场规模
craw 68359 : https://baike.baidu.com/item/%E6%B8%85%E6%99%8F%E5%9B%AD
Save to disk filename:webpages/清晏园
craw 68360 : http://baike.baidu.com/item/%E5%AE%9D%E8%8E%B1%E5%9D%9E
Save to disk filename:webpages/宝莱坞
craw 68361 : https://baike.baidu.com/item/%E5%BA%93%E6%96%AF%E7%A7%91%E5%9F%8E
Save to disk filename:webpages/库斯科城
```

