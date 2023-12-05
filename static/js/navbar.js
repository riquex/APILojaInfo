window.onload = () => {
    const drop_down = document.getElementById("drop-down");

    window.onclick = (event) => {
        if (event instanceof Event){
            const target = event.target;
            if(target instanceof HTMLElement){
                if(target.matches('.drop-down-link, .hambuger-lines, .line, .dropdown-content')){
                    drop_down.classList.add("show");
                } else {
                    drop_down.classList.remove("show");
                }
            }
        }
    };
};