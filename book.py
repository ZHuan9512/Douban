import requests
from lxml import html,etree

def douban():
	start_url='https://book.douban.com/top250?start={}'
	headers={
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
			}
	k=1
	for i in range(10):
		url=start_url.format(i*25)
		
		response=requests.get(url,headers=headers)
		response.encoding='utf-8'
		res=response.content
		r=html.fromstring(res)
		result=r.xpath('//tr[@class="item"]')
		for results in result:
			name = results.xpath('td[2]/div[1]/a[@title]/text()')[0]
			book_link = results.xpath('td[2]/div[1]/a/@href')[0]
			author = results.xpath('td[2]/p[1]/text()')[0]
			score = results.xpath('td[2]/div[2]/span[2]/text()')[0]
			quote = results.xpath('td[2]/p[2]/span/text()')
			print("TOP%s"%str(k))
			if len(quote)>0:
				print(name)
				print(author)
				print(score)
				print(quote[0])
				print(book_link)
			else:
				print(name)
				print(author)
				print(score)
				print(book_link)
			print("=================================")
			with open("豆瓣图书TOP250.txt","a",encoding='utf-8')as f:
				if len(quote)>0:
					f.write("TOP %s:\n书名: %s\n作者: %s\n评分: %s\n引言: %s\n"%(k,name,author,score,quote[0]))
				else:
					f.write("TOP %s:\n书名: %s\n作者: %s\n评分: %s\n引言: \n"%(k,name,author,score))
				f.write("================================\n")
				f.close()

			k+=1
douban()
