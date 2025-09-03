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
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>🌈 Дитячий API</title>
    <style>
        body {
            font-family: Comic Sans MS, cursive;
            background: linear-gradient(45deg, #ff9a9e, #fecfef, #fecfef);
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        h1 { text-align: center; color: #ff6b6b; font-size: 2.5em; }
        .section {
            background: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            border: 3px solid #ff6b6b;
        }
        input, button {
            padding: 12px;
            border: 2px solid #ff6b6b;
            border-radius: 10px;
            font-size: 16px;
            margin: 5px;
        }
        input { width: 200px; }
        button {
            background: #ff6b6b;
            color: white;
            cursor: pointer;
            border: none;
            font-weight: bold;
        }
        button:hover { background: #ff5252; }
        .result {
            background: #e8f5e8;
            border: 2px solid #4caf50;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌈 Веселий API для Дітей🎈</h1>

        <div class="section">
            <h3>🎲 Випадкові речі</h3>
            <button onclick="getRandomAnimal()">Випадкова тварина</button>
            <button onclick="getRandomColor()">Випадковий колір</button>
            <button onclick="getJoke()">Смішний жарт</button>
            <div id="random-result" class="result" style="display:none;"></div>
        </div>

        <div class="section">
            <h3>🧮 Калькулятор</h3>
            <input type="number" id="num1" placeholder="Перше число">
            <input type="number" id="num2" placeholder="Друге число">
            <button onclick="calculate()">Порахувати</button>
            <div id="calc-result" class="result" style="display:none;"></div>
        </div>

        <div class="section">
            <h3>👋 Привітання</h3>
            <input type="text" id="name" placeholder="Твоє ім'я">
            <input type="number" id="age" placeholder="Твій вік">
            <button onclick="getGreeting()">Привітати</button>
            <div id="greeting-result" class="result" style="display:none;"></div>
        </div>

        <div class="section">
            <h3>🔤 Лічильник букв</h3>
            <input type="text" id="word" placeholder="Напиши слово">
            <button onclick="countLetters()">Порахувати букви</button>
            <div id="letters-result" class="result" style="display:none;"></div>
        </div>
    </div>

    <script>
        function getRandomAnimal() {
            fetch('/api/animal')
                .then(response => response.json())
                .then(data => showResult('random-result', data.message));
        }

        function getRandomColor() {
            fetch('/api/color')
                .then(response => response.json())
                .then(data => showResult('random-result', data.message));
        }

        function getJoke() {
            fetch('/api/joke')
                .then(response => response.json())
                .then(data => showResult('random-result', data.message));
        }

        function calculate() {
            const num1 = document.getElementById('num1').value;
            const num2 = document.getElementById('num2').value;

            if (!num1 || !num2) {
                showResult('calc-result', '❌ Введи обидва числа!');
                return;
            }

            fetch('/api/calculate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({num1: parseInt(num1), num2: parseInt(num2)})
            })
            .then(response => response.json())
            .then(data => showResult('calc-result', data.message));
        }

        function getGreeting() {
            const name = document.getElementById('name').value;
            const age = document.getElementById('age').value;

            if (!name) {
                showResult('greeting-result', '❌ Напиши своє ім\'я!');
                return;
            }

            fetch('/api/greeting', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name: name, age: age ? parseInt(age) : 0})
            })
            .then(response => response.json())
            .then(data => showResult('greeting-result', data.message));
        }

        function countLetters() {
            const word = document.getElementById('word').value;

            if (!word) {
                showResult('letters-result', '❌ Напиши якесь слово!');
                return;
            }

            fetch('/api/letters', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({word: word})
            })
            .then(response => response.json())
            .then(data => showResult('letters-result', data.message));
        }

        function showResult(elementId, message) {
            const element = document.getElementById(elementId);
            element.innerHTML = message;
            element.style.display = 'block';
        }
    </script>
</body>
</html>
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