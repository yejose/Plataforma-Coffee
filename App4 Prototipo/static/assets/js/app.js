$(document).ready(function(){
  $("#filtro_producto").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#filtro_producto").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});