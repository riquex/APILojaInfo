window.onload = () => {
    window.onclick = (event) => {
        const drop_down = document.getElementById("drop-down");
        if (event instanceof Event){
            if(event.target == drop_down){
                drop_down.classList.add("show");
            } else {
                drop_down.classList.remove("show");
            }
        }
    };
};