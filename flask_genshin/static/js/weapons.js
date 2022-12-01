"use strict";
function show_weapons(id_num){
    for (let i = 1; i <= 5; i++) {
        if(i != Number(id_num)){
            document.getElementById('cards-' + String(i)).style.display = "none";
        }
        else{
            document.getElementById('cards-' + String(i)).style.display = "flex";
        }
    }
}

function toggle_class(css_class, class_to_be_toggle) {
    var ele = document.getElementsByClassName(css_class);
    for (let i = 0; i < ele.length; i++) {
        ele[i].classList.toggle(class_to_be_toggle);
    }
}

show_weapons('1');