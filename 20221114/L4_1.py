import json
import urllib.request as wclient
import random

def test1(a,b):
    data = {}
    data["a"] = random.randint(0,100)
    data["b"] = random.randint(0,100)

    jmsg = json.dumps(data)

    url = "http://localhost:2022/test2/" + jmsg
    url = url.replace(" ", "%20")  # 띄어쓰기를 인코딩 시키는 것

    print(url)
    connection = wclient.urlopen(url)
    jmsg = connection.read()
    print("From:" , jmsg)
    data = json.loads(jmsg)
    print("sum:",data["result"])


test1()
