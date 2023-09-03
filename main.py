from flask import Flask, render_template, request, jsonify
from data import data

app= Flask (__name__)

@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"sucess"
    
    })

@app.route("/star")
def stars():
    name=request.args.get("name")
    stars_data=next(item for item in data if item["name"]==name)
    return jsonify({
        "data": stars_data,
        "message":"sucess"
    })

if __name__ == "__main__":
    app.run()

