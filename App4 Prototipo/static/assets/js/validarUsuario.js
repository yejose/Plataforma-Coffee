
const add_uName = document.getElementById("add_uName");
const add_uLastname = document.getElementById("add_uLastname");
const add_uEmail = document.getElementById("add_uEmail");
const add_uPhone = document.getElementById("add_uPhone");
const add_uProfile = document.getElementById("add_uProfile");
const add_uPassword = document.getElementById("add_uPassword");
const error_add_uName = document.getElementById("error_add_uName");
const error_add_uLastName = document.getElementById("error_add_uLastname");
const error_add_uEmail = document.getElementById("error_add_uEmail");
const error_add_uPhone = document.getElementById("error_add_uPhone");
const error_add_uProfile = document.getElementById("error_add_uProfile");
const error_add_uPassword = document.getElementById("error_add_uPassword");
const add_form = document.getElementById("add_form");
const email = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;

console.log("entró al javaScript validar usuario")

function validarTexto(parametro){
   var patron = /^[a-zA-Z\s]*$/;
   if(parametro.search(patron)){
     return false;
   } else{
     return true; 
   } 
}


function validarUsuarios() {
    console.log("Entro a validarUsuarios()")
    //REVISAR
    let flag = false;
    let errorN = "";
    let errorL = "";
    let errorE = "";
    let errorPh = "";
    let errorP = "";

    // let tecla = add_uName.value
    // key = tecla.which;
    // tecla = string.fromCharCode(key).toLowerCase();
    // let letras = " áéíóúabcdefghijklmnñopqrstuvwxyz";
    
    // especiales = [8, 37, 39, 46];

    // tecla_especial = false
    // for(var i in especiales) {
    //     if(key == especiales[i]) {
    //         tecla_especial = true;
    //         break;
    //     }
    // }

    // if(!letras.indexOf(tecla)){
    //     flag = true;
    //     errorN = "Ingrese solo letras"
    //     console.log("entro al indexOf")
    // }

    if(add_uName.value.length == 0 || add_uName.value.length == null){
        flag = true;
        errorN = "Ingrese un nombre de usuario <br>"
        console.log ("entró al add_uName");
    } else if(validarTexto(add_uName.value)==false){
        errorN = "Ingrese solo letras <br>";    
        console.log("aqui vamos nuevo metodo validar texto");
        flag = true;
    } else if(add_uName.value.length <= 2){
        flag = true;
        errorN = "Ingrese un Nombre mas largo <br>";
    } else if(add_uName.value.length >=25){
        flag = true; 
        errorN = "ingrese un Nombre mas corto <br>";
    } else if(!isNaN(add_uName.value)){
        flag = true;
        errorN = "ingrese un nombre correcto <br>";
    }

    // add_uNameString = add_uName.value.split("");
    // add_uNameAlert = false;
    // for (let i = 0; i < add_uNameString.length; i++){

    //     console.log(i)
    //     console.log(typeof(i))

    //     if (add_uNameString[i] == '0'){
    //         add_uNameAlert = true;
    //     }
    //     if (add_uNameString[i] == '1'){
    //         add_uNameAlert = true;
    //     }
    //     if (add_uNameString[i] == '2'){
    //         add_uNameAlert = true;
    //     }
    //     if (add_uNameString[i] == '3'){
    //         add_uNameAlert = true;
    //     }
    //     if (add_uNameString[i] == '4'){
    //         add_uNameAlert = true;
    //     }
    //     if (add_uNameString[i] == '5'){
    //         add_uNameAlert = true;
    //     }
    //     if (add_uNameString[i] == '6'){
    //         add_uNameAlert = true;
    //     }
    //     if (add_uNameString[i] == '7'){
    //         add_uNameAlert = true;
    //     }
    //     if (add_uNameString[i] == '8'){
    //         add_uNameAlert = true;
    //     }
    //     if (add_uNameString[i] == '9'){
    //         add_uNameAlert = true;
    //     }
    
    // }

    // console.log(add_uNameString);
    // console.log(add_uNameAlert);

    // if (add_uNameAlert == true){
    //     console.log("Javascript encontro que el Nombre tiene un numero");
    //     errorN = "Ingresa un nombre sin numeros.";
    // }
    // console.log(errorN);

    if(add_uLastname.value.length == 0 || add_uLastname.value.length == null){
        flag = true;
        errorL = "Ingrese un nombre de usuario <br>"
        console.log ("entró al add_uLastame");
    } else if(validarTexto(add_uLastname.value)==false){
        errorN = "Ingrese solo letras <br>";    
        console.log("aqui vamos nuevo metodo validar texto");
        flag = true;
    } else if(add_uLastname.value.length <= 2){
        flag = true;
        errorL = "Ingrese un Nombre mas largo <br>";
    } else if(add_uLastname.value.length >=25){
        flag = true; 
        errorL = "Ingrese un Nombre mas corto <br>";
    } else if(!isNaN(add_uLastname)){
        flag = true;
        errorL = "Ingrese un nombre correcto <br>";
    }

    if(add_uEmail.value.length == 0 || add_uEmail.value.length == null){
        flag = true;
        errorE = "Ingrese un Email <br>"
    } else if (!(email.test(add_uEmail.value))) {
        flag = true;
        errorE = "Ingrese un email valido";
        console.log ("entró al error del email")
    }

    if(add_uPhone.value.length == 0 || add_uPhone.value.length == null){
        flag = true;
        errorPh = "Ingrese un numero de telefono"
    } else if(add_uPhone.value.length > 10 || add_uPhone.value.length < 10){
        flag = true;
        errorPh = "Ingrese un numero de telefono valido"
    } 

    if(isNaN(add_uPhone.value) == true){
        flag = true;
        errorPh = "Ingrese un numero de telefono valido"
    }

    if(add_uPassword.value.length == 0 || add_uPassword.value.length == null){
        flag = true;
        errorP = "Ingrese una contraseña"
    } else if (add_uPassword.value.length > 15 || add_uPassword.value.length < 3){
        flag = true;
        errorP = "Ingrese una contraseña de tamaño adecuado (no mayor que 15 o menor que 3 caracteres)"
    }

    if(flag == true){
        console.log("pasó por aquí en el true")
        error_add_uName.innerHTML = errorN;
        error_add_uLastName.innerHTML = errorL;
        error_add_uEmail.innerHTML = errorE;
        error_add_uPhone.innerHTML = errorPh;
        error_add_uPassword.innerHTML = errorP;
    } else {
        console.log("paso por aqui en el false")
        document.getElementById("add_form").submit();
        console.log(error_add_uEmail.value)
        console.log("se mando el formulario a /users")
        errorN = "";
        errorL = "";
        errorE = "";
        errorPh="";
        errorP = "";
        error_add_uName.innerHTML =  errorN;
        error_add_uLastName.innerHTML = errorL;
        error_add_uEmail.innerHTML = errorE;
        error_add_uPhone.innerHTML = errorPh;
        error_add_uPassword.innerHTML = errorP;

    }
}


let email_salvado = 0;
function validarBusqueda(){

    search_uEmail = document.getElementById("search_uEmail");
    console.log("Entro a validarBusqueda()")
    console.log(document.getElementById("search_uEmail").value)
    error_search_uEmail = document.getElementById("error_search_uEmail");
    flag = false;
    errorE = "";

    if(search_uEmail.value.length == 0 || search_uEmail.value.length == null){
        flag = true;
        errorE = "Ingrese un Email <br>"
        console.log("entró al if del error")
    } else if (!(email.test(search_uEmail.value))) {
        flag = true;
        errorE = "Ingrese un email valido";
        console.log ("entró al error del email") 
    }
    
    if (flag == false){
        errorE = "";
        error_search_uEmail.innerHTML = errorE;
        email_salvado = document.getElementById("search_uEmail");
        document.getElementById("search_form").submit();
        document.getElementById("upgrade_uEmail").innerHTML = email_salvado;
        
    } else if (flag == true){
        error_search_uEmail.innerHTML = errorE;
    }

}
    function validarActualizar(){
  
    flag = false;
    errorN = "";
    errorL = "";
    errorE = "";
    errorPh = "";


    const upgrade_uName = document.getElementById("upgrade_uName");
    const upgrade_uLastname = document.getElementById("upgrade_uLastname");
    const upgrade_uEmail = document.getElementById("upgrade_uEmail");
    const upgrade_uPhone = document.getElementById("upgrade_uPhone");
    const error_upgrade_uName = document.getElementById("error_upgrade_uName");
    const error_upgrade_uLastName = document.getElementById("error_upgrade_uLastname");
    // const error_upgrade_uEmail = document.getElementById("error_upgrade_uEmail");
    const error_upgrade_uPhone = document.getElementById("error_upgrade_uPhone");
    const upgrade_form = document.getElementById("upgrade_form");
    // const email = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;


    if(upgrade_uName.value.length == 0 || upgrade_uName.value.length == null){
        flag = true;
        errorN = "Ingrese un nombre de usuario <br>"
        console.log ("entró al add_uName");
    } else if(upgrade_uName.value.length <= 2){
        flag = true;
        errorN = "Ingrese un Nombre mas largo <br>";
    } else if(upgrade_uName.value.length >=25){
        flag = true; 
        errorN = "ingrese un Nombre mas corto <br>";
    } else if(!isNaN(upgrade_uName.value)){
        flag = true;
        errorN = "ingrese un nombre correcto <br>";
    }

    if(upgrade_uLastname.value.length == 0 || upgrade_uLastname.value.length == null){
        flag = true;
        errorL = "Ingrese un nombre de usuario <br>"
        console.log ("entró al add_uLastame");
    } else if(upgrade_uLastname.value.length <= 2){
        flag = true;
        erroL = "Ingrese un Nombre mas largo <br>";
    } else if(upgrade_uLastname.value.length >=25){
        flag = true; 
        errorL = "Ingrese un Nombre mas corto <br>";
    } else if(!isNaN(upgrade_uLastname)){
        flag = true;
        errorL = "Ingrese un nombre correcto <br>";
    }

    // if(upgrade_uEmail.value.length == 0 || upgrade_uEmail.value.length == null){
    //     flag = true;
    //     errorE = "Ingrese un Email <br>"
    // } else if (!(email.test(add_uEmail.value))) {
    //     flag = true;
    //     errorE = "Ingrese un email valido";
    //     console.log ("entró al error del email")
    // }

    if(upgrade_uPhone.value.length == 0 || upgrade_uPhone.value.length == null){
        console.log("entró al error del telefono")
        flag = true;
        errorPh = "Ingrese un numero  de telefono"
    } else if(upgrade_uPhone.value.length > 10 || upgrade_uPhone.value.length < 10){
        console.log("entró al error del telefono")
        flag = true;
        errorPh = "Ingrese un numero de telefono valido"
    }

    if(flag == true){
        console.log("pasó por aquí en el true")
        error_upgrade_uName.innerHTML = errorN;
        error_upgrade_uLastName.innerHTML = errorL;
        // error_upgrade_uEmail.innerHTML = errorE;
        error_upgrade_uPhone.innerHTML = errorPh;
    } else {
        console.log("paso por aqui en el false")
        document.getElementById("upgrade_form").submit();
        // document.getElementById("upgrade_form").reset();
        window.location.reload(false);
        console.log("se mando el formulario a /users")
        errorN = "";
        errorL = "";
        // errorE = "";
        errorPh="";
        error_upgrade_uName.innerHTML =  errorN;
        error_upgrade_uLastName.innerHTML = errorL;
        // error_upgrade_uEmail.innerHTML = errorE;
        error_upgrade_uPhone.innerHTML = errorPh;
    }

}

function validarEliminar(){
    console.log("ENTRO A ELIMINAR USUARIOS")

    delete_uEmail = document.getElementById("delete_uEmail");
    error_delete_uEmail = document.getElementById("error_delete_uEmail");
    flag = false;
    errorE = "";

    if(delete_uEmail.value.length == 0 || delete_uEmail.value.length == null){
        flag = true;
        errorE = "Ingrese un Email <br>"
        console.log("entró al if del error")
    } else if (!(email.test(delete_uEmail.value))) {
        flag = true;
        errorE = "Ingrese un email valido";
        console.log ("entró al error del email") 
    }

    if(flag==true){
        error_delete_uEmail.innerHTML = errorE;
    }else {
        errorE = "";
        error_delete_uEmail.innerHTML = errorE;
        document.getElementById("delete_form").submit();
    }
}

