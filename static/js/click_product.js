/**
 * 
 * @param {Element} element 
 * @param {string} className 
 * @returns {Element | null}
 */
const getHighElementByClass = (element, className) => {
    if (element instanceof Element){
        if(element.classList.contains(className)){
            return element;
        }return getHighElementByClass(element.parentElement, className);
    }
    return null;
};

window.onload = () => {
    window.onclick = (event) => {
        if (event instanceof Event){
            const target = event.target;
            if (target instanceof Element){
                const card = getHighElementByClass(target, 'card')
                if (card != null){
                    window.location.replace(`/produto/${card.id}`)
                }
            }
        }
    };
};