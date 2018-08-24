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

//invertir fecha
function convertirfecha(date){
  console.log("fecha antes de convertir " + date)
  date = date.split("-");
  var value=new Date(date[2],(date[1]-1),date[0]);
  value.setHours(0,0,0,0);
  fecha = value.getFullYear()+'-'+(value.getMonth()+1)+'-'+value.getDate()
  console.log("fecha despues de convertir " + fecha)
  return fecha
}

function generateReport(){
  var date1 = convertirfecha($('#date1').val())
  var date2 = convertirfecha($('#date2').val())
  if(date1===date2){
    console.log("si son iguales");
    axios.get('/api/Prestamo/?Fecha_prestamo='+date1)
      .then(function (response) {
      var datos = response.data;
      report(datos)
    }).catch(function (error) {
        // console.log(error);
    });
  }else{
    axios.get('/api/Prestamo/?Fecha_0='+date1+'&Fecha_1='+date2)
      .then(function (response) {
      var datos = response.data;
      report(datos)
    }).catch(function (error) {
        // console.log(error);
    });
  }
}

function report(data){
  console.log(data)
}
