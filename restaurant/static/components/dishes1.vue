<template>
    <div class="row mt-5">
        <div class="col-lg-5 col-md-6 align-self-center py-5">
            <h2 class="special-number">01.</h2>
            <div class="dishes-text">
                {% for item in present %}
                {% if forloop.first %}
                <h3><span>Beef</span><br> Steak Sauce</h3>
                <p class="pt-3">{{ item.text1 }}</p>
                {% endif %}
                {% endfor %}
                <h3 class="special-dishes-price">$15.00</h3>
                <a href="#" class="btn-primary mt-3">book a table</a>
            </div>
        </div>
        <div class="col-lg-5 offset-lg-2 col-md-6 align-self-center mt-4 mt-md-0">
            <img src="/static/img/steak.jpg" alt="" class="img-fluid shadow w-100">
        </div>
    </div>
    <dishes2-compo></dishes2-compo>
</template>
<script>
    module.exports = {
        data: {
            
        },
       components: {
            'dishes2-compo': httpVueLoader('/static/components/dishes2.vue'),
        },
        
    }
</script>