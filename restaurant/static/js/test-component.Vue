<template>
    <div class='test'> ${message} ${name}</div>
</template>

<script>
module.exports = {
    name:'test-compo',
    data: function() {
        return {
            name: 'steph'
        }
    },
    props:['message'],
    delimiters:["${","}"],
}
</script>

<style>
.test {
    background-color: rgba(150,46,24,0.7);
}
</style>