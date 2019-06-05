import requests

# 功能：获取对应网址的网页
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        headers_pc = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                   'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9,image/webp, * / *;q = 0.8'}
        # headers_mobile={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36',
        #                 "Accept":"text / html, application / xhtml + xml, application / xml;q = 0.9,image/webp, * / *;q = 0.8"}
        response = requests.get(url,headers=headers_pc,timeout=10)
        if response.status_code != 200:
            return None
        return response.content


if __name__ == "__main__":
    #https://baike.baidu.com/item/%E6%96%87%E6%B1%87%E6%8A%A5?bk_fr=chain_bottom&timestamp=1559566601712
    downloader=HtmlDownloader()
    htm=downloader.download('https://baike.baidu.com/item/文汇报').decode('utf-8')
    content=open('temp.html','w')#wpf=3&ldr=1&page=1&insf=1&_=1559569199226
    content.write(htm)
    # 1559566851.4734867
    # 1559569199226
    # 1559567213000


