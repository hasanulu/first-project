from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis bağlantısı (Konteyner ismiyle bağlanıyoruz!)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    return cache.incr('hits')

@app.route('/')
def hello():
    count = get_hit_count()
    return f'<h1>Merhaba! Bu sayfa {count} kez görüntülendi.</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)