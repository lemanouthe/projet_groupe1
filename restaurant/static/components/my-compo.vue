<template>
    <div class="col-lg-4 menu-wrap">
        <div class="heading-menu">
            <h3 class="text-center mb-5">Breakfast</h3>
        </div>
        <menu-compo></menu-compo>
        <menu-compo></menu-compo>
        <menu-compo></menu-compo>
    </div>
</template>
<script>
    module.exports = {
       components: {
            'menu-compo': httpVueLoader('/static/components/menu.vue'),
        },
    }
</script>