#!/usr/bin/env python3

import requests
from lxml import etree

headers = {'Cookie':'_s_tentry=www.cnblogs.com; Apache=1835318692028.5225.1471917396941; SINAGLOBAL=1835318692028.5225.1471917396941; ULV=1471917396951:1:1:1:1835318692028.5225.1471917396941:; login_sid_t=4355ae76baccf8065f1a8ee21410af4c; SSOLoginState=1472100625; un=d_shaowu@sina.com; wvr=6; UOR=www.cnblogs.com,widget.weibo.com,www.baidu.com; SUB=_2A256xUX_DeTxGedI7FYW9izMyjiIHXVZszA3rDV8PUNbmtBeLXjikW-Fnc2Do-rzYWdBr3bUrwoB8O8GwA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWsDXopZAwQwb.lAj_vhI8m5JpX5KMhUgL.Fo2cS0BNSoz7eKB2dJLoI7HiUJvkx5tt; SUHB=0A04Z2Z8J0WkF8; ALF=1503815982', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

rsp = requests.get('http://weibo.com/fhtsks?refer_flag=1001030103_&is_hot=1', headers = headers)

#print(dir(rsp))
#print(rsp.text)

html = rsp.text
#html = res.replace('\n', '')
print(len(html))

fd = open('test.html', 'w')
fd.write(html)
fd.close()

tree = etree.HTML(html)

nodes = tree.xpath('//div[@class="pf_intro"]/@title')
print(nodes)

for atom in nodes:
	print(atom.text)

