<template>
  <div class="home">
    asd
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref } from "vue";
import { useRouter } from 'vue-router'
import { rsvpOffline, rsvpOnline } from '../request/api'

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
  }
  components: {},
});
</script>
<style lang="scss" scoped>

</style>
