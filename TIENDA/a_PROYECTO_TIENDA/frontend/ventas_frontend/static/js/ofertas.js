// ofertas.js
document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const removeFromCartButtons = document.querySelectorAll('.remove-from-cart');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.dataset.productId;
            const productName = this.dataset.productName;
            const productPrice = parseFloat(this.dataset.productPrice);
            addToCart(productName, productPrice, this);
        });
    });

    removeFromCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.dataset.productId;
            const productName = this.dataset.productName;
            removeFromCart(productName, this);
        });
    });
});

function addToCart(name, price, button) {
    const item = cart.find(item => item.name === name);

    if (item) {
        item.quantity += 1;
    } else {
        cart.push({ name, price, quantity: 1 });
    }
    updateCartSummary();
    localStorage.setItem('cart', JSON.stringify(cart));
    showMessage(name + ' añadido al carrito', button);
}

function removeFromCart(name, button) {
    const itemIndex = cart.findIndex(item => item.name === name);

    if (itemIndex !== -1) {
        cart.splice(itemIndex, 1);
    }
    updateCartSummary();
    localStorage.setItem('cart', JSON.stringify(cart));
    showMessage(name + ' eliminado del carrito', button);
}

function updateCartSummary() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    cartItems.innerHTML = '';

    let total = 0;

    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - $${item.price.toFixed(2)} x ${item.quantity}`;
        cartItems.appendChild(li);
        total += item.price * item.quantity;
    });

    cartTotal.textContent = 'Total a pagar: $' + total.toFixed(2);
}

function showMessage(message, button) {
    const messageElem = button.parentElement.nextElementSibling;
    messageElem.textContent = message;
    messageElem.style.display = 'block';
    setTimeout(() => {
        messageElem.style.display = 'none';
    }, 3000);
}

