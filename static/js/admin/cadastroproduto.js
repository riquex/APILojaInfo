window.onload = function(){
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
}