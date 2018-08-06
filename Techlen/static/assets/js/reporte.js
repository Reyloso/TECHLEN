$( document ).ready(function() {
  //$(".loader-box").hide();
  //$(".inputidestu").hide();
  $("#reporte").hide();
  //inicializa los componentes datepicker
  $('#date1').datepicker();
  $('#date2').datepicker();
  //se desactiva segundo datepicker mientras no se introduzca datos en el primero
  $('#date2').attr("disabled", true);
  $('#gReport').attr("disabled", true);

  parameterReport();
});
//validar datepicker
function valid(){
  var val = $('#date1').val()
  var formatdate1 = val.split("-");
  $("#date2").datepicker( "option", "minDate", new Date(formatdate1[2], formatdate1[1]-1, formatdate1[0]));
  if(val ==""){
    $('#date2').attr("disabled", true);
    $('#gReport').attr("disabled", true);
    $('#date2').val(null);
  }else{
    $('#date2').attr("disabled", false);
    $('#gReport').attr("disabled", false);
    var val1 = $('#date2').val()
    if(val1 == ""){
      $( "#date2" ).datepicker( "setDate", new Date(formatdate1[2], formatdate1[1]-1, formatdate1[0]))
    }
  }
}

//funcion validar fecha en rango
function validateDate(dateStart,dateEnd,dateValide){
  valuesStart = dateStart.split("-");
  valuesEnd = dateEnd.split("-");
  valuesValid = dateValide.split("-");
  // Verificamos que la fecha no sea posterior a la actual
  var Start=new Date(valuesStart[2],valuesStart[1]-1,valuesStart[0]);
  var End=new Date(valuesEnd[2],valuesEnd[1]-1,valuesEnd[0]);
  var valid = new Date(valuesValid[0],valuesValid[1]-1,valuesValid[2])
  Start.setHours(0,0,0,0);
  End.setHours(0,0,0,0);
  valid.setHours(0,0,0,0);
  if(valid>=Start && valid <=End){
    console.log("si esta en el rango");
    return 0;
  }else{
    console.log("No esta en el rango");
    return 1;
  }
}

//instancia los parametros del reporte
function parameterReport(){
  //instancia el select de programas
  axios.get('/api/programa/')
    .then(function (response) {
    var datos = response.data;
    for(key in datos){
      let option = "<option value="+ datos[key].nombre+">"+ datos[key].nombre+"</option>";
      $("#select1").append(option);
    }
  }).catch(function (error) {
      //console.log(error);
  });
  //instancia el select de tipos de recurso
  axios.get('/api/Recurso/Tipo/')
    .then(function (response) {
    var datos = response.data;
    for(key in datos){
      let option = "<option value="+ datos[key].tipo_recurso+">"+ datos[key].tipo_recurso+"</option>";
      $("#select3").append(option);
    }
  }).catch(function (error) {
      //console.log(error);
  });
  //instancia el select de tipos de recurso
  axios.get('/api/Recurso/Marca/')
    .then(function (response) {
    var datos = response.data;
    for(key in datos){
      let option = "<option value="+ datos[key].Marca+">"+ datos[key].Marca+"</option>";
      $("#select4").append(option);
    }
  }).catch(function (error) {
      //console.log(error);
  });
}


function generateReport(){
  //condicionales o casos del reporte
  axios.get('/api/Prestamo/')
    .then(function (response) {
    var datos = response.data;
    // console.log(datos)
    for(var key in datos){
      // console.log(datos[key].Fecha_prestamo);
      var dateData = datos[key].Fecha_prestamo;
      // var valueData = new Date(dateData[0],(dateData[1]-1),dateData[2]);
      // console.log(valueData);
      var start = $('#date1').val();
      var end = $('#date2').val();
      validateDate(start,end,dateData)
    }
  }).catch(function (error) {
      //console.log(error);
  });
}
