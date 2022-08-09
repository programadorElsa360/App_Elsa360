let cerrar = document.querySelectorAll(".closeModalBorg")[0];
let abrir = document.querySelectorAll(".CTA-ModalBorg")[0];
let modal = document.querySelectorAll(".modalBorg")[0];
let modalC = document.querySelectorAll(".container-modalBorg")[0]; 

abrir.addEventListener("click", function(e){
    e.preventDefault();
    modalC.style.opacity = "1";
    modalC.style.visibility = "visible";
    modal.classList.toggle("modal-closeBorg");
});

cerrar.addEventListener("click", function(){
    modal.classList.toggle("modal-closeBorg");
    setTimeout(function(){
        modalC.style.opacity = "0";
        modalC.style.visibility = "hidden";
    },700);    
});

window.addEventListener("click", function(e){
    console.log(e.target)
    if(e.target == modalC){
        modal.classList.toggle("modal-closeBorg");
        setTimeout(function(){
            modalC.style.opacity = "0";
            modalC.style.visibility = "hidden";
        },700);
    }
}); 