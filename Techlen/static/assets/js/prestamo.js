 //$(".loader-box").hide();
//$(".inputidestu").hide();


 $(".perfil").hide();


 var cantidad = 0;
   function buscar(ele) {
      if(event.key === 'Enter') {
          console.log(ele.value);
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
                      $("#id").text(user.Nro_Tarjeta);
                      $("#nomb").text(last_name);
                      $("#depe").text(user.Correo_Institucional);
                      $("#sede").text(user.Sede);
                  }else{
                    $("#mensaje").text("Esta Tarjeta Se Encuentra Inactiva...");
                  }
            })
            .catch(function (error) {
                $("#mensaje").text("Persona No Encontrada Reintentar");
                console.log(error);
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

//[1,2,3,4,5]

//for x in arra:

//  r = recurso.get(1)
//  prestamo.recursos.add(r)
//  r.estado = false
function Mensaje(t){
        switch (t) {
            case 1: //
                $(".mensaje-alerta").empty();
                // $(".mensaje-alerta").append(
                //     "<div class='alert alert-success' role='alert'>Se agrego con exito el Prestamo...</div>"
                // );
                dbRecursos=[]
                $(".perfil").hide();
                $(".loader-box").show();
                $(".inputidestu").show();
                $("#tabla").empty();
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

  function buscarp(ele) {
    var html="";
    if(event.key === 'Enter') {
          //console.log(ele.value);
          var codigo = ele.value;
          axios.get('/api/recurso/'+codigo)
            .then(function (response) {
                  var recurso = response.data;
                  if(recurso.Id_recurso !== undefined){
                    if(recurso.Estado_Recurso == "ACTIVO" && dbRecursos.includes( recurso.Id_recurso ) == false){

                      guardarRecursoLocal(recurso.Id_recurso);
                      html+= '<tr class="row1" >' +
                          '<td class="field-Id_prestamo">' + recurso.Id_recurso+ "</td>"+
                          "<td>" + recurso.nombre_recurso + "</td>"+
                          "<td>" + recurso.referencia + "</td>"+
                          "<td>" + recurso.Estado_Recurso + "</td>"+
                          '<td> <button class="btn btn-danger borrar" data-eliminar="' + recurso.Id_recurso + '">Eliminar</button></td>'+
                          //'<td><button class="btn btn-warnig" onclick="modificar('+datos[key].Nombre+','+datos[key].Apellidos+','+datos[key].Edad+')">Modificar</button></td>'
                          "</tr>";
                        $("#tabla").append(html);
                        $(".loader-box").hide();
                        $(".inputidestu").hide();
                        $(".perfil").show();
                      $("#cantidad").text(dbRecursos.legth);
                      if (html != "") {
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
                $("#mensaje").text("Recurso No Encontrado");
                console.log(error);
                Mensaje(4);
            });
          ele.value = "";
      }
  }

  function borrar(){
  	var keyborrar = this.getAttribute("data-eliminar");
    console.log(keyborrar)
    for (key in dbRecursos ){
      if(dbRecursos[key]==keyborrar){
        console.log("borrado: " +dbRecursos[key])
        dbRecursos.splice(key,1)
        Mensaje(7)
      }
    }
    // console.log("despues")
    // console.log(dbRecursos)
    $(document).on('click', '.borrar', function (event) {
    event.preventDefault();
    $(this).closest('tr').remove();
    });
}
