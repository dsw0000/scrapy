#!/usr/bin python3

from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='phantomjs')

cookie_str = "_s_tentry=www.cnblogs.com; Apache=1835318692028.5225.1471917396941; SINAGLOBAL=1835318692028.5225.1471917396941; ULV=1471917396951:1:1:1:1835318692028.5225.1471917396941:; login_sid_t=4355ae76baccf8065f1a8ee21410af4c; SSOLoginState=1472100625; un=d_shaowu@sina.com; wvr=6; UOR=www.cnblogs.com,widget.weibo.com,www.baidu.com; SUB=_2A256xUX_DeTxGedI7FYW9izMyjiIHXVZszA3rDV8PUNbmtBeLXjikW-Fnc2Do-rzYWdBr3bUrwoB8O8GwA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWsDXopZAwQwb.lAj_vhI8m5JpX5KMhUgL.Fo2cS0BNSoz7eKB2dJLoI7HiUJvkx5tt; SUHB=0A04Z2Z8J0WkF8; ALF=1503815982"
"""
cookie = {}
tmp = cookie_str.split('; ')
for atom in tmp:
	res = atom.split('=')
	cookie[res[0]] = res[1]
"""
#driver.add_cookie({'Cookie':cookie_str})

driver.get("http://weibo.com/fhtsks?refer_flag=1001030103_&is_hot=1")

time.sleep(3)

html = driver.page_source.encode('gbk', 'ignore')
print(html)

driver.close()
