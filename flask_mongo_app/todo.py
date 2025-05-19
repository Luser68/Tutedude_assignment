from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://Test_app:kBV30N2iBv6KEeni@tutedude-project.madp0ix.mongodb.net/")
db = client['tutedude']
collection = db['todos']

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form['item_name']
    item_description = request.form['item_description']

    todo_item = {
        'item_name': item_name,
        'item_description': item_description
    }

    try:
        collection.insert_one(todo_item)
        return jsonify({"message": "To-Do item added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": f"Error saving to database: {str(e)}"}), 500

