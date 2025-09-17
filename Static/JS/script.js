// Функції для роботи з API

function getRandomAnimal() {
    fetch('/api/animal')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => showResult('random-result', data.message))
        .catch(error => showResult('random-result', '❌ Помилка: ' + error.message));
}

function getRandomColor() {
    fetch('/api/color')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => showResult('random-result', data.message))
        .catch(error => showResult('random-result', '❌ Помилка: ' + error.message));
}

function getJoke() {
    fetch('/api/joke')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => showResult('random-result', data.message))
        .catch(error => showResult('random-result', '❌ Помилка: ' + error.message));
}

function calculate() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;

    if (!num1 || !num2) {
        showResult('calc-result', '❌ Введи обидва числа!');
        return;
    }

    // Перевіряємо, чи є числа дійсно числами
    const number1 = parseInt(num1);
    const number2 = parseInt(num2);
    
    if (isNaN(number1) || isNaN(number2)) {
        showResult('calc-result', '❌ Введи правильні числа!');
        return;
    }

    fetch('/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            num1: number1, 
            num2: number2
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            showResult('calc-result', '❌ ' + data.error);
        } else {
            showResult('calc-result', data.message);
        }
    })
    .catch(error => showResult('calc-result', '❌ Помилка: ' + error.message));
}

function getGreeting() {
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;

    if (!name || name.trim() === '') {
        showResult('greeting-result', '❌ Напиши своє ім\'я!');
        return;
    }

    const requestData = {
        name: name.trim()
    };

    // Додаємо вік тільки якщо він введений і є числом
    if (age && !isNaN(parseInt(age))) {
        requestData.age = parseInt(age);
    }

    fetch('/api/greeting', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            showResult('greeting-result', '❌ ' + data.error);
        } else {
            showResult('greeting-result', data.message);
        }
    })
    .catch(error => showResult('greeting-result', '❌ Помилка: ' + error.message));
}

function countLetters() {
    const word = document.getElementById('word').value;

    if (!word || word.trim() === '') {
        showResult('letters-result', '❌ Напиши якесь слово!');
        return;
    }

    fetch('/api/letters', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            word: word.trim()
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            showResult('letters-result', '❌ ' + data.error);
        } else {
            showResult('letters-result', data.message);
        }
    })
    .catch(error => showResult('letters-result', '❌ Помилка: ' + error.message));
}

function showResult(elementId, message) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = message;
        element.style.display = 'block';
        
        // Додаємо анімацію появи
        element.style.opacity = '0';
        setTimeout(() => {
            element.style.opacity = '1';
        }, 100);
    } else {
        console.error('Елемент з ID ' + elementId + ' не знайдено!');
    }
}

// Додаємо обробники подій для натискання Enter
document.addEventListener('DOMContentLoaded', function() {
    // Калькулятор
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    if (num1Input && num2Input) {
        [num1Input, num2Input].forEach(input => {
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    calculate();
                }
            });
        });
    }

    // Привітання
    const nameInput = document.getElementById('name');
    const ageInput = document.getElementById('age');
    if (nameInput && ageInput) {
        [nameInput, ageInput].forEach(input => {
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    getGreeting();
                }
            });
        });
    }

    // Лічильник букв
    const wordInput = document.getElementById('word');
    if (wordInput) {
        wordInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                countLetters();
            }
        });
    }
});