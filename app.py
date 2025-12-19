from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("map.html")

@app.route("/data")
def data():
    # デプロイ確認用ダミーデータ
    return jsonify([
        {
            "X": 0,
            "Y": 0,
            "areaX": 0,
            "areaY": 0,
            "lux": 100,
            "eco2": 400,
            "temperature": 25,
            "humidity": 50,
            "dust_density": 10,
            "timestamp": "2025-01-01T10:00:00"
        }
    ])

if __name__ == "__main__":
    app.run()
