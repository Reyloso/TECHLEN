$( document ).ready(function() {
  //$(".loader-box").hide();
  //$(".inputidestu").hide();
  $(".perfil").hide();
  // $(".perfil").show();
  var cantidad = 0;
});
   function buscar(ele,e) {
      if(e.keyCode === 13) {
          //console.log(ele.value);
          var tarjeta = ele.value;
          axios.get('/api/Prestamo/?Estado_prestamo=EN+CURSO&Persona__Nro_Tarjeta=' + tarjeta )
          .then(function (response) {
              prestamos =response.data
              if(prestamos.length == 0){
                axios.get('/api/Persona/?Nro_Tarjeta='+tarjeta)
                  .then(function (response) {
                        var user = response.data;
                        if(user[0].Estado_Tarjeta == "ACTIVA"){
                            $(".loader-box").hide();
                            $(".inputidestu").hide();
                            $(".perfil").show();
                            var last_name = user[0].Nombres + " " + user[0].Apellidos
                            $("#tarjeta").text(user[0].Nro_Tarjeta);
                            $("#tarjeta").val(user[0].id);
                            $("#nombre").text(last_name.toUpperCase());
                            $("#cargo").text(user[0].Tipo_Persona.Tipo_persona);
                            $("#documento").text(user[0].Nro_Documento);
                            $("#programa").text(user[0].Dependencia.nombre.toUpperCase());
                            if(user[0].Incidentes.length == 0){
                                $("#incidentes").text("NO");
                            }else{
                              $("#incidentes").text("SI");
                            }
                            $("#cantincidentes").text(user[0].Incidentes.length)

                        }else{
                          $("#mensaje").text("TARJETA INACTIVA...");
                        }
                  })
                  .catch(function (error) {
                      $("#mensaje").text("TARJETA NO ENCONTRADA...");
                      // console.log(error);
                  });
                ele.value = "";
              }else{
                // console.log(prestamos[0].Id_prestamo)
                window.location.replace("/admin/Prestamo/Detalle/"+prestamos[0].Id_prestamo)
              }
          })
          .catch(function (error) {
              $("#mensaje").text("TARJETA NO ENCONTRADA...");
                // console.log(error);
          });
      }
  }
var dbRecursos = [];

function guardarRecursoLocal(idRecurso){
  dbRecursos.push(idRecurso); // Guardar datos en el array definido globalmente
  console.log(dbRecursos);
}

function DRecursos (){
  return dbRecursos
}

function Mensaje(t){
        switch (t) {
            case 1: //
                $(".mensaje-alerta").empty();
                // console.log("prestamo guardado!!")
                dbRecursos=[]
                break;
            case 2: //
                $(".mensaje-alerta").empty();
                $(".mensaje-alerta").append(
                    "<div class='alert alert-danger' role='alert'>No se agrego el Prestamo ERROR</div>"
                );
                break;
            case 3: //
                $(".mensaje-alerta").empty();
                $(".mensaje-alerta").append(
                    "<div class='alert alert-danger' role='alert'>¡Este Recurso está en un prestamo actualmente!</div>"
                );
                break;
            case 4: //
                $(".mensaje-alerta").empty();
                $(".mensaje-alerta").append(
                    "<div class='alert alert-danger' role='alert'>¡Este Recurso No Existe!</div>"
                );
                break;
            case 5: //
                $(".mensaje-alerta").empty();
                $(".mensaje-alerta").append(
                    "<div class='alert alert-success' role='alert'>Recurso añadido correntamente...</div>"
                );
                break;
            case 6: //
                $(".mensaje-alerta").empty();
                $(".mensaje-alerta").append(
                  "<div class='alert alert-danger' role='alert'>Este recurso ya se encuentra en la lista.</div>"
                );
                break;
            case 7: //
                $(".mensaje-alerta").empty();
                $(".mensaje-alerta").append(
                  "<div class='alert alert-success' role='alert'>Recurso borrado de la lista</div>"
                );
                break;
            case 8: //
                $(".mensaje-alerta").empty();
                $(".mensaje-alerta").append(
                  "<div class='alert alert-danger' role='alert'>Recurso está en revisión por incidente</div>"
                );
                break;
            case 9: //
                $(".mensaje-alerta").empty();
                $(".mensaje-alerta").append(
                  "<div class='alert alert-danger' role='alert'>Recurso fue dado de baja por el administrador</div>"
                );
                break;
            case 10: //
                $(".mensaje-alerta").empty();
                $(".mensaje-alerta").append(
                  "<div class='alert alert-danger' role='alert'>No ha agregado recursos a este prestamo</div>"
                );
                break;
            default:

        }
    }



  function buscarp(ele,e) {
    var tabla="";
    console.log("hola")
    if(e.keyCode === 13) {
      var codigo = ele.value;
      console.log(codigo)
      axios.get('/api/recurso/' + codigo)
        .then(function (response) {
            var recurso = response.data;
            console.log(recurso)
            axios.get('/api/Prestamo/?Estado_prestamo=EN+CURSO')
              .then(function (response) {
                var prestamos = response.data
                console.log(prestamos)
                var bandera=false
                for(data in prestamos){
                  for(detalles in prestamos[data].detailprestamo){
                    //console.log(prestamos[data].detailprestamo[detalles].Recurso_detalle.Id_recurso)
                    if(prestamos[data].detailprestamo[detalles].Recurso_detalle.id == recurso.id && prestamos[data].detailprestamo[detalles].Estado !== "DEVUELTO" ){
                      //console.log(prestamos[data].detailprestamo[detalles].Recurso_detalle.Id_recurso)
                      bandera=true
                      break;
                    }
                  }
                  if(bandera==true){
                    break;
                  }
                }
                console.log(bandera)
                if(recurso.Estado_Recurso == "ACTIVO" && dbRecursos.includes( recurso.id ) == false && bandera == false ){
                  guardarRecursoLocal(recurso.id);
                  tabla+= '<li class="list-group-item d-flex justify-content-between lh-condensed">'+
                    '<div>'+
                    '<h6 class="my-0"> ' +recurso.nombre_recurso+'</h6>'+
                    '<small class="text-muted">'+ "ID: " + recurso.id+'</small>'+
                    '<br>'+
                    '<small class="text-muted">'+ "Referencia: " + recurso.referencia+'</small>'+
                    '</div>'+
                    '<span class="text-muted borrar" data-eliminar="' + recurso.id + '"><i class="fa fa-trash"></i></span>'+
                    '</li>'
                  $("#listaRecursos").append(tabla);
                  $("#cantidad").text(dbRecursos.length);
                  if (tabla != "") {
                    var eliminar = document.getElementsByClassName("borrar");
                    for(var i = 0; i < eliminar.length; i++){
                      eliminar[i].addEventListener("click", borrar, false);
                    }
                  }
                }else if (recurso.Estado_Recurso == "ACTIVO" && dbRecursos.includes( recurso.id ) == true){
                  Mensaje(6);
                }else if(recurso.Estado_Recurso == "EN MANTENIMIENTO"){
                  Mensaje(8);
                }else if(recurso.Estado_Recurso == "DADO DE BAJA POR DAÑO TOTAL"){
                  Mensaje(9);
                }else{
                  Mensaje(3);
                }
              })
              .catch(function (error) {
                // console.log(error);
              });
           })
          .catch(function (error) {
            Mensaje(4);
              // console.log(error)
          });
      ele.value = "";
    }
  }

  function borrar(){
  	var keyborrar = this.getAttribute("data-eliminar");
    //console.log(keyborrar)
    for (key in dbRecursos ){
      if(dbRecursos[key]==keyborrar){
        //console.log("borrado: " +dbRecursos[key])
        dbRecursos.splice(key,1)
        Mensaje(7)
      }
    }
    $("#cantidad").text(dbRecursos.length);

    $(document).on('click', '.borrar', function (event) {
      event.preventDefault();
      $(this).closest('li').remove();
    });
}
