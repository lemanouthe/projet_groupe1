<template>
    <div class="col-lg-4 menu-wrap">
        <div class="heading-menu">
            <h3 class="text-center mb-5">${ item.categorie.nom.substring(0,38) }</h3>
        </div>
        <menu-compo></menu-compo>
    </div>
</template>
<script>
    module.exports = {
        props: ['item'],
        components: {
            'menu-compo': httpVueLoader('/static/components/menu.vue'),
        },
        delimiters: ["${", "}"],
    }
</script>