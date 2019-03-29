from flask import Flask, render_template, Response, request
import requests
import hashlib
import redis

app = Flask(__name__)
# hostname defined in docker-compose
cache = redis.StrictRedis(host='redis', port=6379, db=0)
default_name = "Kurt Marshall"
salt = 'UNIQ_SALT'

@app.route('/', methods=['GET', 'POST'])
def main_page():
    name = default_name
    if request.method == 'POST':
        name = request.form['name']
    salted = name + salt
    name_hash = hashlib.sha256(salted.encode()).hexdigest()

    # Jinja injects name to template
    return render_template("hello.html", name=name, name_hash=name_hash)

@app.route('/monster/<name>')
def get_monster(name):
    image = cache.get(name)
    if image is None:
        print("Cache miss", flush=True)
        # call monster service
        r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
        image = r.content
        cache.set(name, image)
    return Response(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
