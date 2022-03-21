from flask import Flask, make_response, jsonify,request



POSTS = [
    {
        'id':1,
        'title': 'tytul1',
        'text': 'text1'
    },
    {
        'id': 2,
        'title': 'tytul2',
        'text': 'text2'
    },
    {
        'id': 3,
        'title': 'tytul3',
        'text': 'text3'
    },
    {
        'id': 4,
        'title': 'tytul4',
        'text': 'text4'
    },
]
app = Flask(__name__)

@app.route('/posts', methods=['GET','POST'])
def items():
    response_date = {
        'success': True,
        'data': []
    }

    if request.method == 'GET':
        response_date['data'] = POSTS
        return  jsonify((response_date))
    elif request.method == 'POST':
        data = request.json
        if 'id' not in data or 'title' not in data or 'text' not in data:
            response_date['success'] = False
            response_date['error'] = "please provide all required information"
            response = jsonify(response_date)
            response.status_code = 400
        else:
            POSTS.append(data)
            response_date['data'] == POSTS
            response = jsonify(response_date)
            response.status_code = 201
        return response

    return jsonify(response_date)


@app.route('/')
def index():
    # print(request.headers)
    # print(f'method: {request.method}')
    # print(f'path: {request.path}')
    # print(f'url: {request.url}')
    # print(request.headers['Authorization'])
    # print(request.headers['Content-Type'])
    # print((type(request.json)))
    # print(request.json['name'])
    response = jsonify([{'id':1,'title':'tytul'}, {'id':1,'title':'tytul'}])
    # response.headers['Content-Type'] = 'application/json'
    return  response

@app.route('/posts/<int:post_id>')
def item(post_id):
    response_date = {
        'success': True,
        'data': []
    }

    try:
        item = [post for post in POSTS if post['id'] == post_id][0]
    except IndexError:
        response_date['success'] = False
        response_date['error'] = 'Not Found'
        response = jsonify(response_date)
        response.status_code = 404
    else:
        response_date['data'] = item
        response = jsonify(response_date)
    return response

@app.errorhandler(404)
def not_found(error):
    response_date = {
        'success': False,
        'data': [],
        'error': 'Not Found'
    }

    response = jsonify(response_date)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)





