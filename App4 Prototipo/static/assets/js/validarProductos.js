
const add_pName = document.getElementById("add_pName");
const add_pDescription = document.getElementById("add_pDescription");
const add_pPrice = document.getElementById("add_pPrice");
const add_pAmount = document.getElementById("add_pAmount");
const add_pColor = document.getElementById("add_pColor");
const add_form = document.getElementById("add_form");
const error_add_pName = document.getElementById("error_add_pName");
const error_add_pDescription = document.getElementById("error_add_pDescription");
const error_add_pPrice = document.getElementById("error_add_pPrice");
const error_add_pAmount = document.getElementById("error_add_pAmount");


console.log("entró al javascript");
function validarProductos() {
  
  let flag = false;
  let errorN = "";
  let errorD = "";
  let errorP = "";
  let errorA = ""; 

  if (add_pName.value.length == 0 || add_pName.value.length == null) {
    errorN = "Ingrese un nombre<br>";    
    console.log("aqui vamos nombre");
    flag = true;
  } else if (add_pName.value.length <= 2){
      errorN = "Ingrese un nombre mas largo<br>";
      flag = true;
  }

  if (add_pDescription.value.length == 0  || add_pDescription.value == null) {
    errorD = "Ingrese una descripcion <br>";
    flag = true;
  } else if(add_pDescription.value.length <= 5) {
      errorD = "ingrese una descripcion mas larga";
      flag = true;
  } else if(add_pDescription.value.length > 100) {
      errorD = "Ingrese una descripcion mas corta";
      flag = true;
  }

  if(add_pPrice.value.length == 0 || add_pPrice.value == null || add_pPrice.value == 0){
    errorP = "el precio no es valido <br>";    
    console.log("aqui vamos precio");
    flag = true;
  }

  if(isNaN(add_pPrice.value)){ 
    console.log("valor de precio errad0");
    errorP += "el valor no es valido <br>"
    flag = true;
  } else {
      parseFloat(add_pPrice.value)
  }

  if (parseFloat(add_pPrice.value) < 0) {
    console.log("El valor es negativo")
    errorP = "la cantidad no es valida"
    flag = true;
  }

  if (add_pAmount.value == "" || add_pAmount.value == null) {
    errorA = "ingrese una cantidad<br>";
    flag = true;
  } 

  if(isNaN(add_pAmount.value)){
    errorA = "el valor no es valido <br>"
    flag = true;
    } else {
    parseInt(add_pAmount.value)
    }

  if (parseInt(add_pAmount.value) <= 0 || parseInt(add_pAmount.value) > 999) {
      console.log("El valor es negativo")
      errorA = "la cantidad no es valida "
      flag = true;
  }

  if(flag == true){
     error_add_pName.innerHTML =  errorN;
     error_add_pDescription.innerHTML = errorD;
     error_add_pPrice.innerHTML = errorP;
     error_add_pAmount.innerHTML = errorA; 
  } else{
    console.log("Entra a else, Js")
    console.log("antes del submit");    
    document.getElementById("add_form").submit();
    console.log("despues del reload");
    // document.getElementById("add_form").reset();
    errorN = "";
    errorD = "";
    errorP = "";
    errorA = "";
    error_add_pName.innerHTML =  errorN;
    error_add_pDescription.innerHTML = errorD;
    error_add_pPrice.innerHTML = errorP;
    error_add_pAmount.innerHTML = errorA;
       
  }
  
}

id_salvada = 0;

function validarBusqueda(){

  search_pID = document.getElementById("search_pID").value
  console.log("Entro a validarBusqueda()")
  console.log(search_pID.value)
  
  if(isNaN(search_pID) == false && search_pID > 0){ //Valida si es numerico o no numerico
    document.getElementById("error_search_pID").innerHTML = "";
    console.log("La ID es numerica")

    id_salvada = document.getElementById("search_pID");
    document.getElementById("search_form").submit();
    document.getElementById("upgrade_pID").innerHTML = id_salvada;

    if (document.getElementById("error_search_pID").innerHTML.length > 0){ //Valida si existe o no existe
      //aqui entra cuando la ID no existe
      console.log("Python detecto que la email NO existe.")

    } else {
      console.log("Python detecto que la email existe.")
      
    }
    
    
  } else {
    document.getElementById("error_search_pID").innerHTML = "ID invalida.";
    // console.log("NO ES NUMERICA")
  }
}

function validarActualizar(){
  
  flag = false;
  errorN = "";
  errorD = "";
  errorP = "";
  errorA = ""; 
  //upgrades que manda python una vez realizada la busqueda

  
  upgrade_ID = document.getElementById("upgrade_pID");
  upgrade_pName = document.getElementById("upgrade_pName");
  upgrade_pDescription = document.getElementById("upgrade_pDescription");
  upgrade_pPrice = document.getElementById("upgrade_pPrice");
  upgrade_pAmount = document.getElementById("upgrade_pAmount");
  upgrade_form = document.getElementById("upgrade_form");
  error_upgrade_pName = document.getElementById("error_upgrade_pName");
  error_upgrade_pDescription = document.getElementById("error_upgrade_pDescription");
  error_upgrade_pPrice = document.getElementById("error_upgrade_pPrice");
  error_upgrade_pAmount = document.getElementById("error_upgrade_pAmount");

  console.log("Entro a Actualizar");
  console.log(upgrade_pDescription.innerHTML);

  if (upgrade_pName.value.length == 0 || upgrade_pName.value.length == null) {
    errorN = "Ingrese un nombre<br>";    
    console.log("aqui vamos nombre");
    flag = true;
  } else if (upgrade_pName.value.length <= 2){
      errorN = "Ingrese un nombre mas largo<br>";
      flag = true;
  }

  if (upgrade_pDescription.value.length == 0 || upgrade_pDescription.value.length == null) {
      console.log("descripcion")  
      errorD = "Ingrese una descripcion <br>";
      flag = true;
  } else if(upgrade_pDescription.value.length < 5) {
      errorD = "ingrese una descripcion mas larga";
      flag = true;
  } else if(upgrade_pDescription.value.length > 100) {
      errorD = "Ingrese una descripcion mas corta";
      flag = true;
  }

  if(upgrade_pPrice.value.length == 0 || upgrade_pPrice.value == null){
    console.log("precio")
    errorP = "el precio no es valido <br>";    
    console.log("aqui vamos precio");
    flag = true;
  }

  if(isNaN(upgrade_pPrice.value)){ 
    console.log("valor de precio errad0");
    errorP += "el valor no es valido <br>"
    flag = true;
  } else {
      parseFloat(upgrade_pPrice.value)
  }

  if(parseFloat(upgrade_pPrice.value) < 0) {
    console.log("El valor es negativo")
    errorP = "la cantidad no es valida"
    flag = true;
  }

  if(upgrade_pAmount.value == "" || upgrade_pAmount.value == null) {
    errorA = "ingrese una cantidad<br>";
    flag = true;
  } 

  if(isNaN(upgrade_pAmount.value)){
    errorA = "el valor no es valido <br>"
    flag = true;
    } else {
    parseInt(upgrade_pAmount.value)
    }

  if (parseInt(upgrade_pAmount.value)< 0 || parseInt(upgrade_pAmount.value) > 999) {
      console.log("El valor es negativo")
      errorA = "la cantidad no es valida "
      flag = true;
  }



  console.log(flag);
  

  // if(flag == true){
  //   error_upgrade_pName.innerHTML =  errorN;
  //   // console.log("entró al true");
  //   // error_add_pDescription.innerHTML = errorD;
  //   // error_add_pPrice.innerHTML = errorP;
  //   // error_add_pAmount.innerHTML = errorA; 
  // } else{
    
  //   document.getElementById("upgrade_form").submit();
  // //  document.getElementById("upgrade_form").reset();
  //   errorN = "";
  // //  errorD = "";
  // //  errorP = "";
  // //  errorA = "";
  //   error_upgrade_pName.innerHTML =  errorN;
  // //  error_add_pDescription.innerHTML = errorD;
  // //  error_add_pPrice.innerHTML = errorP;
  // //  error_add_pAmount.innerHTML = errorA;
      
  // }


  if(flag == true){
    console.log("entro al true");
     error_upgrade_pName.innerHTML =  errorN;
     error_upgrade_pDescription.innerHTML = errorD;
     error_upgrade_pPrice.innerHTML = errorP;
     error_upgrade_pAmount.innerHTML = errorA; 
  } else{
    console.log("entro al true");
    // document.getElementById("search_pID").value = upgrade_pID;
    document.getElementById("upgrade_form").submit();  
    // window.location.reload(false);
    // document.getElementById("upgrade_form").reset();
    
    console.log(upgrade_ID.value);
    errorN = "";
    errorD = "";
    errorP = "";
    errorA = "";
    // search_pID.innerHTML = "";
    error_upgrade_pName.innerHTML =  errorN;
    error_upgrade_pDescription.innerHTML = errorD;
    error_upgrade_pPrice.innerHTML = errorP;
    error_upgrade_pAmount.innerHTML = errorA;
       
  }
  
    // document.getElementById("error_upgrade_pName").innerHTML = "El Nombre es demasiado corto";

}

function validarDelete(){


  delete_pID = document.getElementById("delete_pID");
  error_search_pID = document.getElementById("error_delete_pID");
  flag=false;
  error = "";
  
  if(isNaN(delete_pID.value)){
    console.log("El ID es no numerico");
    flag=true;
    error = "Ingrese una ID numerica.";

  } else if (delete_pID.value.length == 0 || delete_pID.value.length == null)  {
    console.log("El ID esta vacio");
    flag=true;
    error = "Ingrese una ID.";
    
  }

  if (flag==false){
    console.log("El ID es numerico");
    error_search_pID.innerHTML = "";
    error = "";
    document.getElementById("delete_form").submit()  

  } else {
      error_search_pID.innerHTML = error;     
    }
  }
  
