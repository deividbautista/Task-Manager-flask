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

document.addEventListener("DOMContentLoaded", function () {
  // Obtiene todos los botones de clase "btnEliminarAsignacion"
  var buttons = document.querySelectorAll(".btnEliminarAsignacion");

  // Agrega un controlador de eventos a cada botón
  buttons.forEach(function (button) {
    button.addEventListener("click", function (event) {

      event.preventDefault(); // Previene la acción por defecto del botón
      // Obtiene los atributos "data"
      var idProceso = button.getAttribute("data-id");
      var idAsignado = button.getAttribute("data-id-asignado");

      // Crea un objeto de datos a enviar en la solicitud
      var data = {
        id_proceso: idProceso,
        id_asignado: idAsignado
      };

      // Urilizamos la variable swal, la cual nos determinara los valores o caracteristicas 
      // del alert que estamos exponiendo al usuario
      Swal.fire({
        title: '¿Estás seguro?',
        text: 'Esta acción eliminará la asignación de forma permanente.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar',
        customClass: {
          // confirmButtonColor: '#900C3F',
          // cancelButtonColor: '#33415c',
          // confirmButtonText: 'Sí, eliminar',
          // cancelButtonText: 'Cancelar'
          confirmButton: 'custom-button-confirmation-1',
          cancelButton: 'custom-button-cancel-1',
          icon: 'custom-icon-class-1'
        }
      }).then((result) => {
        if (result.isConfirmed) {
          /// Aquí puedes agregar la lógica para eliminar al usuario
        fetch("/deleteAsignacion", {
          method: "POST",
          headers: {
            "Content-Type": "application/json" // Establece el tipo de medio como JSON
          },
          body: JSON.stringify(data)
        })
          .then(response => response.json())
          .then(data => {
            // Maneja la respuesta del servidor aquí
            console.log(data);
            // Recarga la página o realiza otras acciones según sea necesario
          })
          .catch(error => {
            // Maneja los errores aquí
            console.error(error);
          });
          Swal.fire(
            'Eliminada',
            'La asignación ha sido eliminada.',
            'success'
          ).then(() => {
            // Refresca la ventana después de la confirmación
            location.reload();
          });
          
        } else {
          Swal.fire({
            title: 'Cancelado',
            text: 'La eliminación de la asignación ha sido cancelada.',
            icon: 'info',
            customClass: {
              confirmButton: 'custom-button-confirmation-2',
              icon: 'custom-icon-class-2',
            }
          });
        }
      });
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



