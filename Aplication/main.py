from flask import Flask, render_template_string, request, jsonify
import random

app = Flask(__name__)

# Дані
animals = ["🐱 Кіт", "🐶 Собака", "🐸 Жаба", "🐰 Заєць", "🦊 Лисиця"]
colors = ["червоний", "синій", "зелений", "жовтий", "рожевий"]
jokes = [
    "Чому комп'ютер пішов до лікаря? Бо в нього був вірус! 💻",
    "Що каже сир на фото? Молоко! 🧀",
    "Чому риба не грає теніс? Боїться сітки! 🐟"
]

# HTML шаблон
HTML = '''

'''


# Головна сторінка
@app.route('/')
def home():
    return render_template_string(HTML)


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