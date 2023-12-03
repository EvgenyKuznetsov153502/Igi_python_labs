let toys = [];

function addToy(name, cost, ageRange) {
    if(name && cost && ageRange){
        toys.push({
        name: name,
        cost: cost,
        ageRange: ageRange
        });
        displayArrayContent();
    }else{
        alert("Ошибка ввода");
    }
}

function findExpensiveToys() {
    let maxCost = Math.max(...toys.map(toy => toy.cost));

    let expensiveToys = toys.filter(toy => Math.abs(toy.cost - maxCost) <= 1);

    let resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<h3>Наиболее дорогие игрушки:</h3>';

    if (expensiveToys.length > 0) {
        expensiveToys.forEach(toy => {
            resultDiv.innerHTML += `<p>${toy.name} - ${toy.cost} руб., для детей ${toy.ageRange} лет</p>`;
        });
    } else {
        resultDiv.innerHTML += '<p>Нет подходящих игрушек</p>';
    }
}

function displayArrayContent() {
    let arrayContentDiv = document.getElementById('arrayContent');
    arrayContentDiv.innerHTML = '<h3>Содержимое массива:</h3>';

    if (toys.length > 0) {
        toys.forEach((toy, index) => {
            arrayContentDiv.innerHTML += `<p>${index + 1}. ${toy.name} - ${toy.cost} руб., для детей ${toy.ageRange} лет</p>`;
        });
    } else {
        arrayContentDiv.innerHTML += '<p>Массив пуст</p>';
    }
}

function addNewToy() {
    let toyName = document.getElementById('toyName').value;
    let toyCost = parseFloat(document.getElementById('toyCost').value);
    let ageRange = document.getElementById('ageRange').value;

    addToy(toyName, toyCost, ageRange);

    document.getElementById('toyName').value = '';
    document.getElementById('toyCost').value = '';
    document.getElementById('ageRange').value = '';
}

function changeColor() {
    const title = document.getElementById('arr-title');
    title.classList.toggle('pink');
}

