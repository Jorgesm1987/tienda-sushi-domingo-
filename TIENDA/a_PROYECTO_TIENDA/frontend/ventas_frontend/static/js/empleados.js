const apiUrl = 'http://127.0.0.1:8000/api/empleados/'; // Asegúrate de que esta URL es correcta

function showMessage(message, success = true) {
    const messageElem = document.getElementById('mensaje');
    messageElem.textContent = message;
    messageElem.className = success ? 'alert alert-success' : 'alert alert-danger';
    messageElem.style.display = 'block';
    setTimeout(() => {
        messageElem.style.display = 'none';
    }, 3000);
}

function createEmpleado() {
    const empleadoData = {
        run: document.getElementById('run').value,
        nombres: document.getElementById('nombres').value,
        ap_paterno: document.getElementById('ap_paterno').value,
        ap_materno: document.getElementById('ap_materno').value,
        email: document.getElementById('email').value,
        genero: document.getElementById('genero').value,
        region: document.getElementById('region').value,
        provincia: document.getElementById('provincia').value,
        comuna: document.getElementById('comuna').value
    };

    fetch(`${apiUrl}create/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(empleadoData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showMessage('Empleado agregado exitosamente');
        } else {
            showMessage('Error al agregar empleado', false);
        }
    })
    .catch(error => {
        showMessage('Error al agregar empleado', false);
    });
}

function readEmpleado() {
    const run = document.getElementById('run').value;

    fetch(`${apiUrl}read/${run}/`)
    .then(response => response.json())
    .then(data => {
        if (data.run) {
            document.getElementById('nombres').value = data.nombres;
            document.getElementById('ap_paterno').value = data.ap_paterno;
            document.getElementById('ap_materno').value = data.ap_materno;
            document.getElementById('email').value = data.email;
            document.getElementById('genero').value = data.genero;
            document.getElementById('region').value = data.region;
            document.getElementById('provincia').value = data.provincia;
            document.getElementById('comuna').value = data.comuna;
            showMessage('Empleado encontrado');
        } else {
            showMessage('Empleado no encontrado', false);
        }
    })
    .catch(error => {
        showMessage('Error al leer empleado', false);
    });
}

function updateEmpleado() {
    const run = document.getElementById('run').value;
    const empleadoData = {
        nombres: document.getElementById('nombres').value,
        ap_paterno: document.getElementById('ap_paterno').value,
        ap_materno: document.getElementById('ap_materno').value,
        email: document.getElementById('email').value,
        genero: document.getElementById('genero').value,
        region: document.getElementById('region').value,
        provincia: document.getElementById('provincia').value,
        comuna: document.getElementById('comuna').value
    };

    fetch(`${apiUrl}update/${run}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(empleadoData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showMessage('Empleado actualizado exitosamente');
        } else {
            showMessage('Error al actualizar empleado', false);
        }
    })
    .catch(error => {
        showMessage('Error al actualizar empleado', false);
    });
}

function deleteEmpleado() {
    const run = document.getElementById('run').value;

    fetch(`${apiUrl}delete/${run}/`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            showMessage('Empleado eliminado exitosamente');
        } else {
            showMessage('Error al eliminar empleado', false);
        }
    })
    .catch(error => {
        showMessage('Error al eliminar empleado', false);
    });
}

function clearForm() {
    document.getElementById('empleado-form').reset();
}
