<template>
  <div class="home">
    asd
  </div>
</template>
<script lang="ts" setup>
  import { onBeforeMount } from 'vue'
  import { useStore } from 'vuex'

  const store = useStore()
  const initSocket = () => {
    store.commit('initWebsocket')
  }
  
  onBeforeMount(() => {
    initSocket()
  })
</script>
<style lang="scss" scoped>

</style>
