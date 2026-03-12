import os
from flask import Flask

app = Flask(__name__)

APP_VERSION = os.getenv('APP_VERSION', 'local-dev')

HOSTNAME = os.getenv('HOSTNAME', 'unknown')

@app.route('/')
def home():
    """Главная страница"""
    return f"""
    <h1>👋 Привет!</h1>
    <p>CI/CD работает!.</p>
    <hr>
    <p>Версия: <code>{APP_VERSION}</code></p>
    <p>Хост: <code>{HOSTNAME}</code></p>
    """

@app.route('/version')
def version():
    """Эндпоинт для проверки версии"""
    return {'version': APP_VERSION, 'status': 'ok'}

@app.route('/health')
def health():
    """Эндпоинт для проверки здоровья"""
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)