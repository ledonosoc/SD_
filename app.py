from flask import Flask, jsonify, request
import json
import Producer
import Consumer

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register', methods=['POST'])
#def write_json(new_data, filename='users.json'):
#    with open(filename,'r+') as file:
#       file_data = json.load(file)
#       #content['users'].append(new_data)
#       #file_data.update(content)
#       file_data["Usuarios"].append(new_data)
#       file.seek(0)
#       json.dump(file_data, file, indent = 4)  

def get_body():
    #users = request.form['users']
    data = request.get_json()
    #user = data['user']
    #password = data['pass']
    new_user = {"user":f"{data['user']}",
                "pass":f"{data['pass']}"
                }
    print(new_user)
    with open('users.json', 'r+') as file:
        file_data = json.load(file)
        file_data["Usuarios"].append(new_user)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

    #write_json(new_user)
    return (new_user)



#f = open('users.json', 'r')
#content = json.load(f)

#f = open('users1.json', 'w')

#new_name = input('username: ')
#new_password = input('password: ')
    
#new_user = {"Username":f"{new_name}",
#            "Password": f"{new_password}"
#            }

#write_json(new_user)


@app.route('/login', methods=['POST'])
def login_user():
    body = request.get_json()
    user = body['user']
    password = body['pass']
    print('user= ', user)
    print('pass= ', password)
    if body is None:
        return "The request body is null", 400
    if 'user' not in body:
        return "No user input", 400
    if 'pass' not in body:
        return "No pass input", 400
    else:
        f = open('users.json', 'r+')
        content = json.load(f)

        for c in content:
            for e in content["Usuarios"]:
                print(e["user"])
                print(e["pass"])
                if user == e["user"]:
                    if password == e["pass"]:
                        print('usuario correctamente logeado!')
                    else:
                        print('(pass)Una de las credenciales ingresada incorrectamente.')
                        Producer.Producer(user)
                else: 
                    print('(user)Una de las credenciales ingresada incorrectamente.')
    return "ok", 200
@app.route('/blocked-users', methods=['GET'])
def get_blocked():
    lista = json.dumps({"users-blocked":Consumer.Consumer()})
    return lista

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
