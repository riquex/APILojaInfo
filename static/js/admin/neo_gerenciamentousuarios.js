/**
 * User Type
 * @typedef {Object} User
 * @property {string} idUsuarios
 * @property {string} nome
 * @property {string} cpf
 * @property {string} dataNascimento
 * @property {string} telefone
 * @property {string} cep
 * @property {string} rua
 * @property {string} municipio
 * @property {string} estado
 * @property {string} complemento
 */

/**
 * 
 * @param {any} value 
 * @returns {boolean}
 */

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

const changeInformation = async (data_obj) => {
    const headersList = {
        "Accept": "application/json",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/json"
    }

    const response = await fetch("/user/atualizarusuario", { 
        method: "PUT",
        headers: headersList,
        body: JSON.stringify(
            data_obj
        )
    });

    return response.ok;
};

window.onload = () => {
    const columns = ["idUsuarios","nome","dataNascimento","telefone","cpf","email","cep","rua","municipio","estado","complemento"];
    const columntrans = {
        id:         "idUsuarios",
        nascimento: "dataNascimento",
        nome:       "nome",
        telefone:   "telefone",
        cpf:        "cpf",
        email:      "email",
        cep:        "cep",
        rua:        "rua",
        municipio:  "municipio",
        estado:     "estado",
        complemento:"complemento"
    };

    let search_data = {
        column: "Nome",
        stringlike: "",
        start: -1
    }

    const table = document.getElementById("kilobyte-clients");

    const clickEvent = new Event("click");

    let orberby = ['idUsuario', false];
    /**
     * JackSort
     * @param {User} a 
     * @param {User} b 
     * @returns {-1|0|1}
     */
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

    const update = document.getElementById("update");
    const search_bar = document.getElementById("search-bar");
    const search_inp = document.getElementById("searchInp");
    const popup = document.querySelector("body > div.content > div.form-popup");

    update.onclick = async () => {
        const headersList = {
            "Accept": "application/json",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Content-Type": "application/json"
        }

        if (search_inp instanceof HTMLInputElement)
            search_data["stringlike"] = search_inp.value;

        const response = await fetch("/admin/fetchusersall", { 
            method: "POST",
            headers: headersList,
            body: JSON.stringify(
                search_data
            )
        });

        /**
         * @type {[User]}
         */
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
                            const h3 = document.querySelector("div.form-popup > h3");
                            h3.innerHTML = `Usuário ID:${data_obj['idUsuarios']}`;

                            const nome = document.querySelector("#inp-nome");
                            if (nome instanceof HTMLInputElement) nome.value = data_obj['nome'];
                            const cpf = document.querySelector("#inp-cpf");
                            if (cpf instanceof HTMLInputElement) cpf.value = data_obj['cpf'];
                            const datanascimento = document.querySelector("#inp-datanascimento");
                            if (datanascimento instanceof HTMLInputElement) datanascimento.value = data_obj['dataNascimento'];
                            const telefone = document.querySelector("#inp-telefone");
                            if (telefone instanceof HTMLInputElement) telefone.value = data_obj['telefone'];
                            const cep = document.querySelector("#inp-cep");
                            if (cep instanceof HTMLInputElement) cep.value = data_obj['cep'];
                            const rua = document.querySelector("#inp-rua");
                            if (rua instanceof HTMLInputElement) rua.value = data_obj['rua'];
                            const municipio = document.querySelector("#inp-municipio");
                            if (municipio instanceof HTMLInputElement) municipio.value = data_obj['municipio'];
                            const estado = document.querySelector("#inp-estado");
                            if (estado instanceof HTMLInputElement) estado.value = data_obj['estado'];
                            const complemento = document.querySelector("#inp-complemento");
                            if (complemento instanceof HTMLInputElement) complemento.value = data_obj['complemento'];

                            if (popup instanceof Element){
                                popup.classList.add('form-popup-show');
                            }
                        };
                    }
                }
            }
        }
    };

    const change_active = (event=undefined) => {
        for (const element in search_bar.children){
            element.classList.remove("active");
        }

        if (event instanceof Event){
            event.target.classList.add("active");
            search_data["column"] = columntrans[event.target.innerHTML];
        }
    };

    for (const element of search_bar.children){
        if (element instanceof HTMLButtonElement){
            element.onclick = change_active;
        }
    }

    search_inp.onkeydown = (event = undefined) => {
        if (event instanceof Event){
            if (event.key === 'Enter'){
                update.dispatchEvent(clickEvent);
            }
        }
    }

    const close_popup = document.querySelector("div.form-popup > button.close-form");
    if (close_popup instanceof HTMLButtonElement){
        close_popup.onclick = () => {
            if (popup instanceof Element){
                popup.classList.remove('form-popup-show');
            }
        }
    }

    const submit_btn = document.querySelector('div.form-popup > * > button[type=submit]');
    if (submit_btn instanceof HTMLButtonElement){
        submit_btn.onclick = async () => {
            wait();
            let data_obj = {}
            const h3 = document.querySelector("div.form-popup > h3");
            if (h3 instanceof Element) data_obj['idUsuarios'] = h3.innerHTML.replace(/\D/g, '');
            const nome = document.querySelector("#inp-nome");
            if (nome instanceof HTMLInputElement) data_obj['nome'] = nome.value;
            const cpf = document.querySelector("#inp-cpf");
            if (cpf instanceof HTMLInputElement) data_obj['cpf'] = cpf.value;
            const datanascimento = document.querySelector("#inp-datanascimento");
            if (datanascimento instanceof HTMLInputElement) data_obj['dataNascimento'] = datanascimento.value;
            const telefone = document.querySelector("#inp-telefone");
            if (telefone instanceof HTMLInputElement) data_obj['telefone'] = telefone.value;
            const cep = document.querySelector("#inp-cep");
            if (cep instanceof HTMLInputElement) data_obj['cep'] = cep.value;
            const rua = document.querySelector("#inp-rua");
            if (rua instanceof HTMLInputElement) data_obj['rua'] = rua.value;
            const municipio = document.querySelector("#inp-municipio");
            if (municipio instanceof HTMLInputElement) data_obj['municipio'] = municipio.value;
            const estado = document.querySelector("#inp-estado");
            if (estado instanceof HTMLInputElement) data_obj['estado'] = estado.value;
            const complemento = document.querySelector("#inp-complemento");
            if (complemento instanceof HTMLInputElement) data_obj['complemento'] = complemento.value;

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
                const h3 = document.querySelector("div.form-popup > h3");
                if (h3 instanceof Element) data_obj['idUsuarios'] = h3.innerHTML.replace(/\D/g, '');

                const headersList = {
                    "Accept": "application/json",
                    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
                    "Content-Type": "application/json"
                }

                const response = await fetch("/user/delecaousuario", { 
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
}