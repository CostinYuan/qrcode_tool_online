from flask import Flask, request
import flask
import qrcode
import io


app = Flask(__name__)

@app.route('/')
def qr():
    return flask.render_template('qrcode.html')

@app.route('/qr')
def qr_img():
    data = request.form.get("data")

    img = qrcode.make(data)
    bi = io.BytesIO()  # 创建一个BytesIO对象，用于存储二维码图像数据
    img.save(bi, "png")  # 调用img对象的save方法将二维码图像数据以PNG编码格式写入bi对象管理的内存空间
    bi.seek(0)  # 将bi对象内部的位置指针移动到图像数据的其实位置

    return flask.send_file(bi, "image/png")



if __name__ == '__main__':
    app.run(debug=True)