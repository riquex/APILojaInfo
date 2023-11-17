window.onload = async function(){
    document.getElementById("submit_form").addEventListener("click", async () => {
        const response = await fetch("/userinfo/4");
        const dados = await response.json();

        console.log(dados)
        const mensagem = document.getElementById("Mensagem");
        mensagem.style.visibility = "visible";
        mensagem.innerHTML = "usuario criado com sucesso"; 
    })
}