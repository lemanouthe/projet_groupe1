<template>
    <div class="row mt-5">
        <div class="col-lg-5 col-md-6 align-self-center order-2 order-md-1 mt-4 mt-md-0">
            <img src="/static/img/salmon-zucchini.jpg" alt="" class="img-fluid shadow w-100">
        </div>
        <div class="col-lg-5 offset-lg-2 col-md-6 align-self-center order-1 order-md-2 py-5">
            <h2 class="special-number">02.</h2>
            <div class="dishes-text">
                {% for item in present %}
                {% if forloop.first %}
                <h3><span>Salmon</span><br> Zucchini</h3>
                <p class="pt-3">{{ item.text2 }}</p>
                {% endif %}
                {% endfor %}
                <h3 class="special-dishes-price">$12.00</h3>
                <a href="#" class="btn-primary mt-3">book a table <span><i class="fa fa-long-arrow-right"></i></span></a>
            </div>
        </div>
    </div>
</template>
<script>
    module.exports = {
        data: {
            
        },
    }
</script>