from flask import Flask, jsonify

app = Flask(__name__)

DATA = [
    {"id": 1, "Campus": "MMC", "Lat": 25.76, "Lon": -80.36},
    {"id": 2, "Campus": "BBC", "Lat": 25.90, "Lon": -80.13},
    {"id": 3, "Campus": "DC", "Lat": 38.89, "Lon": -77.01}
]

next_id = 4


@app.route("/")
def index():
    return """
    <h1>FIU Campuses API</h1>
    <p>Try these endpoints:</p>
    <ul>
        <li><a href="/api/health">/api/health</a></li>
        <li><a href="/api/items">/api/items</a></li>
        <li><a href="/api/items/1">/api/items/1</a></li>
    </ul>
    """


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/items")
def items():
    return jsonify(DATA), 200


@app.route("/api/items/<int:id>")
def item(id):
    for i in DATA:
        if i["id"] == id:
            return jsonify(i), 200
    return jsonify({"error": "Item not found"}), 404


@app.route("/homepage")
def homepage():
    return "<h1>Hello! Welcome to the Campus HomePage</h1>"


if __name__ == "__main__":
    app.run(debug=True)
