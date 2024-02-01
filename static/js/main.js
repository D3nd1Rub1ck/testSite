let tg = window.Telegram.WebApp;
tg.expand()

let testButton = document.getElementById("testButton"); 

testButton.addEventListener('click', function(){
    alert("Good bye WebApp Closing")
    tg.close()
});