<template>
  <router-view/>
</template>

<style lang="scss">
*{
  padding: 0px;
  margin: 0px;
}
html,body,#app{
  width: 100%;
  height: 100%;
}
</style>
<!-- <script lang="ts" setup>
  import { onBeforeMount } from 'vue'
  import { useStore } from 'vuex'
  /**
   * 仓库
   */
  const store = useStore()
  //websocket初始化
  const initSocket = () => {
    store.commit('initWebsocket')
  }
  
  onBeforeMount(() => {
    //console.log('2.组件挂载页面之前执行----onBeforeMount')
    initSocket()
  })
</script> -->