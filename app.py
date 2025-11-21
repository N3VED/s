from flask import Flask
from routes.tasks import tasks_bp

app = Flask(__name__)

# подключаем наши роуты (маршруты)
app.register_blueprint(tasks_bp)

@app.route("/")
def home():
    return "Todo API работает! (структура проекта обновлена)"

if __name__ == "__main__":
    app.run(debug=True)
