$( document ).ready(function() {
  //$(".loader-box").hide();
  //$(".inputidestu").hide();
  $(".perfil").hide();
});

 var cantidad = 0;
   function buscar(ele) {
      if(event.key === 'Enter') {
          //console.log(ele.value);
          var tarjeta = ele.value;
          axios.get('/api/Persona/'+tarjeta)
            .then(function (response) {
                  var user = response.data;
                  //console.log(user);
                  if(user.Estado_tarjeta == "ACTIVA"){
                      $(".loader-box").hide();
                      $(".inputidestu").hide();
                      $(".perfil").show();
                      var last_name = user.Primer_Nombre + " " + user.Primer_Apellido + " " + user.Segundo_Apellido
                      $("#tarjeta").text(user.Nro_Tarjeta);
                      $("#id").text(user.Id_Persona);
                      $("#nombre").text(last_name.toUpperCase());
                      $("#tipodoc").text(user.Tipo_Documento);
                      $("#documento").text(user.Nro_Documento);
                      $("#programa").text(user.Programa_Academico.nombre.toUpperCase());
                      $("#cargo").text(user.Correo_Institucional.toUpperCase());
                      if(user.Incidentes.length == 0){
                          $("#incidentes").text("NO");
                      }else{
                        $("#incidentes").text("SI");
                      }
                      $("#cantincidentes").text(user.Incidentes.length)

                  }else{
                    $("#mensaje").text("Esta Tarjeta Se Encuentra Inactiva...");
                  }
            })
            .catch(function (error) {
                $("#mensaje").text("Persona No Encontrada Reintentar");
                //console.log(error);
            });
          ele.value = "";
      }
  }

var dbRecursos = [];

function guardarRecursoLocal(idRecurso){
  dbRecursos.push(idRecurso); // Guardar datos en el array definido globalmente
  // console.log(dbRecursos);
}

function DRecursos (){
  return dbRecursos
}

function Mensaje(t){
        switch (t) {
            case 1: //
                $(".mensaje-alerta").empty();
                console.log("prestamo guardado!!")
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
                  "<div class='alert alert-success' role='alert'>Recurso Borrado de la lista</div>"
                );
                break;
            default:

        }
    }

  function buscarp() {
    var tabla="";
    var ele = $("#add").val()
    if(event.key === 'Enter') {
          $("#add").val("");
          //console.log(ele.value);
          var codigo = ele;
          axios.get('/api/recurso/'+codigo)
            .then(function (response) {
                  var recurso = response.data;
                  if(recurso.Id_recurso !== undefined){
                    if(recurso.Estado_Recurso == "ACTIVO" && dbRecursos.includes( recurso.Id_recurso ) == false){
                      guardarRecursoLocal(recurso.Id_recurso);
                      tabla+= '<li class="list-group-item d-flex justify-content-between lh-condensed">'+
                        '<div>'+
                          '<h6 class="my-0">'+recurso.nombre_recurso+'</h6>'+
                          '<small class="text-muted">'+ "ID: " + recurso.Id_recurso+'</small>'+
                        '</div>'+
                        '<span class="text-muted borrar" data-eliminar="' + recurso.Id_recurso + '"><i class="fa fa-trash"></i></span>'+
                      '</li>'
                      $("#listaRecursos").append(tabla);
                      $("#cantidad").text(dbRecursos.length);
                      if (tabla != "") {
                  			var eliminar = document.getElementsByClassName("borrar");
                  			for(var i = 0; i < eliminar.length; i++){
                  				eliminar[i].addEventListener("click", borrar, false);
                  			}
                  		}
                    }else if (recurso.Estado_Recurso == "ACTIVO" && dbRecursos.includes( recurso.Id_recurso ) == true){
                      Mensaje(6);
                    }else {
                      Mensaje(3);
                    }
                  }else{
                    Mensaje(4);
                  }
            })
            .catch(function (error) {
                Mensaje(4);
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
