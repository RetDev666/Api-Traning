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