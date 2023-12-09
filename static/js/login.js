function wait(){
    const waitv = document.querySelector("div.snackbar.wait");
    if (waitv != null){
        waitv.classList.add("show");
        setTimeout(()=>{waitv.classList.remove("show")}, 3000);
    }
}

function success(){
    const successv = document.querySelector("div.snackbar.success");
    if (successv != null){
        successv.classList.add("show");
        setTimeout(()=>{successv.classList.remove("show")}, 3000);
    }
}

function fail(){
    const failv = document.querySelector("body > div.snackbar.fail");
    if (failv != null){
        failv.classList.add("show");
        setTimeout(()=>{failv.classList.remove("show")}, 3000);
    }
}

window.onload = () => {
    const headersList = {
        "Accept": "application/json",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/json"
    }
    const request_handler = async () => {
        let post_obj = {}
        wait();

        const email = document.querySelector("#email");
        const password  = document.querySelector("#senha");

        if (email instanceof HTMLInputElement && password instanceof HTMLInputElement){
            post_obj[email.name] = email.value;
            post_obj[password.name] = password.value;
        }

        const response = await fetch("/login", { 
            method: "POST",
            headers: headersList,
            body: JSON.stringify(
                post_obj
            )
        });

        if (response.ok){
            success()
            if (response.redirected){
                window.location.replace(response.url);
            }
        }else {
            fail()
        }
    };
    const submit = document.querySelector("#submit_form");

    if (submit instanceof HTMLInputElement){
        submit.onclick = request_handler;
    }
    for (const input of document.getElementsByTagName("input")){
        input.addEventListener("keypress", event => {
            if (event.key === "Enter"){
                request_handler();
            }
        });
    }
};