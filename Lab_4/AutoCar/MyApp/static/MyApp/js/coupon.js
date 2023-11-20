let arrOfProducts = [
    ['Отопление', 100, 'Круглосуточное отопление стоянки (что сохраняет время автовладельцев на прогрев автомобиля)'],
    ['Наблюдение', 150, 'Автоматизированная система наблюдения (т.е. гарантии безопасности автомобиля)'],
    ['Контроль', 423, 'Контроль всех выходов из комплекса автостоянки'],
    ['Парковочное место', 450, 'Предоставление закрытого парковочного места (что дает возможность избежать загрязнения от погодных условий)']
]

let arrOfCoupons = [
    ['10autocar10', 10, 'Скидка 10% при регистрации нового авто'],
    ['3Cars', 20, 'Скидка 20% для тех у кого 3+ авто на нашей стоянке'],
    ['777', 5, 'Скидка 5%. Действует до конца месяца.']
]

let lenOfCoupons = arrOfCoupons.length;
let lenOfProducts = arrOfProducts.length;
let but = document.querySelector("#cal-butt");

class Product {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }

  calculateDiscountedPrice(discountPercentage) {
    const discountAmount = (discountPercentage / 100) * this.price;
    return this.price - discountAmount;
  }
}

class ExtendedProduct extends Product {
  constructor(name, price, description) {
    super(name, price);
    this.description = description;
  }

  getName() {
    return this.name;
  }

  setName(newName) {
    this.name = newName;
  }

  getPrice() {
    return this.price;
  }

  setPrice(newPrice) {
    this.price = newPrice;
  }

  getDescription() {
    return this.description;
  }

  setDescription(newDescription) {
    this.description = newDescription;
  }
}

// дискриптер
function log(classObj, fn) {
    return function () {
        let val = fn.call(classObj);
        alert("Исполнение: " + fn.name);
        return val;
    }
}


function Discount(name, percentage) {
  this.name = name;
  this.percentage = percentage;
}

Discount.prototype.getName = function () {
  return this.name;
};

Discount.prototype.setName = function (newName) {
  this.name = newName;
};

Discount.prototype.getPercentage = function () {
  return this.percentage;
};

Discount.prototype.setPercentage = function (newPercentage) {
  this.percentage = newPercentage;
};

// Дочерний класс
function ExtendedDiscount(name, percentage, description) {
  // Вызывов конструктора родительского класса
  Discount.call(this, name, percentage);
  this.description = description;
}

// Наследование прототипа
ExtendedDiscount.prototype = Object.create(Discount.prototype);

ExtendedDiscount.prototype.getDescription = function () {
  return this.description;
};

ExtendedDiscount.prototype.setDescription = function (newDescription) {
  this.description = newDescription;
};



const product = new ExtendedProduct('Имя', 1000, 'Описание');
//const discountedPrice = product.calculateDiscountedPrice(10);
//console.log(discountedPrice); // Вывод: 1080 (цена с учетом 10% скидки)

let price;
let percent;

function CalcInfo(){
    let productAnswer = document.querySelector('#sel-product');
    let productName = productAnswer.value;
    let setNameProd = document.querySelector('#name-product');
    let setPriceProd = document.querySelector('#price-product');
    let setNameCop = document.querySelector('#name-coupon');
    let setValCop = document.querySelector('#value-coupon');
    let setResult = document.querySelector('#result-price');

    for(let i = 0; i < lenOfProducts; i++){
        if (arrOfProducts[i][0] == productName){
            product.setName(productName);
            price = arrOfProducts[i][1];
            product.setPrice(price);
            product.setDescription(arrOfProducts[i][2]);

            setNameProd.innerHTML = 'Название услуги: ' + product.getName();
            setPriceProd.innerHTML = 'Цена до скидки: ' + product.getPrice();

        }
    }
    // использование декаратора
    //let wrapped = log(product, product.getName);
    //wrapped();

    let couponAnswer = document.querySelector('#sel-coup');
    let couponName = couponAnswer.value;

    const discount = new ExtendedDiscount("Имя", 15, "Описание");
    for(let j = 0; j < lenOfCoupons; j++){
        if (arrOfCoupons[j][0] == couponName){
            discount.setName(couponName);
            percent = arrOfCoupons[j][1];
            discount.setPercentage(percent);
            discount.setDescription(arrOfCoupons[j][2]);
            let res = product.calculateDiscountedPrice(percent);

            setNameCop.innerHTML = 'Название купона: ' + discount.getName();
            setValCop.innerHTML = 'Процент скидки: ' + discount.getPercentage();
            setResult.innerHTML = 'Итоговая стоимость: ' + res;
        }
    }


}