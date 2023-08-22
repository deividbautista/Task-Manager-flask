// Obtén todos los labels de los usuarios
const userLabels = document.querySelectorAll(".NombreUsuario");
const idlabel = document.querySelectorAll(".usuariosSeleccionados");
const boton = document.getElementById("boton");
const checkboxes = document.querySelectorAll(".usuariosSelect");
const inputOculto = document.getElementById('inputOculto');

document.addEventListener('DOMContentLoaded', () => {
  // Tu código JavaScript que necesita interactuar con el DOM
  const closeButtons = document.querySelectorAll('.Cerrar');
  closeButtons.forEach(button => {
    button.addEventListener('click', () => {
      console.log("hola");
    });
  });
});

// document.addEventListener('DOMContentLoaded', function() {
//   const btnEliminarAsignacion = document.querySelectorAll('.btnEliminarAsignacion');
//   const nombreU = document.querySelectorAll(".nameU")
//   btnEliminarAsignacion.forEach(button => {
//       button.addEventListener('click', function() {

//           console.log(nombreU.value);
//           // Aquí puedes agregar la lógica para realizar la eliminación con los datos obtenidos
//       });
//   });
// });


// Espera a que el documento esté listo
document.addEventListener("DOMContentLoaded", function () {
  // Selecciona todos los botones con la clase "btnEliminarAsignacion"
  var buttons = document.querySelectorAll(".btnEliminarAsignacion");

  // Agrega un manejador de eventos a cada botón
  buttons.forEach(function (button) {
    button.addEventListener("click", function (event) {
      // Evita el comportamiento por defecto del botón (en este caso, evitará la recarga de la página)
      event.preventDefault();

      // Obtiene los atributos personalizados data-id y data-id-asignado del botón
      var idProceso = button.getAttribute("data-id");
      var idUsuario = button.getAttribute("data-id-asignado");

      // Muestra los datos en la consola
      console.log("ID de Proceso:", idProceso);
      console.log("ID de Usuario asignado:", idUsuario);
    });
  });
});



// Agrega un evento click a cada label.
userLabels.forEach(label => {
  label.addEventListener('click', (event) => {
    // Prevenir que se cierre la lista.
    event.stopPropagation();
  });
});

// Función para obtener la fecha del dia de hoy y asignarla automaticament en el campo de periodo.
window.onload = function () {
  var dateField = document.getElementById("fecha");
  var today = new Date().toISOString().split("T")[0];
  dateField.value = today;
};



