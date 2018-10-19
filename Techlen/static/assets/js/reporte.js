$( document ).ready(function() {
  //$(".loader-box").hide();
  //$(".inputidestu").hide();
  $("#reporte").hide();
  //inicializa los componentes datepicker
  $('#date1').datepicker();
  $('#date2').datepicker();

  $('#date1').attr("disabled", true);
  $('#select').attr("disabled", true);
  $('#selectOne').attr("disabled", true);
  $('#select2').attr("disabled", true);
  $('#select3').attr("disabled", true);
  $('#select4').attr("disabled", true);
  $('#select5').attr("disabled", true);
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

function TipoReport(){
  if( $( "#tipoReporte" ).val()=="0"){
    $('#date1').attr("disabled", true);
    $('#select').attr("disabled", true);
    $('#selectOne').attr("disabled", true);
    $('#select2').attr("disabled", true);
    $('#select3').attr("disabled", true);
    $('#select4').attr("disabled", true);
    $('#select5').attr("disabled", true);
  }else if($( "#tipoReporte" ).val()=="1"){
    $('#date1').attr("disabled", false);
    $('#select').attr("disabled", false);
    $('#selectOne').val("SOLO INCIDENTES")
    $('#selectOne').attr("disabled", true);
    $('#select2').attr("disabled", false);
    $('#select3').attr("disabled", false);
    $('#select4').attr("disabled", false);
    $('#select5').attr("disabled", false);
  }else if($( "#tipoReporte" ).val()=="2"){
    $('#date1').attr("disabled", false);
    $('#select').attr("disabled", false);
    $('#selectOne').val("SI")
    $('#selectOne').attr("disabled", false);
    $('#select2').attr("disabled", false);
    $('#select3').attr("disabled", false);
    $('#select4').attr("disabled", false);
    $('#select5').attr("disabled", false);
  }else{
    $('#date1').attr("disabled", false);
    $('#select').attr("disabled", false);
    $('#selectOne').val("SI")
    $('#selectOne').attr("disabled", false);
    $('#select2').attr("disabled", false);
    $('#select3').attr("disabled", false);
    $('#select4').attr("disabled", false);
    $('#select5').attr("disabled", false);
  }
}

function countRow(){
  var nFilas = $("#detallep tr").length;
  // console.log("n filas "+nFilas)
  return nFilas;
}

//instancia los parametros del reporte
function parameterReport(){
  //instancia el select de programas
  axios.get('/api/programa/')
    .then(function (response) {
    var datos = response.data;
    for(key in datos){
      let option = "<option value="+ datos[key].id+">"+ datos[key].nombre+"</option>";
      $("#select2").append(option);
    }
  }).catch(function (error) {
      //console.log(error);
  });


  //instancia select tipo PERSONA
  axios.get('/api/Persona/tipo/')
    .then(function (response) {
    var datos = response.data;
    for(key in datos){
      let option = "<option value="+ datos[key].id+">"+ datos[key].Tipo_persona+"</option>";
      $("#select3").append(option);
    }
  }).catch(function (error) {
      //console.log(error);
  });


  //instancia el select de tipos de recurso
  axios.get('/api/Recurso/Tipo/')
    .then(function (response) {
    var datos = response.data;
    for(key in datos){
      let option = "<option value="+ datos[key].id_recurso+">"+ datos[key].tipo_recurso+"</option>";
      $("#select4").append(option);
    }
  }).catch(function (error) {
      //console.log(error);
  });

  //instancia el select de tipos de recurso
  axios.get('/api/Recurso/Marca/')
    .then(function (response) {
    var datos = response.data;
    for(key in datos){
      let option = "<option value="+ datos[key].id+">"+ datos[key].Marca+"</option>";
      $("#select5").append(option);
    }
  }).catch(function (error) {
      //console.log(error);
  });
}

//invertir fecha
function convertirfecha(date){
  date = date.split("-");
  var value=new Date(date[2],(date[1]-1),date[0]);
  value.setHours(0,0,0,0);
  fecha = value.getFullYear()+'-'+(value.getMonth()+1)+'-'+value.getDate()
  return fecha
}

//funcion que genera el reporte
function generateReport(){
  var date1 = convertirfecha($('#date1').val())
  var date2 = convertirfecha($('#date2').val())
  if(date1===date2){
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

// instancia la cabezeras del reporte
function instanciarReporte(query){
  $("#encabezado").empty();
  $("#titulotabla").empty();
  $("#cabezaReporte").empty();
  var fecha ="";
  var date1 = convertirfecha($('#date1').val())
  var date2 = convertirfecha($('#date2').val())
  if(date1 == date2){
    fecha = "<b>FECHA: </b>" +date1 + " <br />"
  }else{
    fecha = "<b>FECHA: </b>" +date1 + "<b> HASTA </b> " +date2 +" <br />"
  }

  //instanciar cabeza del reporte
  var encabezado= "<p>"+
    "<b>TIPO REPORTE: </b>" +$('select[name="reporte"] option:selected').text().toUpperCase()  + " <br />"+
    fecha+
    "<b>ESTADO: </b>"+$('select[name="estado"] option:selected').text().toUpperCase() +"<br />"+
    "<b>INCIDENTE: </b>"+ $('select[name="incidente"] option:selected').text().toUpperCase()+"<br />"+
    "<b>DEPENDENCIA: </b>"+ $('select[name="programa"] option:selected').text().toUpperCase()+"<br />"+
    "<b>TIPO PERSONA: </b>"+ $('select[name="cargo"] option:selected').text().toUpperCase()+"<br />"+
    "<b>TIPO RECURSO: </b>"+ $('select[name="recurso"] option:selected').text().toUpperCase()+"<br />"+
    "<b>MARCA: </b>"+ $('select[name="marca"] option:selected').text().toUpperCase()+"<br />"+
    "</p>"
  $("#encabezado" ).append(encabezado);

  //instancia cabezera de la tabla
  if($( "#tipoReporte" ).val()=="1"){
    var titulo = "<i class='fa fa-list-alt' aria-hidden='true'></i> Detalle & Consolidado Incidentes";
    $( "#titulotabla" ).append(titulo);
    var thead = "<tr>"+
      "<th>ID Prestamo</th>"+
      "<th>Persona</th>"+
      "<th>ID Incidente</th>"+
      "<th>Fecha Incidente</th>"+
      "<th>Estado Incidente</th>"+
      "<th>Recurso Incidente</th>"+
      "<th>Tipo Incidente</th>"+
    "</tr>"
      $( "#cabezaReporte" ).append(thead);
  }else if($( "#tipoReporte" ).val()=="2"){
    var titulo = "<i class='fa fa-list-alt' aria-hidden='true'></i> Detalle & Consolidado Prestamos";
    $( "#titulotabla" ).append(titulo);
    var thead = "<tr>"+
      "<th>ID Prestamo</th>"+
      "<th>Persona</th>"+
      "<th>Programa</th>"+
      "<th>Fecha</th>"+
      "<th>Estado</th>"+
      "<th>Total Recursos</th>"+
      "<th>Incidentes</th>"+
    "</tr>"
      $( "#cabezaReporte" ).append(thead);
  }else{
    var titulo = "<i class='fa fa-list-alt' aria-hidden='true'></i> Detalle & Consolidado Recursos";
    $( "#titulotabla" ).append(titulo);
    var thead = "<tr>"+
      "<th>ID Prestamo</th>"+
      "<th>Fecha Prestamo</th>"+
      "<th>ID Recurso</th>"+
      "<th>Nombre</th>"+
      "<th>Referencia</th>"+
      "<th>Estado</th>"+
      "<th>Incidentes</th>"+
    "</tr>"
      $( "#cabezaReporte" ).append(thead);
  }

//instancia cuerpo de tablas
  if($( "#tipoReporte" ).val() =="1" & query.length != 0){
    for(key in query){
      for(j in query[key].detailprestamo){
        if(query[key].detailprestamo[j].Incidentes !=0){
          var row = "<tr class='row1' >" +
            '<td class="field-Id_prestamo">' + query[key].Id_prestamo+ "</td>"+
            "<td>" + query[key].Persona.Nombres + " " +query[key].Persona.Apellidos+ "</td>"+
            "<td>" + query[key].detailprestamo[j].Incidentes[0].Id_Incidente  + "</td>"+
            "<td>" + query[key].detailprestamo[j].Incidentes[0].Fecha_Incidente + "</td>"+
            "<td>" + query[key].detailprestamo[j].Incidentes[0].Estado + "</td>"+
            "<td>" + query[key].detailprestamo[j].Recurso_detalle.nombre_recurso + "</td>"+
            "<td>" + query[key].detailprestamo[j].Incidentes[0].Tipo_Incidente + "</td>"+
            "</tr>";
          $("#detallep").append(row);
        }
      }
    }

    var row =  '<tr class="table-info">'+
        "<td><strong>Total Incidentes: </strong></td>"+
        "<td> </td>"+
        "<td> </td>"+
        "<td> </td>"+
        "<td> </td>"+
        "<td> </td>"+
      "<td>"+(countRow())+"</td>"+
      "</tr>";
    $("#detallep").append(row);
    //tipo de reporte 2
  }else if($( "#tipoReporte" ).val() =="2" & query.length != 0){
    query.sort(function (o1,o2) {
      if (o1.Persona.Dependencia.nombre > o2.Persona.Dependencia.nombre) {
        return 1;
      } else if (o1.Persona.Dependencia.nombre < o2.Persona.Dependencia.nombre) {
        return -1;
      }
      return 0;
    });
    for(key in query){
      var incidente = ""
      for(j in query[key].detailprestamo){
        if(query[key].detailprestamo[j].Incidentes !=0){
          incidente = "SI"
          break;
        }else{
          incidente = "NO"
        }
      }
      var row = "<tr class='row1' >" +
        '<td class="field-Id_prestamo">' + query[key].Id_prestamo+ "</td>"+
        "<td>" + query[key].Persona.Nombres + " " +query[key].Persona.Apellidos+ "</td>"+
        "<td>" + query[key].Persona.Dependencia.nombre + "</td>"+
        "<td>" + query[key].Fecha_prestamo + "</td>"+
        "<td>" + query[key].Estado_prestamo + "</td>"+
        "<td>" + query[key].detailprestamo.length + "</td>"+
        "<td>" + incidente + "</td>"+
        "</tr>";
      $("#detallep").append(row);
    }
    //tipo de reporte 3
    var row =  '<tr class="table-info">'+
        "<td><strong>Total Prestamos: </strong></td>"+
        "<td> </td>"+
        "<td> </td>"+
        "<td> </td>"+
        "<td> </td>"+
        "<td> </td>"+
      "<td>"+(countRow())+"</td>"+
      "</tr>";
    $("#detallep").append(row);
  }else if($( "#tipoReporte" ).val() =="3" & query.length != 0){
    // console.log(query)
    for(key in query){
      //si tipo de recurso es todos
      if($("#select4").val() == "0" ){
        //si marca es difierente a todos
        if($("#select5").val() !="0"){
          if($("#selectOne").val()=="SOLO INCIDENTES"){
            var incidente = ""
            for(j in query[key].detailprestamo){
              if($("#select5").val() == query[key].detailprestamo[j].Recurso_detalle.Marca){
                if(query[key].detailprestamo[j].Incidentes !=0){
                  incidente = "SI"
                  var row = "<tr class='row1' >" +
                    '<td class="field-Id_prestamo">' + query[key].Id_prestamo+ "</td>"+
                    "<td>" + query[key].Fecha_prestamo + "</td>"+
                    "<td>" + query[key].detailprestamo[j].Recurso_detalle.Id_recurso + "</td>"+
                    "<td>" + query[key].detailprestamo[j].Recurso_detalle.nombre_recurso + "</td>"+
                    "<td>" + query[key].detailprestamo[j].Recurso_detalle.referencia + "</td>"+
                    "<td>" + query[key].detailprestamo[j].Recurso_detalle.Estado_Recurso + "</td>"+
                    "<td>" + incidente + "</td>"+
                    "</tr>";
                  $("#detallep").append(row);
                }
              }
            }
          }else{
            var incidente = ""
            for(j in query[key].detailprestamo){
              if($("#select5").val() == query[key].detailprestamo[j].Recurso_detalle.Marca){
                if(query[key].detailprestamo[j].Incidentes !=0){
                  incidente = "SI"
                }else{
                  incidente = "NO"
                }
                var row = "<tr class='row1' >" +
                  '<td class="field-Id_prestamo">' + query[key].Id_prestamo+ "</td>"+
                  "<td>" + query[key].Fecha_prestamo + "</td>"+
                  "<td>" + query[key].detailprestamo[j].Recurso_detalle.Id_recurso + "</td>"+
                  "<td>" + query[key].detailprestamo[j].Recurso_detalle.nombre_recurso + "</td>"+
                  "<td>" + query[key].detailprestamo[j].Recurso_detalle.referencia + "</td>"+
                  "<td>" + query[key].detailprestamo[j].Recurso_detalle.Estado_Recurso + "</td>"+
                  "<td>" + incidente + "</td>"+
                  "</tr>";
                $("#detallep").append(row);
              }
            }
          }
          //si marca es igual a todas regresa todos las marcas y tipos
        }else{
          if($("#selectOne").val()=="SOLO INCIDENTES"){
            var incidente = ""
            for(j in query[key].detailprestamo){
                if(query[key].detailprestamo[j].Incidentes !=0){
                  incidente = "SI"
                  var row = "<tr class='row1' >" +
                    '<td class="field-Id_prestamo">' + query[key].Id_prestamo+ "</td>"+
                    "<td>" + query[key].Fecha_prestamo + "</td>"+
                    "<td>" + query[key].detailprestamo[j].Recurso_detalle.Id_recurso + "</td>"+
                    "<td>" + query[key].detailprestamo[j].Recurso_detalle.nombre_recurso + "</td>"+
                    "<td>" + query[key].detailprestamo[j].Recurso_detalle.referencia + "</td>"+
                    "<td>" + query[key].detailprestamo[j].Recurso_detalle.Estado_Recurso + "</td>"+
                    "<td>" + incidente + "</td>"+
                    "</tr>";
                    $("#detallep").append(row);
                    break;
                }
              }
          }else{
            var incidente = ""
            for(j in query[key].detailprestamo){
              if(query[key].detailprestamo[j].Incidentes !=0){
                incidente = "SI"
              }else{
                incidente = "NO"
              }
              var row = "<tr class='row1' >" +
                '<td class="field-Id_prestamo">' + query[key].Id_prestamo+ "</td>"+
                "<td>" + query[key].Fecha_prestamo + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.Id_recurso + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.nombre_recurso + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.referencia + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.Estado_Recurso + "</td>"+
                "<td>" + incidente + "</td>"+
                "</tr>";
                $("#detallep").append(row);
            }
          }

        }
        //si tipo de recurso  es diferente a todas
      }else{
        if($("#select5").val() !="0"){
          var incidente = ""
          for(j in query[key].detailprestamo){
            if($("#select4").val() == query[key].detailprestamo[j].Recurso_detalle.tipo_de_recurso & $("#select5").val() == query[key].detailprestamo[j].Recurso_detalle.Marca){
              if(query[key].detailprestamo[j].Incidentes !=0){
                incidente = "SI"
              }else{
                incidente = "NO"
              }
              var row = "<tr class='row1' >" +
                '<td class="field-Id_prestamo">' + query[key].Id_prestamo+ "</td>"+
                "<td>" + query[key].Fecha_prestamo + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.Id_recurso + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.nombre_recurso + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.referencia + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.Estado_Recurso + "</td>"+
                "<td>" + incidente + "</td>"+
                "</tr>";
              $("#detallep").append(row);
            }
          }
        }else if($("#selectOne").val()=="SOLO INCIDENTES"){
          var incidente = ""
          for(j in query[key].detailprestamo){
            if($("#select4").val() == query[key].detailprestamo[j].Recurso_detalle.tipo_de_recurso){
              if(query[key].detailprestamo[j].Incidentes !=0){
                incidente = "SI"
                var row = "<tr class='row1' >" +
                  '<td class="field-Id_prestamo">' + query[key].Id_prestamo+ "</td>"+
                  "<td>" + query[key].Fecha_prestamo + "</td>"+
                  "<td>" + query[key].detailprestamo[j].Recurso_detalle.Id_recurso + "</td>"+
                  "<td>" + query[key].detailprestamo[j].Recurso_detalle.nombre_recurso + "</td>"+
                  "<td>" + query[key].detailprestamo[j].Recurso_detalle.referencia + "</td>"+
                  "<td>" + query[key].detailprestamo[j].Recurso_detalle.Estado_Recurso + "</td>"+
                  "<td>" + incidente + "</td>"+
                  "</tr>";
                $("#detallep").append(row);
              }
            }
          }
        }else{
          var incidente = ""
          for(j in query[key].detailprestamo){
            if($("#select4").val() == query[key].detailprestamo[j].Recurso_detalle.tipo_de_recurso){
              if(query[key].detailprestamo[j].Incidentes !=0){
                incidente = "SI"
              }else{
                incidente = "NO"
              }
              var row = "<tr class='row1' >" +
                '<td class="field-Id_prestamo">' + query[key].Id_prestamo+ "</td>"+
                "<td>" + query[key].Fecha_prestamo + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.Id_recurso + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.nombre_recurso + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.referencia + "</td>"+
                "<td>" + query[key].detailprestamo[j].Recurso_detalle.Estado_Recurso + "</td>"+
                "<td>" + incidente + "</td>"+
                "</tr>";
              $("#detallep").append(row);
            }
          }
        }
      }
    }
    var row =  '<tr class="table-info">'+
        "<td><strong>Total Recursos: </strong></td>"+
        "<td> </td>"+
        "<td> </td>"+
        "<td> </td>"+
        "<td> </td>"+
        "<td> </td>"+
      "<td>"+(countRow())+"</td>"+
      "</tr>";
    $("#detallep").append(row);
  // para añadir parametro al detalle reporte
  }else{

  }

}

function report(data){
  $("#detallep").empty();
  var incidentes = filtrarIncidente(data)
  var estados = filtroEstado(incidentes)
  var programa = filtroDependencia(estados)
  var personat = filtroTipoPersona(programa)
  var TipoR = filtroRecursoTipo(personat)
  var query = filtroMarca(TipoR)
  //tipo de reporte 1
  instanciarReporte(query)
  if(query.length == 0){
    alerta()
    connsole.log("hola")
    $("#reporte").hide();
  }else if( (countRow()-1) == 0){
      alerta()
      console.log("hola2")
      $("#reporte").hide();
  }else{
    $("#reporte").show();
    $("#cabecera").hide();
  }
}

function closet(){
  $('#alert').hide();
}

function alerta(){
  console.log("funcion")
  var row = " <div class='alert alert-warning alert-dismissible show' id='alert' role='alert'>"+
      "<strong>SIN RESULTADOS!</strong>...Esta consulta no arrojó resultados, compruebe los campos de filtro."+
      "<button type='button' class='close' onclick='closet()' >"+
        "<span >&times;</span>"+
      "</button>"+
    "</div>"
    $("#msj").prepend(row)

}

function imprimir(){
  window.print()
}

function atras(){
  $("#reporte").hide();
  $("#cabecera").show();
}

//filtro por marca
function filtroMarca(data){
  var query = [];
  var value = $("#select5").val();
  if(value == "0"){
    query = data;
  }else{
    for(key in data){
      for(j in data[key].detailprestamo){
        if(data[key].detailprestamo[j].Recurso_detalle.Marca == value){
          query.push(data[key])
          break;
        }
      }
    }
  }
  return query
}

//filtro por tipo recurso
function filtroRecursoTipo(data){
  var query = [];
  var value = $("#select4").val();
  if(value == "0"){
    query = data;
  }else{
    for(key in data){
      for(j in data[key].detailprestamo){
        if(data[key].detailprestamo[j].Recurso_detalle.tipo_de_recurso == value){
          query.push(data[key])
          break;
        }
      }
    }
  }
  return query
}

//filtro por Tipo_persona
function filtroTipoPersona(data){
  var query = [];
  var value = $("#select3").val();
  if(value == "0"){
    query = data;
  }else{
    for(key in data){
      if(data[key].Persona.Tipo_Persona.id == value){
        query.push(data[key])
      }
    }
  }
  return query
}

//filtro por dependencia
function filtroDependencia(data){
  var query = [];
  var value = $("#select2").val();
  if(value == "0"){
    query = data;
  }else{
    for(key in data){
      if(data[key].Persona.Dependencia.id == value){
        query.push(data[key])
      }
    }
  }
  return query
}

//filtro por estado
function filtroEstado(data){
  var query = [];
  var value = $("#select").val();
  if(value == "0"){
    query = data;
  }else if(value == "1"){
    for(key in data){
      if(data[key].Estado_prestamo == "EN CURSO"){
        query.push(data[key]);
      }
    }
  }else{
    for(key in data){
      if(data[key].Estado_prestamo == "DEVUELTO"){
        query.push(data[key]);
      }
    }
  }
  return query
}

//filro por incidente
function filtrarIncidente(data){
  var query = [];
  var bandera = false;
  var value = $("#selectOne").val();
  if(value == "SI"){
    query = data;
  }else if(value == "NO"){
    for(key in data){
      for(j in data[key].detailprestamo){
        if(data[key].detailprestamo[j].Incidentes != 0){
          bandera = true;
          break;
        }else{
          bandera = false
        }
      }
      if(bandera == false){
        query.push(data[key]);
      }
    }
  }else{
    for(key in data){
      for(j in data[key].detailprestamo){
        if(data[key].detailprestamo[j].Incidentes != 0){
          query.push(data[key]);
          break;
        }
      }
    }
  }
  return query
}
