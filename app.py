from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://Test_app:kBV30N2iBv6KEeni@tutedude-project.madp0ix.mongodb.net/")
db = client['tutedude']
collection = db['submissions']

@app.route('/', methods=['GET', 'POST'])
def form():
    error_message = None

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        if name and password:
            try:
                collection.insert_one({'name': name, 'password': password})
                return redirect(url_for('success'))
            except Exception as e:
                error_message = f"Error saving to database: {str(e)}"

    return render_template('form.html', error_message=error_message)

@app.route('/success')
def success():
    return "<h1>Data submitted successfully!</h1><a href='/'>Go back</a>"

@app.route('/api', methods=['GET'])
def api():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

