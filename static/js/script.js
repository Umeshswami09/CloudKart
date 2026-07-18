console.log("script.js loaded");

const searchInput = document.getElementById("search-input");
const searchResults = document.getElementById("search-results");

console.log(searchInput);
console.log(searchResults);

if (searchInput) {

    searchInput.addEventListener("keyup", function () {

        let query = this.value.trim();

        console.log("Typing:", query);

        if (query.length === 0) {

            searchResults.innerHTML = "";
            return;

        }

        fetch(`/search/?q=${query}`)

            .then(response => response.json())

            .then(data => {

                console.log("DATA:", data);

                searchResults.innerHTML = "";

                data.forEach(product => {

                    searchResults.innerHTML += `
                        <a href="/product/${product.id}/" class="search-item">
                            <img src="${product.image}" width="45">
                            <div>
                                <strong>${product.name}</strong><br>
                                ₹${product.price}
                            </div>
                        </a>
                    `;

                });

            })

            .catch(error => {

                console.log(error);

            });

    });

}