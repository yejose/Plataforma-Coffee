const add_bAddress = document.getElementById("add_bAddress");
const error_add_bAddress = document.getElementById("error_add_bAddress");

function validarDireccion(){

    errorD = "";
    flag = false;

    if (add_bAddress.value.length == null || add_bAddress.value.length == 0){
        errorD = "Ingrese una direccion porfavor";
        flag = true;
    }

    if (add_bAddress.value.length < 9){
        errorD = "Ingrese una direccion valida";
        flag = true;
    }

    if (flag == true){
        error_add_bAddress.innerHTML = errorD;
    } else if (flag == false){
        errorD = "";
        error_add_bAddress.innerHTML = errorD;
        document.getElementById("address_form").submit();
    }
}