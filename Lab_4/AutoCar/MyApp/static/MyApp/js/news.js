const newsLeft = document.querySelector('#news_left');
const newsRight = document.querySelector('#news_right');
const text = document.querySelector('#text');

window.addEventListener('scroll',()=>{
    let value = scrollY;
    newsLeft.style.left = `-${value/0.7}px`
    newsRight.style.left = `${value/0.7}px`
    text.style.bottom = `-${value}px`;
})