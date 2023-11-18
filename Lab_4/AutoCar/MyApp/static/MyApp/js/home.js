let interval = localStorage.getItem('bannerInterval') || 2000;
let index = 1;
let isBannerChanging = true;

let arrOfImagesAndLinks = [
    ['static/MyApp/images/banner.png','https://mak.by/ru/'],
    ['static/MyApp/images/nike.png','https://www.nike.com/'],
    ['static/MyApp/images/kfc.png','https://www.kfc.by/']
]
let len = arrOfImagesAndLinks.length;

let banner = document.querySelector("#mak img");
let link = document.querySelector('#mak');
let intervalInput = document.querySelector("#intervalInput");

let intervalId = setInterval(changeImage, interval);

function changeImage(){
    if (!isBannerChanging) {
        return;
    }

    index = index % len;

    if (banner && link) {
        banner.setAttribute("src", arrOfImagesAndLinks[index][0]);
        link.setAttribute("href", arrOfImagesAndLinks[index][1]);
        index++;
    }
}

function changeInterval() {
    interval = parseInt(intervalInput.value);
    console.log(interval);
    if (interval <= 0){
        alert("Интервал должен быть положительным");
    }else{
        localStorage.setItem('bannerInterval', interval);
        clearInterval(intervalId);
        intervalId = setInterval(changeImage, interval);
    }
}

// Обработчик события изменения фокуса страницы
function handlePageFocus() {
    isBannerChanging = true;
}

// Обработчик события потери фокуса страницы
function handlePageBlur() {
    isBannerChanging = false;
}

window.addEventListener('focus', handlePageFocus);
window.addEventListener('blur', handlePageBlur);


// Объемные карточки

const cards = document.querySelectorAll(".card-wrapper");

cards.forEach(
card_w => {

  const card = card_w.querySelector(".service");

  card_w.addEventListener('mousemove', event=>{
   const [x, y] = [event.offsetX, event.offsetY];
   const rect = card_w.getBoundingClientRect();
   const [width, height] = [rect.width, rect.height];
   const middleX = width / 2;
   const middleY = height / 2;
   const offsetX = ((x - middleX) / middleX) * 25;
   const offsetY = ((y - middleY) / middleY) * 25;
   const offX = 50 + ((x - middleX) / middleX) * 25;
   const offY = 50 - ((y - middleY) / middleY) * 20;
   card.style.setProperty("--rotateX", 1 * offsetX + "deg");
   card.style.setProperty("--rotateY", -1 * offsetY + "deg");
   card.style.setProperty("--posx", offX + "%");
   card.style.setProperty("--posy", offY + "%");
  });
  card_w.addEventListener('mouseleave', eve=>{

    card.style.animation = 'reset-card 1s ease';
    card.addEventListener("animationend", e=>{
      card.style.animation = 'unset';
      card.style.setProperty("--rotateX", "0deg");
      card.style.setProperty("--rotateY", "0deg");
      card.style.setProperty("--posx", "50%");
      card.style.setProperty("--posy", "50%");
    }, {
      once: true
    });
  });
});