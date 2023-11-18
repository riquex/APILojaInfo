window.onload = function(){
    document.getElementById("submit_form").addEventListener("click", async () => {
        let nome_v = "";
        const nome = document.getElementById("nome");
        if (nome instanceof HTMLInputElement) nome_v = nome.value;

        let senha_v = "";
        const senha = document.getElementById("senha");
        if (senha instanceof HTMLInputElement) senha_v = senha.value;

        let cpf_v = "";
        const cpf = document.getElementById("cpf");
        if (cpf instanceof HTMLInputElement) cpf_v = cpf.value;

        let data_nascimento_v = "";
        const data_nascimento = document.getElementById("data_nascimento");
        if (data_nascimento instanceof HTMLInputElement) data_nascimento_v = data_nascimento.value;

        let telefone_v = "";
        const telefone = document.getElementById("telefone");
        if (telefone instanceof HTMLInputElement) telefone_v = telefone.value;

        let email_v = "";
        const email = document.getElementById("email");
        if (email instanceof HTMLInputElement) email_v = email.value;

        let cep_v = "";
        const cep = document.getElementById("cep");
        if (cep instanceof HTMLInputElement) cep_v = cep.value;

        let rua_v = "";
        const rua = document.getElementById("rua");
        if (rua instanceof HTMLInputElement) rua_v = rua.value;

        let municipio_v = "";
        const municipio = document.getElementById("municipio");
        if (municipio instanceof HTMLInputElement) municipio_v = municipio.value;

        let estado_v = "";
        const estado = document.getElementById("estado");
        if (estado instanceof HTMLInputElement) estado_v = estado.value;

        let complemento_v = "";
        const complemento = document.getElementById("complemento");
        if (complemento instanceof HTMLInputElement) complemento_v = complemento.value;

        console.log(email_v, senha_v, nome_v, cpf_v, rua_v, telefone_v, cep_v, data_nascimento_v, municipio_v, estado_v, complemento_v);
        const mensagem = document.getElementById("Mensagem");
        mensagem.style.visibility = "visible";
        mensagem.innerHTML = "usuario criado com sucesso"; 
    })
}