<template>
    <div class="menus d-flex align-items-center">
        <div class="menu-img rounded-circle">
            <img class="img-fluid" :src="items.image" alt="">
        </div>
        <div class="text-wrap">
            <div class="row align-items-start">
                <div class="col-8">
                    <h4>${ items.nom.substring(0,38) }</h4>
                </div>
                <div class="col-4">
                    <h4 class="text-muted menu-price">${ items.prix }</h4>
                </div>
            </div>
            <p>${ items.ingredient.nom }</p>
        </div>
    </div>
</template>

<script>
    module.exports = {
        props: ['item','items'],
        delimiters: ["${", "}"], 
    }
</script>