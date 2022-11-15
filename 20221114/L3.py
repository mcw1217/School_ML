import json
import urllib.request as wclient


def test1():
    data = {"name": "mcw1217", "age": 22}

    jmsg = json.dumps(data)

    url = "http://localhost:2022/test2/" + jmsg
    url = url.replace(" ", "%20")  # 띄어쓰기를 인코딩 시키는 것

    print(url)
    connection = wclient.urlopen(url)
    jmsg = connection.read()
    print("From:" , jmsg)
    data = json.loads(jmsg)
    print(data["server"])


test1()
