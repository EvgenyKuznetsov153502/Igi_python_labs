function checkAge() {
      let dobInput = document.getElementById('dob');
      let dob = new Date(dobInput.value);
      let currentDate = new Date();

      if(dob == "Invalid Date"){
            alert("Некорректный ввод даты");
            return;
      }

      if(dobInput){
            let age = currentDate.getFullYear() - dob.getFullYear();
            if(currentDate < dob){
                alert("Некорректный ввод даты");
                return;
            }
            if (age >= 18) {
            let daysOfWeek = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота'];
            let dayOfWeek = daysOfWeek[dob.getDay()];
            alert('Вы можете у нас работать т.к. вы совершеннолетний. День недели вашего рождения: ' + dayOfWeek);
            } else {
            alert('Вы несовершеннолетний. Будете работать неофициально (зарплата в конверте)');
            }
      }
}