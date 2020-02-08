from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
                    {'nome':'Alexandre',
                     'habilidades':['Python', 'Flask']
                     },
                    {'nome':'Janaina',
                     'habilidades':['Java', 'PHP']
                     }
]

@app.route('/dev/<int:id>/')
def desenvolvedor(id):
    desenvolvedor = desenvolvedores[id]
    print(desenvolvedor)
    return jsonify(desenvolvedor)

@app.route('/<int:id>/')
def pessoa(id):
    return jsonify({'id':id,
                    'pessoa:':'Alexandre La Laina',
                    'idade:':35})

# @app.route('/soma', methods=['POST', 'PUT', 'GET'])
# def soma():
#     # dados = json.loads(request.data)
#     # request.data ---- recupera as info do BODY
#     dados = json.loads(request.data)
#     print(dados)
#     return 'soma'

if __name__ == '__main__':
    app.run(debug=True)




