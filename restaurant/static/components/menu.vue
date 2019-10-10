<template>
    <div class="menus d-flex align-items-center">
        <div class="menu-img rounded-circle">
            <img class="img-fluid" src="/static/img/breakfast-1.jpg" alt="">
        </div>
        <div class="text-wrap">
            <div class="row align-items-start">
                <div class="col-8">
                    <h4>Egg Sandwich</h4>
                </div>
                <div class="col-4">
                    <h4 class="text-muted menu-price">$30</h4>
                </div>
            </div>
            <p>Meat Ball, Mie</p>
        </div>
    </div>
</template>

<script>
    module.exports = {
        props: ['item'],
    }
</script>