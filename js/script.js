// Función que muestra un alert cuando se envía el formulario y limpia los campos
function mostrarMensaje(event) {
    event.preventDefault(); // Evitar el envío del formulario para demostración
    
    // Obtener el formulario
    const formulario = document.getElementById("contact_form");
    const inputs = formulario.querySelectorAll("input, textarea"); // Todos los campos del formulario
    
    // Verificar si todos los campos están llenos
    let camposCompletos = true;
    inputs.forEach(input => {
      if (input.value.trim() === "") { // Si algún campo está vacío
        camposCompletos = false;
      }
    });
    
    if (camposCompletos) {
      alert("¡Su mensaje se ha enviado correctamente!");
      formulario.reset(); // Limpiar todos los campos del formulario
    } else {
      alert("Por favor, llene todos los campos antes de enviar el formulario.");
    }
}
  
// Asignar el evento al botón al cargar la página
document.addEventListener("DOMContentLoaded", () => {
    const boton = document.getElementById("form_button");
    boton.addEventListener("click", mostrarMensaje);
});
  
// Valida que solamente se ingresen números en el campo de teléfono
document.getElementById('telephone_input').addEventListener('input', function (e) {
    // Si el valor contiene algo que no es un número, muestra un alert y limpia el campo
    if (/[^0-9]/.test(this.value)) {
        alert("Este campo solo permite números.");
        this.value = this.value.replace(/[^0-9]/g, ''); // Elimina cualquier carácter que no sea un número
    }
});