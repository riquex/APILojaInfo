const toBase64 = file => new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result);
    reader.onerror = reject;
    reader.readAsDataURL(file);
});

window.onload = function(){
    const submit = document.getElementById("submit");
    const image_preview = document.getElementById("previewimage");
    const image_input = document.getElementById("imagem");

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

        const snackbar_type = (response.status === 200) ? "success" : "fail";
        const success = document.querySelector(`.snackbar.${snackbar_type}`);
        if (success instanceof HTMLDivElement){
            success.classList.add("show");
            setTimeout(()=>{success.classList.remove("show")}, 3000);
        }

        if (load != null){
            load.classList.remove("inline-block");
        }
    };
}