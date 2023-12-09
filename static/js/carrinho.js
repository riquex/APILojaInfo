// dados dos itens - Modificar para obter dinamicamente do backend.
const itens = [
    { nome: 'Produto 1', preco: 50.00 },
    { nome: 'Produto 2', preco: 30.00 },
    // Pode adicionar mais itens manualmente
];

// Função para renderizar os itens no carrinho
function renderizarItens() {
    const listaItens = document.getElementById('lista-itens');
    listaItens.innerHTML = '';

    let subtotal = 0;

    itens.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.nome} - R$ ${item.preco.toFixed(2)}`;
        listaItens.appendChild(li);

        subtotal += item.preco;
    });

    // Atualizar a compra
    const subtotalSpan = document.getElementById('subtotal');
    subtotalSpan.textContent = subtotal.toFixed(2);

    const freteSpan = document.getElementById('frete');
    // Adicionar lógica para calcular o frete

    const totalSpan = document.getElementById('total');
    const total = subtotal + parseFloat(freteSpan.textContent);
    totalSpan.textContent = total.toFixed(2);
}

// Inicializar o carrinho ao carregar a página
window.onload = function () {
    renderizarItens();
};

// Simular finalização da compra - Modificar para obter dinamicamente do backend.
function finalizarCompra() {
    alert('Compra finalizada! Obrigado por comprar conosco.');
}
