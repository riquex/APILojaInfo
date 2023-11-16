document.getElementById("submit_form").addEventListener("click", ()=>{
    fetch("http://127.0.0.1:5000/useraddress/4")
    .then(response => response.json())
    .then(json => {
        if(json == 200)
        {
            //Retorna a mensagem com sucesso
        }
        else
        {
            //Caso tenha algum problema 
        }
        document.getElementById("Mensagem").style.visibility="visible"
        document.getElementById("Mensagem").innerHTML= "usuario criado com sucesso" 
        console.log(json)
    })
})