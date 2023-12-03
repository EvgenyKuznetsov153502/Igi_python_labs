function showCountdown() {
        let now = new Date().getTime();
        let startTime = localStorage.getItem('countdownStartTime');

        if (!startTime || now - startTime > 3600000) {
            startTime = now;
            localStorage.setItem('countdownStartTime', startTime);
        }

        let remainingTime = 3600000 - (now - startTime);

        updateCountdown(remainingTime);

        setInterval(function() {
            now = new Date().getTime();
            remainingTime = 3600000 - (now - startTime);
            updateCountdown(remainingTime);
        }, 1000);
    }

function updateCountdown(remainingTime) {
    var hours = Math.floor(remainingTime / (1000 * 60 * 60));
    var minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

    document.getElementById('countdown').innerHTML = 'Осталось времени: ' + hours + 'ч ' + minutes + 'м ' + seconds + 'с';
}

showCountdown();