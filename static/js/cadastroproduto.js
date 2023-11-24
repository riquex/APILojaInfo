window.onload = function(){
    const image_input = document.getElementById("imagem");
    if (image_input instanceof HTMLInputElement){
        image_input.addEventListener("change", () => {
            const input_text = document.getElementById("image-text");
            if (input_text instanceof HTMLInputElement){
                input_text.value = image_input.value.replace(/^.*[\\/]/, '')
            }
        })
    }
}