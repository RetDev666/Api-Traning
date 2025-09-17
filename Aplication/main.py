import os.path
from flask import Flask, request, jsonify, render_template
import random
from werkzeug.utils import send_from_directory

app = Flask(__name__,
            template_folder='../Templates',
            static_folder='../Static')

# Дані
animals = ["🐱 Кіт", "🐶 Собака", "🐸 Жаба", "🐰 Заєць", "🦊 Лисиця"]
colors = ["червоний", "синій", "зелений", "жовтий", "рожевий"]
jokes = [
    "Чому комп'ютер пішов до лікаря? Бо в нього був вірус! 💻",
    "Що каже сир на фото? Молоко! 🧀",
    "Чому риба не грає теніс? Боїться сітки! 🐟"
]


def check_files():
    """Перевірка існування необхідних файлів та папок"""
    template_path = os.path.join(os.path.dirname(__file__), '../Templates')
    static_path = os.path.join(os.path.dirname(__file__), '../Static')

    # Перевіряємо кожен шлях окремо
    if not os.path.exists(template_path):
        print(f"❌ ПОМИЛКА: Папка Templates не знайдена: {template_path}")
        return False

    if not os.path.exists(static_path):
        print(f"❌ ПОМИЛКА: Папка Static не знайдена: {static_path}")
        return False

    # Перевіряємо index.html
    index_html = os.path.join(template_path, 'index.html')
    if not os.path.exists(index_html):
        print(f"❌ ПОМИЛКА: Файл index.html не знайдено: {index_html}")
        print("📁 Переконайтеся, що структура папок правильна:")
        print("   Templates/")
        print("   └── index.html")
        print("   Static/")
        print("   ├── CSS/")
        print("   │   └── style.css")
        print("   └── JS/")
        print("       └── script.js")
        return False

    return True


# Головна сторінка
@app.route('/')
def home():
    return render_template('index.html')


# Маршрути для статичних файлів
@app.route('/CSS/<path:filename>')
def css_files(filename):
    return send_from_directory('../Static/CSS', filename)


@app.route('/JS/<path:filename>')
def js_files(filename):
    return send_from_directory('../Static/JS', filename)


# API endpoints
@app.route('/api/animal')
def random_animal():
    animal = random.choice(animals)
    return jsonify({"message": f"Твоя тварина: {animal} 🎉"})


@app.route('/api/color')
def random_color():
    color = random.choice(colors)
    return jsonify({"message": f"Твій колір: {color} 🌈"})


@app.route('/api/joke')
def joke():
    joke = random.choice(jokes)
    return jsonify({"message": joke})


@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Не надіслано даних"}), 400

        num1 = data.get('num1')
        num2 = data.get('num2')

        if num1 is None or num2 is None:
            return jsonify({"error": "Потрібно вказати обидва числа"}), 400

        result = num1 + num2
        return jsonify({
            "message": f"🧮 {num1} + {num2} = {result} ✨"
        })
    except Exception as e:
        return jsonify({"error": "Помилка в обчисленні"}), 400

@app.route('/api/mines', methods=['POST'])
def mines():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Не надіслано даних"}), 400

        num3 = data.get('num3')
        num4 = data.get('num4')

        if num3 is None or num4 is None:
            return jsonify({"error": "Потрібно вказати обидва числа"}), 400

        result2 = num3 - num4
        return jsonify({
            "message": f"🧮 {num3} - {num4} = {result2} ✨"
        })
    except Exception as e:
        return jsonify({"error": "Помилка в обчисленні"}), 400

@app.route('/api/greeting', methods=['POST'])
def getGreeting():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Не надіслано даних"}), 400

        name = data.get('name')
        if not name:
            return jsonify({"error": "Не вказано ім'я"}), 400

        age = data.get('age', 0)

        if age > 0:
            message = f"👋 Привіт, {name}! Тобі {age} років - це чудово! 🎈"
        else:
            message = f"👋 Привіт, {name}! Радий тебе бачити! 😊"

        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"error": "Помилка сервера"}), 500


@app.route('/api/letters', methods=['POST'])
def count_letters():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Не надіслано даних"}), 400

        word = data.get('word')
        if not word:
            return jsonify({"error": "Не вказано слово"}), 400

        count = len(word)

        if count == 1:
            message = f"🔤 В слові '{word}' всього 1 буква!"
        elif count < 5:
            message = f"🔤 В слові '{word}' {count} букви - коротке слово!"
        elif count < 10:
            message = f"🔤 В слові '{word}' {count} букв - середнє слово!"
        else:
            message = f"🔤 Вау! В слові '{word}' аж {count} букв - довжелезне слово! 🤯"

        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"error": "Помилка сервера"}), 500


if __name__ == '__main__':
    print("🚀 Запускаю дитячий сайт...")

    # Перевіряємо файли перед запуском
    if check_files():
        print("✅ Всі файли на місці!")
        print("🌐 Відкрий: http://localhost:5000")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("❌ Помилка запуску: не всі файли знайдено")