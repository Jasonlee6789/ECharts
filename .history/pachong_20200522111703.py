fronm  urllib import request
url = "http://www.baidu.com"
res = request.urlopen(url)
#  获取相应
print(res.info())
print(res.getcode())
print(res.geturl())