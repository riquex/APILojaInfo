export function wait(){
    const waitv = document.querySelector("div.snackbar.wait");
    if (waitv != null){
        waitv.classList.add("show");
        setTimeout(()=>{waitv.classList.remove("show")}, 3000);
    }
}

export function success(){
    const successv = document.querySelector("div.snackbar.success");
    if (successv != null){
        successv.classList.add("show");
        setTimeout(()=>{successv.classList.remove("show")}, 3000);
    }
}

export function fail(){
    const failv = document.querySelector("body > div.snackbar.fail");
    if (failv != null){
        failv.classList.add("show");
        setTimeout(()=>{failv.classList.remove("show")}, 3000);
    }
}