from flask import Flask
import json

webserver = Flask(__name__)

# http://localhost
@webserver.route("/")
def index():
    msg = "hello"

    return msg


# http://localhost:2022/
@webserver.route("/test1")
def test1():
    msg = "hello world"
    return msg


# http://localhost:2022/test2/'{"member":"test", "age":20, "tel":"01071433652"}'
@webserver.route("/test2/<para>")
def test2(para):
    print(para)
    msg = para

    data = json.loads(para)

    return msg


webserver.run(port=2022, host="0.0.0.0")
