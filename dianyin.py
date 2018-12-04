import requests
from lxml import etree

def top_movie():
	k=1
	start_url="https://movie.douban.com/top250?start={}&filter="
	headers={
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
		}
	for i in range(10):
		url = start_url.format(i*25)
		response = requests.get(url,headers=headers)
		#if response.status_code == 200:
			#print(response.text)
		res = response.text
		html = etree.HTML(res)
		movie_list = html.xpath('//div[@class="info"]') 
		#print(movie_list)
		for movie in movie_list:
			title=movie.xpath('div[@class="hd"]/a/span/text()')[0]
			#print(title)
			num=movie.xpath('div[@class="bd"]/div/span[2]/text()')[0]
			#print(num)
			quote=movie.xpath('div[@class="bd"]/p[2]/span/text()')
			#print(quote)
			url=movie.xpath('div[@class="hd"]/a/@href')[0]
			print(url)
			with open("豆瓣电影TOP250.txt","a",encoding="utf-8")as f:
				if len(quote)>0:
					f.write("TOP %s\n片名: %s\n评分: %s\n简评: %s\n链接: %s\n"%(k,title,num,quote[0],url))
					f.write("=====================\n")
					f.close()
				else:
					f.write("TOP %s\n片名: %s\n评分: %s\n简评:\n链接: %s\n"%(k,title,num,url))
					f.write("=====================\n")
					f.close()
			k+=1
			
top_movie()

