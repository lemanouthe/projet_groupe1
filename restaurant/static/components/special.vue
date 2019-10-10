<template>
    <div class="col-md-4">
        <div class="team-card mb-5">
            <img class="img-fluid" :src="items.photo" alt="">
            <div class="team-desc">
                <h4 class="mb-0">${ items.nom.substring(0,20) }</h4>
                <p class="mb-1">${ items.poste.nom.substring(0,10) }</p>
                <ul class="list-inline mb-0 team-social-links">
                    <li class="list-inline-item">
                        <a href="${ items.social.lien }">
                            <i class="${ items.social.name }"></i>
                        </a>
                    </li>
                    
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    module.exports = {
       props: ['items'],
       delimiters: ["${", "}"],
    }
</script>