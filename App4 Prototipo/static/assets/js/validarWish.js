const delete_form = document.getElementById("delete_form");
const error_delete_pID = document.getElementById("error_delete_pID");
const delete_pID = document.getElementById("delete_pID");

function validarBusqueda(){

    console.log("Entro a validarBusqueda()")
    flag = false;
    errorD = "";

    if(delete_pID.value.length == 0 || delete_pID.value.length == null){
        flag = true;
        errorD = "Ingrese un ID <br>"
        console.log("entró al if del error")
    } else if (isNaN(delete_pID.value)==true) {
        flag = true;
        errorD = "Ingrese un ID valido";
        console.log ("entró al error del id") 
    }
    
    if (flag == false){
        errorD = "";
        error_delete_pID.innerHTML = errorD;
        document.getElementById("delete_form").submit();
        
    } else if (flag == true){
        error_delete_pID.innerHTML = errorD;
    }

}