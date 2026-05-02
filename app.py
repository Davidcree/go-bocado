from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_productos():
    return [
        {
            "id": 1,
            "nombre": "Empanaditas",
            "precio": 15,
            "imagen": "/static/img/empanadita.jpg"
        },
        {
            "id": 2,
            "nombre": "Tequeños",
            "precio": 18,
            "imagen": "/static/img/tequenos.jpg"
        },
        {
            "id": 3,
            "nombre": "Mini Sandwich",
            "precio": 20,
            "imagen": "/static/img/mini_sandwich.jpg"
        }
    ]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/productos")
def productos():
    return jsonify(get_productos())

