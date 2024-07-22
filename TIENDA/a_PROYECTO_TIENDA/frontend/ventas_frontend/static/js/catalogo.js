let cart = JSON.parse(localStorage.getItem('cart')) || [];

function addToCart(name, price, element) {
    const quantity = parseInt(element.previousElementSibling.value);
    const item = cart.find(product => product.name === name);

    if (item) {
        item.quantity += quantity;
    } else {
        cart.push({ name, price, quantity });
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartSummary();

    const clienteId = getClienteId();

    fetch('/agregar_producto/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            producto_id: name, // Debería ser el ID del producto
            cantidad: quantity,
            cliente_id: clienteId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status !== 'Producto agregado al carrito') {
            alert('Error al agregar el producto al carrito');
        }
    });
}

function removeFromCart(name, element) {
    cart = cart.filter(product => product.name !== name);
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartSummary();

    const clienteId = getClienteId();

    fetch('/eliminar_producto/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            producto_id: name, // Debería ser el ID del producto
            cliente_id: clienteId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status !== 'Producto eliminado del carrito') {
            alert('Error al eliminar el producto del carrito');
        }
    });
}

function processPayment() {
    const clienteId = getClienteId();

    fetch('/procesar_pago/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            cliente_id: clienteId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'Compra procesada exitosamente') {
            alert('Compra procesada exitosamente');
            cart = [];
            localStorage.setItem('cart', JSON.stringify(cart));
            updateCartSummary();
        } else {
            alert('Error al procesar la compra');
        }
    });
}

function updateCartSummary() {
    const cartItemsElement = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    cartItemsElement.innerHTML = '';
    let total = 0;

    cart.forEach(product => {
        const li = document.createElement('li');
        li.innerHTML = `${product.name} - $${product.price.toLocaleString('es-CL')} x ${product.quantity}
            <button class="btn btn-remove-small" onclick="removeFromCart('${product.name}', this)">Eliminar</button>`;
        cartItemsElement.appendChild(li);
        total += product.price * product.quantity;
    });

    cartTotalElement.textContent = `Total a pagar: $${total.toLocaleString('es-CL')}`;
}

function getClienteId() {
    // Implementa una función para obtener el ID del cliente
    return 1; // Placeholder
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById('btn-pagar').addEventListener('click', processPayment);
document.addEventListener('DOMContentLoaded', updateCartSummary);
