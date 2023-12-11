const wait = (text='Aguarde ...') => {
    const waitv = document.querySelector("div.snackbar.wait");
    if (waitv != null){
        waitv.innerHTML = text;
        waitv.classList.add("show");
        setTimeout(()=>{waitv.classList.remove("show")}, 3000);
    }
};

const success = (text='Registro Bem Sucedido') => {
    const successv = document.querySelector("div.snackbar.success");
    if (successv != null){
        successv.innerHTML = text;
        successv.classList.add("show");
        setTimeout(()=>{successv.classList.remove("show")}, 3000);
    }
};

const fail = (text='Registro Mal Sucedido') => {
    const failv = document.querySelector("div.snackbar.fail");
    if (failv != null){
        failv.innerHTML = text;
        failv.classList.add("show");
        setTimeout(()=>{failv.classList.remove("show")}, 3000);
    }
};

window.onload = () => {
    const comprar  = document.querySelector("div.btns > button.buy-btn");
    const carrinho = document.querySelector("div.btns > button.cart-btn");
    const main_div = document.querySelector("div.produto-area");

    if (carrinho instanceof HTMLButtonElement){
        carrinho.onclick = async () => {
            wait()
            let data_obj = {'quantidade': 1};

            if (main_div instanceof Element){
                data_obj['idProduto'] = main_div.id;
            }

            const headersList = {
                "Accept": "application/json",
                "User-Agent": "Thunder Client (https://www.thunderclient.com)",
                "Content-Type": "application/json"
            }

            const response = await fetch("/carrinho", { 
                method: "PUT",
                headers: headersList,
                body: JSON.stringify(
                    data_obj
                )
            });

            if (response.ok){
                success("Produto Adicionado Ao Carrinho");
            }else{
                fail("Não foi possível adicionar ao carrinho");
            }
        };
    }
};