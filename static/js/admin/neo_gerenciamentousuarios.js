window.onload = () => {
    const columns = ["idUsuario","nome","dataNascimento","telefone","cpf","email","cep","rua","municipio","estado","complemento"];
    const columntrans = {
        id:         "idUsuario",
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

    let post_obj = {
        column: "Nome",
        stringlike: "",
        start: -1
    }

    const table = document.getElementById("kilobyte-clients");

    const clickEvent = new Event("click");

    let orberby = ['idUsuario', false];
    const jackSort = (a, b) => {
        if (a instanceof Object && b instanceof Object){
            let valueA = a[orberby[0]];
            let valueB = b[orberby[0]];
            if (typeof(valueA) === 'string' && typeof(valueB) === 'string'){
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
        const rows = table.rows;
        const firt_row = rows.item(0);
        const childrens = firt_row.children;
        for(let i=0; i < childrens.length; ++i){
            const th = childrens[i]
            if (th instanceof HTMLTableCellElement){
                th.onclick = table_header_click_handle;
            }
        }
    }

    const update = document.getElementById("update");
    const search_bar = document.getElementById("search-bar");
    const search_inp = document.getElementById("seachInp");

    update.onclick = async () => {
        const headersList = {
            "Accept": "application/json",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Content-Type": "application/json"
        }

        if (search_inp instanceof HTMLInputElement)
            post_obj["stringlike"] = search_inp.value;

        const response = await fetch("/admin/fetchusersall", { 
            method: "POST",
            headers: headersList,
            body: JSON.stringify(
                post_obj
            )
        });

        const data = await response.json();

        if (table instanceof HTMLTableElement){
            while (table.rows.length > 1){
                table.deleteRow(1);
            }

            if (data instanceof Array){
                //console.log(data[0]);
                data.sort(jackSort)
                if (orberby[1])
                    data.reverse();

                for(let i = 0; i < data.length; ++i){
                    let row = table.insertRow();

                    for (let j = 0; j < columns.length; ++j){
                        const cell = row.insertCell();
                        //console.log(data[i], columns[j]);
                        cell.innerHTML = data[i][columns[j]]
                    }
                }
            }
        }
    };

    const change_active = (event=undefined) => {
        for (const i in search_bar.children){
            if (search_bar.children[i] instanceof HTMLButtonElement){
                search_bar.children[i].classList.remove("active");
            }
        }

        if (event instanceof Event){
            event.target.classList.add("active");
            post_obj["column"] = columntrans[event.target.innerHTML];
        }
    };

    for (const i in search_bar.children){
        if (search_bar.children[i] instanceof HTMLButtonElement){
            search_bar.children[i].onclick = change_active;
        }
    }
    update.dispatchEvent(clickEvent)
}