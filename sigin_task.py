#_*_encoding:utf-8_*_
import sys
import time
from Account import account


debug = 1
version = "7.7.7"
if debug == 1:
    base_url = "https://123.59.87.5:12308/api.php?"
else:
    base_url = "https://aa.tangdou.com:12308/api.php?"
today=time.strftime("%Y%m%d",time.localtime(time.time()))
print(today)
exit()
account_info = account.login("13681504094","a1234567",version,base_url)
today=time.strftime("%Y%m%d",time.localtime(time.time()))
