#### Tips


- 如果是项目问题，请提issue。
- 如果涉及到不方便公开的，请发邮件。


# 开源web知识图谱项目

- 爬取百度百科中文页面
- 抽取[100W+个三元组](https://raw.githubusercontent.com/lixiang0/WEB_KG/master/kg/triples.txt)
- 构建中文知识图谱

### 环境

- python 3.6
- requests:网络请求
- re:url正则匹配
- bs4:网页解析
- pickle:进度保存
- threading:多线程
- neo4j:知识图谱图数据库,安装可以参考[链接](http://blog.rubenxiao.com/posts/install-neo4j.html)
- pip install neo4j-driver：neo4j python驱动


### 代码目錄

- spider/ 抓取原始网页
- ie/ 从网页中解析正文，从正文中抽取结构化信息
- kg/ 抽取三元組，存入neo4j数据库


### 代码执行顺序：

```
python spider/spider_main.py
python ie/extract-para.py
python ie/extract-table.py
python kg/build-triple-from-table.py
python kg/insert_to_neo4j.py
```

### 知识图谱效果图

![](./kg/kg.png)

