// idProduto, NOME, Descricao, Valor, staticlink
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
        console.log(data);

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
                    }
                }
            }
        }
    };

    update.dispatchEvent(clickEvent)
};