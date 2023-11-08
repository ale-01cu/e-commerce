export function HiddenSectionProduct() {
    const sectionProduct = document.getElementById("section-product");
    sectionProduct.classList.add("hidden");


    const containerUserCart = document.getElementById("container-usercart");
    containerUserCart.classList.remove("hidden");
}

export function HiddenUserCard() {
    const containerUserCart = document.getElementById("container-usercart");
    containerUserCart.classList.add("hidden");

    const sectionProduct = document.getElementById("section-product");
    sectionProduct.classList.remove("hidden");
}