const add_cComment = document.getElementById("add_cComment");
const error_add_cComment = document.getElementById("error_add_cComment");
const upgrade_cComment = document.getElementById("upgrade_cComment");
const error_upgrade_pDescription = document.getElementById("error_upgrade_pDescription");

function validarComentario(){
    console.log("Entro a validar comentario");
    console.log(add_cComment.value);
    errorC = "";
    flag = false;


    if (add_cComment.value.length == 0 || add_cComment.value.length == null){
        console.log("COMENTARIO ESTABA VACIO")
        errorC = "No ingrese comentarios vacios.";
        flag = true;
    }

    if (flag == true){
        console.log("flag detecto errores");
        error_add_cComment.innerHTML = errorC;
    }
    else if (flag == false){
        console.log("flag no detecto errores e hizo el submit")
        errorC = "";
        error_add_cComment.innerHTML = "";
        document.getElementById("addComment_form").submit();
    }
}

function validar_actualizar(){
    console.log("Entro a validar comentario");
    console.log(upgrade_cComment.value);
    errorCa = "";
    flag = false;

    if (upgrade_cComment.value.length == 0 || upgrade_cComment.value.length == null){
        console.log("COMENTARIO ESTABA VACIO")
        errorCa = "No ingrese comentarios vacios.";
        flag = true;
    }
    if(upgrade_cComment.value.length > 100){
        console.log("comentario muy largo...")
        flag = true;
    }

    if (flag == true){
        console.log("flag detecto errores");
        error_upgrade_pDescription.innerHTML = errorCa;
    }
    else if (flag == false){
        console.log("flag no detecto errores e hizo el submit")
        errorCa = "";
        error_upgrade_pDescription.innerHTML = "";
        document.getElementById("upgrade_form").submit();
    }

}