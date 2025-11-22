import os
import sys
import threading
import logging
from flask import Flask

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def run_bot():
    """Запускает Telegram бота"""
    try:
        # Добавляем текущую директорию в путь
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        
        from main import bot
        logger.info("🚀 Starting Telegram Bot...")
        bot.run()
        
    except Exception as e:
        logger.error(f"❌ Bot failed: {e}")

@app.route('/')
def home():
    return """
    <html>
        <head><title>Music Bot</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1 style="color: green;">🎵 Music Bot is Running!</h1>
            <p>Use Telegram to interact with the bot.</p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    # Запускаем бота в отдельном потоке
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    logger.info("✅ Bot thread started")
    
    # Запускаем Flask
    logger.info("🌐 Flask server starting on port 5000")
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
