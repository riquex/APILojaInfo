const is_string = value => typeof value === 'string' || value instanceof String;

const wait = () => {
    const waitv = document.querySelector("div.snackbar.wait");
    if (waitv != null){
        waitv.classList.add("show");
        setTimeout(()=>{waitv.classList.remove("show")}, 3000);
    }
};

const success = () => {
    const successv = document.querySelector("div.snackbar.success");
    if (successv != null){
        successv.classList.add("show");
        setTimeout(()=>{successv.classList.remove("show")}, 3000);
    }
};

const fail = () => {
    const failv = document.querySelector("div.snackbar.fail");
    if (failv != null){
        failv.classList.add("show");
        setTimeout(()=>{failv.classList.remove("show")}, 3000);
    }
};

/**
 * format current 1234567 to 12,345.67
 * @param {string} n value
 * @returns {string}
 */
const formatCurrency = (n) => {
    let val = n.replace(/\D/g, "");
    if (val.length > 2){
        const left = val.substring(0, val.length -2).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        const right = val.substring(val.length -2);
        val = left + "," + right;
    }
    return val
};

const changeInformation = async (data_obj) => {
    const headersList = {
        "Accept": "application/json",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/json"
    }

    const response = await fetch("/admin/atualizarproduto", { 
        method: "PUT",
        headers: headersList,
        body: JSON.stringify(
            data_obj
        )
    });

    return response.ok;
};

window.onload = () => {
    const columns = ["idProduto", "NOME", "Descricao", "Valor", "Quantidade"];
    const columntrans = {
        id:         "idProduto",
        nome:       "NOME",
        descricao:  "Descricao",
        valor:      "Valor",
        quantidade: "Quantidade",
        staticlink: "staticlink",
    };
    const search_data = {
        column: "NOME",
        stringlike: "",
        start: -1
    }

    const table = document.querySelector("#kilobyte-products");

    const clickEvent = new Event("click");

    let orberby = ['idUsuario', false];
    const jackSort = (a, b) => {
        if (a instanceof Object && b instanceof Object){
            let valueA = a[orberby[0]];
            let valueB = b[orberby[0]];
            if (is_string(valueA) && is_string(valueB)){
                valueA = valueA.toLocaleLowerCase();
                valueB = valueB.toLocaleLowerCase();
            }
            if (valueA < valueB){
                return -1;
            }
            if (valueA > valueB){
                return 1;
            }
        }
        return 0;
    };

    const update = document.getElementById("update");
    const search_bar = document.getElementById("search-bar");
    const search_inp = document.getElementById("searchInp");
    const preco_input = document.querySelector("#inp-valor");
    const popup = document.querySelector("body > div.content > div.form-popup");

    update.onclick = async () => {
        const headersList = {
            "Accept": "application/json",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Content-Type": "application/json"
        }

        if (search_inp instanceof HTMLInputElement)
            search_data["stringlike"] = search_inp.value;

        const response = await fetch("/admin/fetchproductsall", { 
            method: "POST",
            headers: headersList,
            body: JSON.stringify(
                search_data
            )
        });

        const data = await response.json();

        if (table instanceof HTMLTableElement){
            while (table.rows.length > 1){
                table.deleteRow(1);
            }

            if (data instanceof Array){
                data.sort(jackSort)
                if (orberby[1])
                    data.reverse();

                for(const data_obj of data){
                    const row = table.insertRow();

                    for (const name of columns){
                        const cell = row.insertCell();
                        cell.innerHTML = data_obj[name]
                        cell.onclick = () => {
                            const h3 = document.querySelector("div.alter-product.form-popup > h3");
                            h3.innerHTML = `Produto ID:${data_obj['idProduto']}`;

                            const nome = document.querySelector("#inp-nome");
                            if (nome instanceof HTMLInputElement){
                                nome.value = data_obj['NOME'];
                            }

                            const valor = document.querySelector("#inp-valor");
                            if (valor instanceof HTMLInputElement){
                                valor.value = data_obj['Valor'];
                            }

                            const desc = document.querySelector("#text-descricao");
                            if (desc instanceof HTMLTextAreaElement){
                                desc.value = data_obj['Descricao'];
                            }

                            if (popup instanceof Element){
                                popup.classList.add('form-popup-show');
                            }
                        };
                    }
                }
            }
        }
    };

    const table_header_click_handle = (event) => {
        if (event instanceof Event){
            const column_name = columntrans[event.target.innerHTML];
            orberby[1] = orberby[0] == column_name ? !orberby[1]: false;
            orberby[0] = column_name;
            update.dispatchEvent(clickEvent);
        }
    };

    if (table instanceof HTMLTableElement){
        const firt_row = table.rows.item(0);
        if (firt_row != null){
            for(const element of firt_row.children){
                if (element instanceof HTMLTableCellElement){
                    element.onclick = table_header_click_handle;
                }
            }
        }
    }

    if (preco_input instanceof HTMLInputElement){
        preco_input.onkeyup =
        preco_input.onkeydown =
        preco_input.onchange = 
        preco_input.onblur =
        preco_input.onfocus = () => {
            const new_value = formatCurrency(preco_input.value);
            preco_input.value = "R$"+ new_value;
        };
    }

    const close_popup = document.querySelector("div.alter-product.form-popup > button.close-form");
    if (close_popup instanceof HTMLButtonElement){
        close_popup.onclick = () => {
            if (popup instanceof Element){
                popup.classList.remove('form-popup-show');
            }
        }
    }

    const submit_btn = document.querySelector('div.form-popup > * > button[type=submit].submit-btn');
    if (submit_btn instanceof HTMLButtonElement){
        submit_btn.onclick = async () => {
            wait();
            let data_obj = {}
            const h3 = document.querySelector("div.alter-product.form-popup > h3");
            if (h3 instanceof Element){
                data_obj['idProduto'] = h3.innerHTML.replace(/\D/g, '');
            }

            const nome = document.querySelector("#inp-nome");
            if (nome instanceof HTMLInputElement){
                data_obj['NOME'] = nome.value;
            }

            const valor = document.querySelector("#inp-valor");
            if (valor instanceof HTMLInputElement){
                data_obj['Valor'] = valor.value;
            }

            const desc = document.querySelector("#text-descricao");
            if (desc instanceof HTMLTextAreaElement){
                data_obj['Descricao'] = desc.value;
            }

            const value = await changeInformation(data_obj)
            if (value){
                success();
            }else{
                fail();
            }
        };
    }
    const delete_btn = document.querySelector("div.form-popup > * > button[type=submit].delete-btn");
    if (delete_btn instanceof HTMLButtonElement){
        delete_btn.onclick = async () => {
            if(window.confirm('Esta ação tem efeitos permanetes.\nTem certeza disto?')){
                wait();
                let data_obj = {}
                const h3 = document.querySelector("div.alter-product.form-popup > h3");
                if (h3 instanceof Element) data_obj['idProduto'] = h3.innerHTML.replace(/\D/g, '');

                const headersList = {
                    "Accept": "application/json",
                    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
                    "Content-Type": "application/json"
                }

                const response = await fetch("/admin/deleteprod", { 
                    method: "DELETE",
                    headers: headersList,
                    body: JSON.stringify(
                        data_obj
                    )
                });

                if (response.ok){
                    success();
                }else{
                    fail();
                }
            }
        };
    }

    update.dispatchEvent(clickEvent)
};