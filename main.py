from flask import Flask, request, render_template, url_for
import qrcode

app = Flask(__name__)

@app.route('/')
def qr():
    return render_template('qrcode.html')

@app.route('/qr_img', methods=['POST'])
def qr_img():
    data = request.form.get("data")
    img = qrcode.make(data)
    img.save('static\\qrcode.png')
    return '<p>快扫我：<img src="%s" alt=""></p>' % url_for('static', filename='qrcode.png')



if __name__ == '__main__':
    app.run(debug=True)