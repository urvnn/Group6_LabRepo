import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Sample book data
books = [
    {'id': 0, 'title': 'A Fire Upon the Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'year_published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'year_published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

# Route to get all books
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# Route to get a book by ID
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if 'id' was provided in the request URL
    if 'id' in request.args:
        try:
            book_id = int(request.args['id'])  # Convert ID to integer
        except ValueError:
            return jsonify({"error": "Invalid ID format. ID must be an integer."}), 400
        
        # Filter books for the given ID
        results = [book for book in books if book['id'] == book_id]

        if results:
            return jsonify(results[0])  # Return the first match
        else:
            return jsonify({"error": "Book not found"}), 404
    else:
        return jsonify({"error": "No ID provided. Please specify an ID."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
