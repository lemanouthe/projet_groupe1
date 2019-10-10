<template>
    <div class="col-lg-4 menu-wrap">
        <div class="heading-menu">
            <h3 class="text-center mb-5">${ item.nom.substring(0,38) }</h3>
        </div>
        <menu-compo
            v-for="plt in item.category_client"
            v-bind:items="plt"
            v-bind:key="plt.id"
        ></menu-compo>
    </div>
</template>
<script>
    module.exports = {
        props: ['item','cat'],
        components: {
            'menu-compo': httpVueLoader('/static/components/menu.vue'),
        },
        delimiters: ["${", "}"], 

    }
</script>