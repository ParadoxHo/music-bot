import os
import subprocess
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Music Bot is running!"

if __name__ == '__main__':
    # Запускаем бота в фоновом режиме
    if os.path.exists('main.py'):
        subprocess.Popen(['python', 'main.py'])
    elif os.path.exists('/opt/render/project/src/main.py'):
        subprocess.Popen(['python', '/opt/render/project/src/main.py'])
    
    # Запускаем Flask сервер
    app.run(host='0.0.0.0', port=5000)
