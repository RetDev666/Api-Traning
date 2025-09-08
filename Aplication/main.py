import os.path

from flask import Flask, request, jsonify, render_template
import random

from werkzeug.utils import send_from_directory

app = Flask(__name__,
            template_folder='../Web Site/HTML',    # Виправлено: без коми
            static_folder='../Web Site')           # Шлях до статичних даних

# Дані
animals = ["🐱 Кіт", "🐶 Собака", "🐸 Жаба", "🐰 Заєць", "🦊 Лисиця"]
colors = ["червоний", "синій", "зелений", "жовтий", "рожевий"]
jokes = [
    "Чому комп'ютер пішов до лікаря? Бо в нього був вірус! 💻",
    "Що каже сир на фото? Молоко! 🧀",
    "Чому риба не грає теніс? Боїться сітки! 🐟"
]

def check_files():
    template_path = os.path.join(os.path.dirname(__file__), '../Web Site/HTML')
    static_path = os.path.join(os.path.dirname(__file__), '../Web Site/CSS')
    if not os.path.exists(template_path, static_path):
        print(f"❌ ПОМИЛКА: Файл index.html або style.css не знайдено за шляхом: {template_path}")
        print("📁 Переконайтеся, що структура папок правильна:")
        print("   Web Site/")
        print("   ├── HTML/")
        print("   │   └── index.html")
        print("   ├── CSS/")
        print("   │   └── style.css")
        print("   └── JS/")
        return False
    return True
# Головна сторінка
@app.route('/')
def home():
    return render_template('index.html')

# Маршрутищатори для статичних файлів
@app.route('/CSS/<path:filename>')
def css_files(filename):
    return send_from_directory('../Web Site/CSS', filename)

@app.route('/JS/<path:filename>')
def js_files(filename):
    return send_from_directory('../Web Site/JS', filename)

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
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({
        "message": f"🧮 {num1} + {num2} = {result} ✨"
    })


@app.route('/api/greeting', methods=['POST'])
def greeting():
    data = request.json
    name = data['name']
    age = data.get('age', 0)

    if age > 0:
        message = f"👋 Привіт, {name}! Тобі {age} років - це чудово! 🎈"
    else:
        message = f"👋 Привіт, {name}! Радий тебе бачити! 😊"

    return jsonify({"message": message})


@app.route('/api/letters', methods=['POST'])
def count_letters():
    data = request.json
    word = data['word']
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


if __name__ == '__main__':
    print("🚀 Запускаю дитячий сайт...")
    print("🌐 Відкрий: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)