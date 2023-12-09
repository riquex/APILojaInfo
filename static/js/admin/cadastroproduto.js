const wait = () => {
    const waitv = document.querySelector("div.snackbar.wait");
    if (waitv != null){
        waitv.classList.add("show");
        setTimeout(()=>{waitv.classList.remove("show")}, 3000);
    }
}

const success = () => {
    const successv = document.querySelector("div.snackbar.success");
    if (successv != null){
        successv.classList.add("show");
        setTimeout(()=>{successv.classList.remove("show")}, 3000);
    }
}

const fail = () => {
    const failv = document.querySelector("body > div.snackbar.fail");
    if (failv != null){
        failv.classList.add("show");
        setTimeout(()=>{failv.classList.remove("show")}, 3000);
    }
}

/**
 * Read a file and return its base64 form.
 * @param {File} file file
 * @returns {Promise<string>}
 */
const toBase64 = file => new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result);
    reader.onerror = reject;
    reader.readAsDataURL(file);
});

/**
 * format current 1234567 to 12,345.67
 * @param {string} n value
 * @returns {string}
 */
const formatCurrency = (n) => {
    let val = n.replace(/\D/g, "");
    if (val.length > 2){
        const left = val.substring(0, val.length -2).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        const right = val.substring(val.length -2);
        val = left + "," + right;
    }
    return val
  }

window.onload = function(){
    const submit = document.getElementById("submit");
    const image_preview = document.getElementById("previewimage");
    const image_input = document.getElementById("imagem");
    const preco_input = document.querySelector("input.preco");

    if (image_input instanceof HTMLInputElement){
        image_input.addEventListener("change", () => {
            const input_text = document.getElementById("image-text");
            if (input_text instanceof HTMLInputElement){
                input_text.value = image_input.value.replace(/^.*[\\/]/, '');
            }

            if (image_preview instanceof HTMLImageElement && image_input.files.length){
                const file = image_input.files;
                image_preview.src = URL.createObjectURL(file.item(0));
            }
            else if (image_preview instanceof HTMLImageElement){
                image_preview.src = "#";
            }
        })
    }

    if (preco_input instanceof HTMLInputElement){
        preco_input.onkeyup =
        preco_input.onkeydown =
        preco_input.onchange = 
        preco_input.onblur =
        preco_input.onfocus = (event) => {
            const new_value = formatCurrency(preco_input.value);
            preco_input.value = "R$"+ new_value;
        };
    }

    submit.onclick = async () => {
        let post_obj = {};
        for (const input of document.getElementsByTagName("input")){
            post_obj[input.name] = input.value;
        }
        for (const textarea of document.getElementsByTagName("textarea")){
            post_obj[textarea.name] = textarea.value
        }
        if (image_input instanceof HTMLInputElement) {
            const files = image_input.files;
            if (files instanceof FileList){
                const file = files.item(0);
                if (file instanceof File){
                    const b64 = await toBase64(file);
                    post_obj["image64"] = b64;
                }
            }
        }

        const headersList = {
            "Accept": "application/json",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "Content-Type": "application/json"
        }

        let load = document.querySelector(".lds-facebook")
        if (load != null){
            load.classList.add("inline-block");
        }

        const response = await fetch("/admin/test/cadastroproduto", { 
            method: "POST",
            headers: headersList,
            body: JSON.stringify(
                post_obj
            )
        });

        if (response.ok){
            success();
        }else{
            fail();
        }

        if (load != null){
            load.classList.remove("inline-block");
        }
    };
}