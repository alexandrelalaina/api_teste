from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
                    {'nome':'Alexandre',
                     'habilidades':['Python', 'Flask']
                     },
                    {'nome':'Joao',
                     'habilidades':['Java', 'PHP']
                     }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            msg = 'Registro de id {} não encontrado!'.format(id)
            response = {'status': '#NDF', 'mensagem': msg}
        except Exception:
            msg = 'Erro desconhecido!'
            response = {'status': '#ERRO', 'mensagem': msg}
        return response

    def put(self):
        return "implementar PUT"
    def delete(self):
        return "implementar DELETE"

api.add_resource(Desenvolvedor, '/dev/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)