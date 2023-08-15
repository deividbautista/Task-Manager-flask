// Obtén todos los labels de los usuarios
const userLabels = document.querySelectorAll(".NombreUsuario");
const idlabel = document.querySelectorAll(".usuariosSeleccionados");
const boton  = document.getElementById("boton");
const checkboxes = document.querySelectorAll(".usuariosSelect");


// Agrega un evento click a cada label.
userLabels.forEach(label => {
  label.addEventListener('click', (event) => {
    // Prevenir que se cierre la lista.
    event.stopPropagation();
  });
});

// Función para obtener la fecha del dia de hoy y asignarla automaticament en el campo de periodo.
window.onload = function() {
  var dateField = document.getElementById("fecha");
  var today = new Date().toISOString().split("T")[0];
  dateField.value = today;
};

