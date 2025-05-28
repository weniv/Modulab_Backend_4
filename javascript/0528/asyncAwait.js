async function fetchProducts() {
    try {
        const response = await fetch(API_URL);
        const json = await response.json();
        // console.log("async-await: ", json);
        const productList = document.getElementById("product-list2");
        json.forEach((product) => {
            const li = document.createElement("li");
            // console.log(product);
            li.textContent = `${product.productName}: ${product.price}`;
            productList.appendChild(li);
        });
    } catch (error) {
        console.log(error);
    }
}

fetchProducts();
