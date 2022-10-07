import requests
import base64
import mmh3
r=requests.get('https://www.baidu.com/favicon.ico') 
r1=r.content
r2=base64.encodebytes(r1)
r3=mmh3.hash(r2)
print('http.favicon.hash:'+str(r3))