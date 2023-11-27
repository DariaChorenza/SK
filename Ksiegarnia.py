from flask import Flask, jsonify, request, abort, json

app = Flask(__name__)


with open('books.json') as f:
    books_data = json.load(f)

@app.route('/isbns', methods=['GET'])
def get_isbns():
    isbns = [book['isbn'] for book in books_data['books']]
    return jsonify(isbns)

@app.route('/isbns/<isbn>', methods=['GET'])
def get_book_by_isbn(isbn):
    book = next((b for b in books_data['books'] if b['isbn'] == isbn), None)
    if book:
        return jsonify(book)
    else:
        abort(404)

@app.route('/authors/<expression>', methods=['GET'])
def get_authors_by_expression(expression):
    authors = [book['author'] for book in books_data['books'] if expression.lower() in book['title'].lower()]
    return jsonify(authors)

@app.route('/isbns/<isbn>', methods=['PUT'])
def update_publisher(isbn):
    new_publisher = request.args.get('publisher')
    book = next((b for b in books_data['books'] if b['isbn'] == isbn), None)
    if book:
        book['publisher'] = new_publisher
        return jsonify({'message': 'Publisher updated successfully'})
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
