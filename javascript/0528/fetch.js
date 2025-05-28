const API_URL = "https://dev.wenivops.co.kr/services/fastapi-crud/1/product";

fetch(API_URL)
    .then((response) => response.json())
    .then((json) => {
        const productList = document.getElementById("product-list1");
        json.forEach((product) => {
            const li = document.createElement("li");
            // console.log(product);
            li.textContent = `${product.productName}: ${product.price}`;
            productList.appendChild(li);
        });
    })
    .catch((error) => console.log(error));
