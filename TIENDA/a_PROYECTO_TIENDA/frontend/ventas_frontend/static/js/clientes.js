// static/js/clientes.js

const apiUrl = 'http://127.0.0.1:8000/api/clientes/';

function createCliente() {
    const clienteData = {
        rut: document.getElementById('rut').value,
        nombre: document.getElementById('nombre').value,
        edad: document.getElementById('edad').value,
        telefono: document.getElementById('telefono').value,
        email: document.getElementById('email').value
    };

    fetch(`${apiUrl}create/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(clienteData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showMessage('Cliente agregado exitosamente');
        } else {
            showMessage('Error al agregar cliente', false);
        }
    })
    .catch(error => {
        showMessage('Error al agregar cliente', false);
    });
}

function readCliente() {
    const rut = document.getElementById('rut').value;

    fetch(`${apiUrl}read/${rut}/`)
    .then(response => response.json())
    .then(data => {
        if (data.rut) {
            document.getElementById('nombre').value = data.nombre;
            document.getElementById('edad').value = data.edad;
            document.getElementById('telefono').value = data.telefono;
            document.getElementById('email').value = data.email;
            showMessage('Cliente encontrado');
        } else {
            showMessage('Cliente no encontrado', false);
        }
    })
    .catch(error => {
        showMessage('Error al leer cliente', false);
    });
}

function updateCliente() {
    const rut = document.getElementById('rut').value;
    const clienteData = {
        nombre: document.getElementById('nombre').value,
        edad: document.getElementById('edad').value,
        telefono: document.getElementById('telefono').value,
        email: document.getElementById('email').value
    };

    fetch(`${apiUrl}update/${rut}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(clienteData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showMessage('Cliente actualizado exitosamente');
        } else {
            showMessage('Error al actualizar cliente', false);
        }
    })
    .catch(error => {
        showMessage('Error al actualizar cliente', false);
    });
}

function deleteCliente() {
    const rut = document.getElementById('rut').value;

    fetch(`${apiUrl}delete/${rut}/`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            showMessage('Cliente eliminado exitosamente');
        } else {
            showMessage('Error al eliminar cliente', false);
        }
    })
    .catch(error => {
        showMessage('Error al eliminar cliente', false);
    });
}

function showMessage(message, success = true) {
    const messageElem = document.getElementById('mensaje');
    messageElem.textContent = message;
    messageElem.className = success ? 'alert alert-success' : 'alert alert-danger';
    messageElem.style.display = 'block';
    setTimeout(() => {
        messageElem.style.display = 'none';
    }, 3000);
}

function clearForm() {
    document.getElementById('cliente-form').reset();
}
