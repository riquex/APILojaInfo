window.onload = () => {
    const id = document.getElementById("id");
    const nome = document.getElementById("nome");
    const nascimento = document.getElementById("nascimento");
    const telefone = document.getElementById("telefone");
    const cpf = document.getElementById("cpf");
    const email = document.getElementById("email");
    const cep = document.getElementById("cep");
    const rua = document.getElementById("rua");
    const municipio = document.getElementById("municipio");
    const estado = document.getElementById("estado");
    const complemento = document.getElementById("complemento");

    sortTable = (column=0, inverse=false) => {
        const table = document.getElementById("tabela-gerencimento-usuarios");
        let done = false;
        let swap = false;
        let i = 0;

        if (table instanceof HTMLTableElement){
            const rows = table.rows;
            while (!done){
                done = true;
                swap = false;

                for(i=1; i < (rows.length - 1); ++i){
                    const x = rows[i    ].getElementsByTagName("td")[column];
                    const y = rows[i + 1].getElementsByTagName("td")[column];

                    if (inverse){
                        if (x.innerHTML.toLowerCase() < y.innerHTML.toLocaleLowerCase()){
                            swap = true;
                            break;
                        }
                    }else if (x.innerHTML.toLowerCase() > y.innerHTML.toLocaleLowerCase()){
                        swap = true;
                        break;
                    }
                }

                if (swap){
                    rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                    done = false;
                }
            }
        }
        
    };

    id.onclick = () => {
        sortTable(0, false);
    };
    nome.onclick = () => {
        sortTable(1, false);
    };
    nascimento.onclick = () => {
        sortTable(2, false);
    };
    telefone.onclick = () => {
        sortTable(3, false);
    };
    cpf.onclick = () => {
        sortTable(4, false);
    };
    email.onclick = () => {
        sortTable(5, false);
    };
    cep.onclick = () => {
        sortTable(6, false);
    };
    rua.onclick = () => {
        sortTable(7, false);
    };
    municipio.onclick = () => {
        sortTable(8, false);
    };
    estado.onclick = () => {
        sortTable(9, false);
    };
    complemento.onclick = () => {
        sortTable(10, false);
    };
};