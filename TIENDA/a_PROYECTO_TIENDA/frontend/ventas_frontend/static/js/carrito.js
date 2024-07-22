let cart = JSON.parse(localStorage.getItem('cart')) || [];

function renderCart() {
    const cartTableBody = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    cartTableBody.innerHTML = '';
    let total = 0;

    cart.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${product.name}</td>
            <td>$${product.price.toLocaleString('es-CL')}</td>
            <td>${product.quantity}</td>
            <td>$${(product.price * product.quantity).toLocaleString('es-CL')}</td>
            <td><button class="btn btn-remove" onclick="removeFromCart('${product.name}')">Eliminar</button></td>
        `;
        cartTableBody.appendChild(row);
        total += product.price * product.quantity;
    });

    cartTotalElement.textContent = `Total a pagar: $${total.toLocaleString('es-CL')}`;
}

function removeFromCart(name) {
    cart = cart.filter(product => product.name !== name);
    localStorage.setItem('cart', JSON.stringify(cart));
    renderCart();
}

function checkout() {
    const clienteId = getClienteId(); // Obtén el ID del cliente de alguna manera

    fetch('/procesar_pago/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            cliente_id: clienteId,
            cart: cart
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la solicitud');
        }
        return response.json();
    })
    .then(data => {
        if (data.status === 'Compra procesada exitosamente') {
            alert('Pago realizado con éxito');
            localStorage.removeItem('cart');
            cart = [];
            renderCart();
        } else {
            alert('Error al realizar el pago: ' + data.message);
        }
    })
    .catch(error => {
        alert('Error al realizar el pago: ' + error.message);
    });
}

function getClienteId() {
    // Implementa una función para obtener el ID del cliente
    return 1; // Placeholder
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', renderCart);



