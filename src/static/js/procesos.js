window.onload = function() {
    var dateField = document.getElementById("fecha");
    var today = new Date().toISOString().split("T")[0];
    dateField.value = today;
  };
