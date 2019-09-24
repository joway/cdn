# -*- coding: utf-8 -*-
from qiniu import Auth
from qiniu import BucketManager
import requests
import os
access_key = ''
secret_key = ''
q = Auth(access_key, secret_key)
bucket = BucketManager(q)
bucket_name = 'block'
# 前缀
prefix = None
# 列举条目
limit = 200000000000
# 列举出除'/'的所有文件以及以'/'为分隔的所有前缀
delimiter = None
# 标记
marker = None
path = '/Users/joway/Code/github/env/cdn/'
ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
for i in ret['items']:
    print(i['key'])
    base_url = 'http://xxx.yangapp.com/'+i['key']
    print(base_url)
    #如果空间有时间戳防盗链或是私有空间，可以调用该方法生成私有链接
    private_url = q.private_download_url(base_url, expires=100)
    print(private_url)
    r = requests.get(private_url)
    if r.content:
        filename = path + i['key']
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        if not os.path.exists(path):
            os.makedirs(path)
        file = open(filename, "wb")
        file.write(r.content)
        file.flush()
        file.close()
