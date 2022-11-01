
const accordionHeader = document.querySelectorAll(".accordion-header");
accordionHeader.forEach((header) => {
    header.addEventListener("click", function () {
        const accordionContent = header.parentElement.querySelector(".accordion-content");
        const allAccordionContent = document.querySelectorAll('.accordion-content');
        let accordionMaxHeight = accordionContent.style.maxHeight;

        if (accordionMaxHeight == "0px" || accordionMaxHeight.length == 0) {
            allAccordionContent.forEach(((content) => {
                content.style.maxHeight = `0px`;
            }))
            accordionContent.style.maxHeight = `${accordionContent.scrollHeight + 32}px`;
            header.querySelector(".fas").classList.remove("fa-plus");
            header.querySelector(".fas").classList.add("fa-minus");
        } else {
            accordionContent.style.maxHeight = `0px`;
            header.querySelector(".fas").classList.add("fa-plus");
            header.querySelector(".fas").classList.remove("fa-minus");
        }
    });
});