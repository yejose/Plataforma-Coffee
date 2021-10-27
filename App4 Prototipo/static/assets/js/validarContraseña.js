// const upgrade_uEmail = document.getElementById("upgrade_uEmail")
const upgrade_uName = document.getElementById("upgrade_uName")
const upgrade_uLastname = document.getElementById("upgrade_uLastname")
const upgrade_uPhone = document.getElementById("upgrade_uPhone")
const error_upgrade_uName = document.getElementById("error_upgrade_uName");
const error_upgrade_uLastName = document.getElementById("error_upgrade_uLastname");
const error_upgrade_uEmail = document.getElementById("error_upgrade_uEmail");
const error_upgrade_uPhone = document.getElementById("error_upgrade_uPhone");

const upgrade_uPass = document.getElementById("upgrade_uPass");
const upgrade_uNewpass = document.getElementById("upgrade_uNewpass");
const upgrade_uNewpass2 = document.getElementById("upgrade_uNewpass2");
const error_upgrade_uPass1 = document.getElementById("error_upgrade_uPass1");
const error_upgrade_uNewPass = document.getElementById("error_upgrade_uNewpass");
const error_upgrade_uNewPass2 = document.getElementById("error_upgrade_uNewPass2");

const upgrade_form = document.getElementById("upgrade_form");
const upgrade_form1 = document.getElementById("upgrade_form1");
const email = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;

console.log("entró al javaScript validar profile")

function validarTexto(parametro){
   var patron = /^[a-zA-Z\s]*$/;
   if(parametro.search(patron)){
     return false;
   } else{
     return true; 
   } 
}

function validar_Profile() {
    console.log("Entro a validar")
    //REVISAR
    let flag = false;
    let errorN = "";
    let errorL = "";
    let errorE = "";
    let errorPh = "";

    // if(upgrade_uEmail.value.length == 0 || upgrade_uEmail.value.length == null){
    //     flag = true;
    //     errorE = "Ingrese un Email <br>"
    // } else if (!(email.test(upgrade_uEmail.value))) {
    //     flag = true;
    //     errorE = "Ingrese un email valido";
    //     console.log ("entró al error del email")
    // }

    if(upgrade_uName.value.length == 0 || upgrade_uName.value.length == null){
        flag = true;
        errorN = "Ingrese un nombre de usuario <br>"
    } else if(validarTexto(upgrade_uName.value)==false){
        errorN = "Ingrese solo letras <br>";    
        console.log("aqui vamos nuevo metodo validar texto");
        flag = true;
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
    } else if(validarTexto(upgrade_uLastname.value)==false){
        errorN = "Ingrese solo letras <br>";    
        console.log("aqui vamos nuevo metodo validar texto");
        flag = true;
    } else if(upgrade_uLastname.value.length <= 2){
        flag = true;
        errorL = "Ingrese un Nombre mas largo <br>";
    } else if(upgrade_uLastname.value.length >=25){
        flag = true; 
        errorL = "Ingrese un Nombre mas corto <br>";
    } else if(!isNaN(upgrade_uLastname)){
        flag = true;
        errorL = "Ingrese un nombre correcto <br>";
    }

    if(upgrade_uPhone.value.length == 0 || upgrade_uPhone.value.length == null){
        flag = true;
        errorPh = "Ingrese un numero  de telefono"
    } else if(upgrade_uPhone.value.length > 10 || upgrade_uPhone.value.length < 10){
        flag = true;
        errorPh = "Ingrese un numero de telefono valido"
    } 

    if(isNaN(upgrade_uPhone.value) == true){
        flag = true;
        errorPh = "Ingrese un numero de telefono valido"
    }

    if(flag == true){
        console.log("pasó por aquí en el true")
        error_upgrade_uName.innerHTML = errorN;
        error_upgrade_uLastName.innerHTML = errorL;
        error_upgrade_uEmail.innerHTML = errorE;
        error_upgrade_uPhone.innerHTML = errorPh;
    } else {
        console.log("paso por aqui en el false")
        document.getElementById("upgrade_form").submit();
        console.log(error_upgrade_uEmail.value)
        console.log("se mando el formulario a /users")
        errorN = "";
        errorL = "";
        errorE = "";
        errorPh= "";
        error_upgrade_uName.innerHTML =  errorN;
        error_upgrade_uLastName.innerHTML = errorL;
        error_upgrade_uEmail.innerHTML = errorE;
        error_upgrade_uPhone.innerHTML = errorPh;

    }

}


function validar_NuevaContraseña(){
    console.log("entró a validar nueva contraseña")
    let flag = false;
    let errorP1 = "";
    let errorN1 = "";
    let errorN2 = "";
    
    if(upgrade_uPass.value.length == 0 || upgrade_uPass.value.length == null){
        errorP1 = "ingrese la contraseña"
        flag =  true;
    }

    if(upgrade_uNewpass.value.length == 0 || upgrade_uNewpass.value.length == null){
        errorN1 = "ingrese la nueva contraseña"
        flag =  true;
    }

    if(upgrade_uNewpass2.value.length == 0 || upgrade_uNewpass2.value.length == null){
        errorN2 = "ingrese la  nueva contraseña"
        flag =  true;
    } 
    
    if(!(upgrade_uNewpass.value == upgrade_uNewpass2.value)){
        errorN2 = "las contraseñas no coinciden"
        flag = true;
    }
   
    if(flag == true){
        console.log("pasó por aquí en el true")
        error_upgrade_uPass1.innerHTML = errorP1;
        error_upgrade_uNewPass.innerHTML = errorN1; 
        error_upgrade_uNewPass2.innerHTML = errorN2 
    } else {
        document.getElementById("upgrade_form1").submit();
        let errorP1 = "";
        let errorN1 = "";
        let errorN2 = "";
        error_upgrade_uPass1.innerHTML = errorP1;
        error_upgrade_uNewPass.innerHTML = errorN1; 
        error_upgrade_uNewPass2.innerHTML = errorN2 

    }
}