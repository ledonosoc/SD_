from flask import Flask, request
import json

# create the Flask app
app = Flask(__name__)

def GetBlocked(blocklist):
    bloqueados = json.loads(blocklist)
    bloqueadosactuales = json.dump({})
    for user in bloqueados:
        if time.time()-bloqueados[user]<60:
            bloqueadosactuales.update(json.dump({user:bloqueados[user]}))
    with open('BlockedUsers.json', 'w') as file:
        json.dump(bloqueadosactuales, file, indent=4)
    return bloqueadosactuales

@app.route('/blocked')
def blocked():
    blocklist = open('BlockedUsers.json','r')
    return GetBlocked(blocklist)

if __name__ == '__main__':
    app.run(debug=True, port=5000)