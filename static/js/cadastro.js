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

window.onload = function(){
    document.getElementById("submit_form").addEventListener("click", async () => {
        wait();
        let data_obj = {};

        const nome = document.getElementById("nome");
        if (nome instanceof HTMLInputElement) data_obj['nome'] = nome.value;

        const senha = document.getElementById("senha");
        if (senha instanceof HTMLInputElement) data_obj['senha'] = senha.value;

        const cpf = document.getElementById("cpf");
        if (cpf instanceof HTMLInputElement) data_obj['cpf'] = cpf.value;

        const datanascimento = document.getElementById("datanascimento");
        if (datanascimento instanceof HTMLInputElement) data_obj['datanascimento'] = datanascimento.value;

        const telefone = document.getElementById("telefone");
        if (telefone instanceof HTMLInputElement) data_obj['telefone'] = telefone.value;

        const email = document.getElementById("email");
        if (email instanceof HTMLInputElement) data_obj['email'] = email.value;

        const cep = document.getElementById("cep");
        if (cep instanceof HTMLInputElement) data_obj['cep'] = cep.value;

        const rua = document.getElementById("rua");
        if (rua instanceof HTMLInputElement) data_obj['rua'] = rua.value;

        const municipio = document.getElementById("municipio");
        if (municipio instanceof HTMLInputElement) data_obj['municipio'] = municipio.value;

        const estado = document.getElementById("estado");
        if (estado instanceof HTMLInputElement) data_obj['estado'] = estado.value;

        const complemento = document.getElementById("complemento");
        if (complemento instanceof HTMLInputElement) data_obj['complemento'] = complemento.value;

        console.log(data_obj);

        const headersList = {
            "Accept": "application/json",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Content-Type": "application/json"
        }

        const response = await fetch("/cadastro", { 
            method: "POST",
            headers: headersList,
            body: JSON.stringify(
                data_obj
            )
        });

        if (response.ok){
            success();
        }else {
            fail();
        }

        if (response.redirected){
            window.location.replace(response.url)
        }
    })
}