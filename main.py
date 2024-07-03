from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

supercars = {
    'Dino 206/246/208/308' : ['640px-Ferrari_Dino_246_F1.jpg', '123'],
    'Ferrari 308/208' : ['640px-1984_Ferrari_308_GTB_qv.jpg', '123'],
    'Ferrari 328' : ['640px-Ferrari.targa.arp.750pix.jpg', '123'],
    'Ferrari 348 TB/TB/GTB/GTS/Spider/Speziale/GT Competizione' : ['610px-1993_Ferrari_348_TS_3.4_Front.jpg', '123'],
    'Ferrari 355 Berlinetta/GTS/Spider/F1 Spider Serie Fiorano' : ['640px-Ferrari_F355_Coupé.jpg', '123']
}
@app.route("/")
def index():
    return render_template('home.html')

@app.route('/time')
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(current_time=current_time)

@app.route("/history/")
def history():
    return render_template("history.html")

@app.route("/supercar/")
def supercar():
    return render_template("supercar.html", supercars=supercars)

@app.route("/ddepp/")
def index_3():
    return render_template("index_4.html")

if __name__ == "__main__":
    app.run()