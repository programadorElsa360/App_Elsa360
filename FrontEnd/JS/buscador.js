var consulta = $("#searchTable").DataTable();

$("#inputBusqueda").keyup(function(){
	consulta.search($(this).val()).draw();

	$("header").css({
		"height": "100vh",
		"background": "rgba(0,0,0,0.5)"
	})

	if ($("#inputBusqueda").val() == ""){
		$("header").css({
			"height": "auto",
			"background": "none"
		})

		$("#search").hide()

	} else {
		$("#search").fadeIn("fast");
	}
})






document.addEventListener("keyup", e=>{

    if (e.target.matches("#buscador")){
  
        if (e.key ==="Escape")e.target.value = ""
  
        document.querySelectorAll(".alimentoLink").forEach(alimentoN =>{
  
            alimentoN.textContent.toLowerCase().includes(e.target.value.toLowerCase())
              ?alimentoN.classList.remove("filtro")
              :alimentoN.classList.add("filtro")
        })
  
    }
  
  
  })