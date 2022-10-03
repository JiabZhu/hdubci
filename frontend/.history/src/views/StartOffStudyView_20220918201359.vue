<template>
  <div class="home">
    asd
  </div>
</template>

<!-- <script lang="ts">
import { defineComponent, reactive, ref } from "vue";
import { useRouter } from 'vue-router'
import { rsvpOffline, rsvpOnline } from '../request/api'
import { useStore } from 'vuex'

export default defineComponent({
  name: "HomeView",
  setup() {
    const router = useRouter()

    return {}
  },
  created() {
    //初始化websocket
    this.initSocket()
  },
  methods: {
    //websocket初始化
    initSocket() {
      this.$store.commit('initWebsocket')
    }
  },
  components: {},
});
</script> -->
<script lang="ts" setup>
  import { onBeforeMount } from 'vue'
  import { useStore } from 'vuex'
  // import {}
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
</script>
<style lang="scss" scoped>

</style>
