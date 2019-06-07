from flask import Flask, render_template, request, make_response
from json import JSONEncoder
from io import BytesIO
import ds_drawer
import mimetypes
app = Flask("SAMDrawer")

# 主页
@app.route("/", methods=["GET"])
def root():
    return render_template("main.html")

# 绘制
@app.route("/draw", methods=["POST", "GET"])
def draw():
    # request.form是一个dict-like object，表示客户端提交的数据。
    if "string" not in request.form:
        # 直接返回文本即可。
        return encode_json({
            "code": -1,
            "message": "Please give a string."
        })
    string = request.form["string"]
    if len(string) > 50:
        return encode_json({
            "code": -1,
            "message": "Too long.."
        })
    svg_data = ""
    target = ds_drawer.generate_graph(string, "svg")
    with open(target, "r") as file:
        svg_data = file.read()
    # 一切正常时直接发回结果。
    return encode_json({
        "code": 0,
        "data": svg_data
    })

# 编码obj到JSON。
def encode_json(obj):
    return JSONEncoder().encode(obj)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="90")
