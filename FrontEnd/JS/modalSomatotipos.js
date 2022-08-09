let cerrar = document.querySelectorAll(".closeModalSomatotipos")[0];
let abrir = document.querySelectorAll(".CTA-Modal")[0];
let modal = document.querySelectorAll(".modal")[0];
let modalC = document.querySelectorAll(".container-modal")[0]; 

abrir.addEventListener("click", function(e){
    e.preventDefault();
    modalC.style.opacity = "1";
    modalC.style.visibility = "visible";
    modal.classList.toggle("modal-close");
});

cerrar.addEventListener("click", function(){
    modal.classList.toggle("modal-close");
    setTimeout(function(){
        modalC.style.opacity = "0";
        modalC.style.visibility = "hidden";
    },700);    
});

window.addEventListener("click", function(e){
    console.log(e.target)
    if(e.target == modalC){
        modal.classList.toggle("modal-close");
        setTimeout(function(){
            modalC.style.opacity = "0";
            modalC.style.visibility = "hidden";
        },700);
    }
}); 