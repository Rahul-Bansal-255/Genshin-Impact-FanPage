function slide_show(){
    if(img_num == img.length - 1){
        img[img_num].style.opacity = "0";
        img[0].style.opacity = "1";
        img_num = 0;
    }
    else{
        img[img_num].style.opacity = "0";
        img[img_num + 1].style.opacity = "1";
        img_num += 1;
    }
}

function slide_show_image(num){
    for(var i = 0; i < img.length; i++){
        if(i == num){
            img[i].style.opacity = "1";
        }
        else{
            img[i].style.opacity = "0";
        }
    }

    img_num = num;
}

var img = document.getElementsByClassName("slide-show-images");
var img_num = 0;
slide_show_image(0);
setInterval(slide_show, 7000);