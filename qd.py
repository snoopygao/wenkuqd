import requests as rq
headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'BAIDUID=自己的内容:FG=1; BDUSS=自己的内容',
'Host': 'wenku.baidu.com',
'Referer': 'https://wenku.baidu.com/task/browse/daily',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}
url = "https://wenku.baidu.com/task/submit/signin"

result = rq.get(url,headers = headers)
