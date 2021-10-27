let search_cID = document.getElementById("search_cID");
let error_search_cID = document.getElementById("error_search_cID");

function validar_busqueda(){

    console.log("ENTRO A VALIDAR_BUSQUEDA")
    errorB = "";
    flag = false;

    if (search_cID.value == 0 || search_cID.value == null){
        errorB = "Ingresa una ID.";
        flag = true;
    }

    if (isNaN(search_cID.value)==true){
        errorB = "No ingreses caracteres.";
        flag = true;
    }

    console.log(flag)

    if (flag == true){
        error_search_cID.innerHTML = errorB;

    } else if (flag == false){
        errorB = "";
        error_search_cID.innerHTML = errorB;
        document.getElementById("search_form").submit()
    }
}

function validar_eliminar(){

    let delete_cID = document.getElementById("delete_cID");
    let error_delete_cID = document.getElementById("error_delete_cID")
    
    console.log("ENTRO A VALIDAR_BUSQUEDA")
    errorD = "";
    flag = false;

    if (delete_cID.value == 0 || delete_cID.value == null){
        errorD = "Ingresa una ID.";
        flag = true;
    }

    if (isNaN(delete_cID.value)==true){
        errorD = "No ingreses caracteres.";
        flag = true;
    }

    console.log(flag)

    if (flag == true){
        error_delete_cID.innerHTML = errorD;

    } else if (flag == false){
        errorD = "";
        error_delete_cID.innerHTML = errorD;
        document.getElementById("delete_form").submit()
        
    }
}