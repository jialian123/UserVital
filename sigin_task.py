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
today=int(time.strftime("%Y%m%d",time.localtime(time.time())))
account_info = account.login("13681504094","a1234567",version,base_url)
#签到命令
days = 9
with open("./redis_commands.txt",'w+',encoding="utf-8") as file_handle:
    file_handle.writelines("签到命令:\n")
    while days > 0:
        file_handle.writelines("hset main:uv:sign:in:{} {} 1\n".format(account_info['uid'],today))
        today -= 1
        days -= 1
