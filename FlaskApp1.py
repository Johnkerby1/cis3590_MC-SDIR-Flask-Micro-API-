from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data storage
DATA = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# ----------------------------------------
# /hello endpoint (GET)
# ----------------------------------------
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Welcome to CIS 3590 Flask API!",
        "status": "success"
    }), 200


# ----------------------------------------
# /data endpoint (GET + POST)
# ----------------------------------------
@app.route("/data", methods=["GET", "POST"])
def data():

    # GET → return all data
    if request.method == "GET":
        return jsonify({
            "count": len(DATA),
            "data": DATA
        }), 200

    # POST → add new item
    if request.method == "POST":
        new_item = request.get_json()

        if not new_item or "name" not in new_item:
            return jsonify({
                "error": "Invalid input. Provide a name."
            }), 400

        new_id = len(DATA) + 1
        item = {
            "id": new_id,
            "name": new_item["name"]
        }

        DATA.append(item)

        return jsonify({
            "message": "Item added successfully",
            "item": item
        }), 201


# ----------------------------------------
# Run App
# ----------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
