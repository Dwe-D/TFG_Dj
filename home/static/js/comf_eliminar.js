function confirmarEliminacion() {
    if (confirm("¿Estás seguro de que deseas eliminar los dispositivos seleccionados?")) {
        document.getElementById("eliminarForm").submit();
    }
}