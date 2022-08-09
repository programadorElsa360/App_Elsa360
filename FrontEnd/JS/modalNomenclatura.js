let cerrarM = document.querySelectorAll(".closeModalNomenclatura")[0];
let abrirM = document.querySelectorAll(".CTA-ModalNomenclatura")[0];
let modalN = document.querySelectorAll(".modalNomenclatura")[0];
let modalD = document.querySelectorAll(".container-modalNomenclatura")[0]; 

abrirM.addEventListener("click", function(e){
    e.preventDefault();
    modalD.style.opacity = "1";
    modalD.style.visibility = "visible";
    modalN.classList.toggle("modal-closeNomenclatura");
});

cerrarM.addEventListener("click", function(){
    modalN.classList.toggle("modal-closeNomenclatura");
    setTimeout(function(){
        modalD.style.opacity = "0";
        modalD.style.visibility = "hidden";
    },700);    
});

window.addEventListener("click", function(e){
    console.log(e.target)
    if(e.target == modalD){
        modalN.classList.toggle("modal-closeNomenclatura");
        setTimeout(function(){
            modalD.style.opacity = "0";
            modalD.style.visibility = "hidden";
        },700);
    }
}); 