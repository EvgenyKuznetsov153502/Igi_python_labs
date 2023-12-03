const form = document.querySelector("#settings");
const body = document.querySelector("#review-main");
const blocks = document.querySelectorAll(".review-arct");
const blockSettings = document.querySelector("#settings");

form.addEventListener('change', function(event) {
    if(form && body){

        if (event.target.matches('.font-size-radio')) {
        const selectedSize = event.target.value;
        body.classList.remove('small-text', 'medium-text', 'large-text');
        body.classList.add(selectedSize + '-text');
        }

        if (event.target.matches('#bgColorCheckbox')) {
            if(event.target.checked){
                body.classList.remove('light-mode');
                body.classList.add('dark-mode');
                blocks.forEach(block => {
                    block.style.backgroundColor = "#501F3A";
                });
                blockSettings.style.backgroundColor = "#501F3A";
            }else{
                body.classList.remove('dark-mode');
                body.classList.add('light-mode');
                blocks.forEach(block => {
                    block.style.backgroundColor = "#d6b7c1";
                });
                blockSettings.style.backgroundColor = "#d6b7c1";
            }
        }
    }
});