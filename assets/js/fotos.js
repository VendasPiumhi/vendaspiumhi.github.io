function change_bg_to_img(class_name,img_url){
    document.getElementsByClassName(class_name)[0].style.backgroundImage = `url("${img_url}")`;

}