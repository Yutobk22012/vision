from flask import Flask, render_template, jsonify
import pymysql
from datetime import datetime, timezone, timedelta

JST = timezone(timedelta(hours=9))

app = Flask(__name__)

# === DB接続設定 ===
def fetch_data():
    conn = pymysql.connect(
        host="192.168.0.199",
        user="online",
        password="pass",
        database="test",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT X, Y, areaX, areaY, lux, eco2, temperature, humidity, dust_density, moisture, timestamp FROM nx10")
            data = cursor.fetchall()

            # timestampをISO形式に変換
            for d in data:
                if isinstance(d["timestamp"], datetime):
                    d["timestamp"] = d["timestamp"].astimezone(JST).isoformat()

    return data

@app.route("/")
def index():
    return render_template("map.html")

@app.route("/data")
def data():
    return jsonify(fetch_data())

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=False)
