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
    const clickEvent = new Event("click");

    let orberby = ['idUsuario', false, (a, b) => -1]

    const numSort = (a, b) => a[orberby[0]] - b[orberby[0]];
    const strSort = (a, b) => {
        const nomeA = a[orberby[0]].toLocaleLowerCase();
        const nomeB = b[orberby[0]].toLocaleLowerCase();
        if (nomeA < nomeB){
            return -1;
        }
        if (nomeB > nomeB){
            return 1;
        }
        return 0;
    };

    id.onclick = () => {
        orberby[2] = orberby[0] == "idUsuario" ? !orberby[2]: false;
        orberby[0] = "idUsuario";
        orberby[3] = numSort;
        update.dispatchEvent(clickEvent);
    };
    nome.onclick = () => {
        orberby[2] = orberby[0] == "nome" ? !orberby[2]: false;
        orberby[0] = "nome";
        orberby[3] = strSort;
        update.dispatchEvent(clickEvent);
    };
    nascimento.onclick = () => {
        orberby[2] = orberby[0] == "dataNascimento" ? !orberby[2]: false;
        orberby[0] = "dataNascimento"
        orberby[3] = strSort;
        update.dispatchEvent(clickEvent);
    };
    telefone.onclick = () => {
        orberby[2] = orberby[0] == "telefone" ? !orberby[2]: false;
        orberby[0] = "telefone"
        orberby[3] = strSort;
        update.dispatchEvent(clickEvent);
    };
    cpf.onclick = () => {
        orberby[2] = orberby[0] == "cpf" ? !orberby[2]: false;
        orberby[0] = "cpf"
        orberby[3] = strSort;
        update.dispatchEvent(clickEvent);
    };
    email.onclick = () => {
        orberby[2] = orberby[0] == "email" ? !orberby[2]: false;
        orberby[0] = "email"
        orberby[3] = strSort;
        update.dispatchEvent(clickEvent);
    };
    cep.onclick = () => {
        orberby[2] = orberby[0] == "cep" ? !orberby[2]: false;
        orberby[0] = "cep"
        orberby[3] = strSort;
        update.dispatchEvent(clickEvent);
    };
    rua.onclick = () => {
        orberby[2] = orberby[0] == "rua" ? !orberby[2]: false;
        orberby[0] = "rua"
        orberby[3] = strSort;
        update.dispatchEvent(clickEvent);
    };
    municipio.onclick = () => {
        orberby[2] = orberby[0] == "municipio" ? !orberby[2]: false;
        orberby[0] = "municipio"
        orberby[3] = strSort;
        update.dispatchEvent(clickEvent);
    };
    estado.onclick = () => {
        orberby[2] = orberby[0] == "estado" ? !orberby[2]: false;
        orberby[0] = "estado"
        orberby[3] = strSort;
        update.dispatchEvent(clickEvent);
    };
    complemento.onclick = () => {
        orberby[2] = orberby[0] == "complemento" ? !orberby[2]: false;
        orberby[0] = "complemento"
        orberby[3] = strSort;
        update.dispatchEvent(clickEvent);
    };

    const update = document.getElementById("update");
    update.onclick = async () => {
        const headersList = {
            "Accept": "application/json",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)"
        }

        const response = await fetch("/admin/fetchusersall", { 
            method: "GET",
            headers: headersList
        });

        const data = await response.json();

        const table = document.getElementById("tabela-gerencimento-usuarios");

        if (table instanceof HTMLTableElement){
            while (table.rows.length > 1){
                table.deleteRow(1);
            }

            if (data instanceof Array){

                data.sort(orberby[3])
                if (orberby[2])
                    data.reverse();

                for(let i = 0; i < data.length; ++i){
                    let row = table.insertRow();

                    const idcell = row.insertCell();
                    idcell.innerHTML = data[i].idUsuario;

                    const nomecell = row.insertCell();
                    nomecell.innerHTML = data[i].nome;

                    const nascimentocell = row.insertCell();
                    nascimentocell.innerHTML = data[i].dataNascimento;

                    const telefonecell = row.insertCell();
                    telefonecell.innerHTML = data[i].telefone;

                    const cpfcell = row.insertCell();
                    cpfcell.innerHTML = data[i].cpf;

                    const emailcell = row.insertCell();
                    emailcell.innerHTML = data[i].email;

                    const cepcell = row.insertCell();
                    cepcell.innerHTML = data[i].cep;

                    const ruacell = row.insertCell();
                    ruacell.innerHTML = data[i].rua;

                    const municipiocell = row.insertCell();
                    municipiocell.innerHTML = data[i].municipio;

                    const estadocell = row.insertCell();
                    estadocell.innerHTML = data[i].estado;

                    const complementocell = row.insertCell();
                    complementocell.innerHTML = data[i].complemento;
                }
            }
        }
    };

    const mainrow = document.getElementById("linha-com-nomes");
    const sticky = mainrow.offsetTop;
    window.onscroll = () => {
        if (window.scrollY - 41 >= sticky){
            mainrow.classList.add("top-sticky");
        } else {
            mainrow.classList.remove("top-sticky");
        }
    };
};