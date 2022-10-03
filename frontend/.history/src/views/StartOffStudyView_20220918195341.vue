<template>
  <div class="home">
    
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
  components: {},
});
</script>
<style lang="scss" scoped>

</style>
