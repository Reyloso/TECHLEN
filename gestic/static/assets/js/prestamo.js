 //$(".loader-box").hide();
//$(".inputidestu").hide();
 $(".perfil").hide();
 var cantidad = 0;
   function buscar(ele) {
      if(event.key === 'Enter') {
          console.log(ele.value);
          var tarjeta = ele.value;
          axios.get('/api/Persona/Detail/'+tarjeta)
            .then(function (response) {
                  var user = response.data;
                  //console.log(user);
                  if(user.Nro_Tarjeta !== undefined){
                      $(".loader-box").hide();
                      $(".inputidestu").hide();
                      $(".perfil").show();
                      var last_name = user.Primer_Nombre + " " + user.Primer_Apellido + " " + user.Segundo_Apellido
                      $("#id").text(user.Nro_Tarjeta);
                      $("#nomb").text(last_name);
                      $("#depe").text(user.Correo_Institucional);
                      $("#sede").text(user.Sede);
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
}

//[1,2,3,4,5]

//for x in arra:

//  r = recurso.get(1)
//  prestamo.recursos.add(r)
//  r.estado = false

function generarJSON(){
  // Seleccionamos los datos de los inputs de formulario

  var datos = {
      "Persona" : $("#id").text(),
      //"Persona" :"123",
      "Recurso": dbRecursos,
      //"Recurso":[1],
      "Fecha_devolucion": $("#FD").val(),
      "Fecha_prestamo": "2018-05-08",//generar
      "Hora_prestamo": "22:07:00",//generar
      "Hora_devolucion": $("#HD").val(),
      "Estado_prestamo": "EN CURSO"//generar
  };
  return datos;
}
function Mensaje(t){
        switch (t) {
            case 1: //
                $(".mensaje-alerta").append(
                    "<div class='alert alert-success' role='alert'>Se agrego con exito el Prestamo</div>"
                );
                break;
            case 2: //
                $(".mensaje-alerta").append(
                    "<div class='alert alert-danger' role='alert'>No se agrego el Prestamo ERROR</div>"
                );
                break;
            default:

        }
    }
  function buscarp(ele) {
    if(event.key === 'Enter') {
          console.log(ele.value);
          var codigo = ele.value;
          axios.get('/api/recurso/'+codigo)
            .then(function (response) {
                  var recurso = response.data;
                  console.log(recurso);
                  if(recurso.Id_recurso !== undefined){
                    var divp = document.getElementById("prod");
                    var divcard = document.createElement("div");
                    var html = "<div class='card border-primary mb-3 ' style='max-width: 18rem;margin-right: 10px;margin-left: 10px;'>"+
                        "<div class='card-header cardprod'>"+ recurso.Id_recurso+"</div>"+
                        "<div class='card-body text-primary'> "+
                        "<h5 class='card-title'>"+recurso.nombre_recurso +"</h5>"+
                        "<p class='card-text'>"+ recurso.tipo_de_recurso+"</br>"+ recurso.fecha_registro+ "</p>"+
                        "</div>";
                    divcard.innerHTML=html;
                    divp.appendChild(divcard);
                      $(".loader-box").hide();
                      $(".inputidestu").hide();
                      $(".perfil").show();
                    cantidad = parseInt($("#cantidad").value) || 0;
                    val = cantidad + 1;
                    $("#cantidad").text(cantidad);
                  }
            })
            .catch(function (error) {
                $("#mensaje").text("Persona No Encontrada Reintentar");
                console.log(error);
            });
          ele.value = "";
      }

  }
