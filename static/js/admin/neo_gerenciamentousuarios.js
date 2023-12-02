const is_string = value => typeof value === 'string' || value instanceof String;

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

                for(const data_obj of data){
                    const row = table.insertRow();

                    for (const name of columns){
                        const cell = row.insertCell();
                        cell.innerHTML = data_obj[name]
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

    update.dispatchEvent(clickEvent)
}