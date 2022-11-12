

function windowScreen(){


const texts = document.querySelectorAll('.animation-text');

for(let i = 0; i < texts.length; i++){
    const text = texts[i];
    const strText = text.textContent;
    const splitText = strText.split('');
    text.textContent = "";

    for(let i = 0; i < splitText.length; i++){
        text.innerHTML += "<span>" + splitText[i] + "</span>";
    }

    let char = 0;
    let timer = setInterval(onTick, 50);

    function onTick(){
        const span = text.querySelectorAll('span')[char];
        span.classList.add('fadee');
        char++;

        if(char === splitText.length){
            complete();
            return;
        }
    }

    function complete(){
        clearInterval(timer);
        timer = null;
    }
}

const elements2 = document.querySelectorAll(".select-div-animation");
for(let i = 0; i < elements2.length; i++){
    const element = elements2[i];
    element.classList.add("fadee2");
}

const elements = document.querySelectorAll(".select-div-animation2");
for(let i = 0; i < elements.length; i++){
    const element = elements[i];
    element.classList.add("fadee3");
}

const elements3 = document.querySelectorAll(".select-div-animation3");
for(let i = 0; i < elements3.length; i++){
    const element = elements3[i];
    element.classList.add("fadee4");
}

const elements4 = document.querySelectorAll(".select-div-animation4");
for(let i = 0; i < elements4.length; i++){
    const element = elements4[i];
    element.classList.add("fadee5");
}

}



window.requestAnimationFrame(windowScreen);