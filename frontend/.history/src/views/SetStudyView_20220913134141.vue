<template>
  <div class="home">
    <el-container>
      <el-header>
        <el-row :gutter="20">
          <el-col :span="4"><img src="../assets/BCI_title.jpg" class="logo" /></el-col>
        </el-row>
      </el-header>
      <el-divider />
      <el-main>


      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { Devices, device } from "../type/device"
import { defineComponent, reactive, ref, toRefs } from "vue";
import { useRouter, useRoute } from 'vue-router'
import { addDevice } from "@/request/api";

export default defineComponent({
  name: "AddDeviceView",
  setup() {
    const forms = reactive(new Devices());
    const router = useRouter()
    const options = [
      {
        value: 'neuroscan',
        label: 'NeuroScan',
      },
      {
        value: 'eyetracker',
        label: 'EyeTracker',
      },
    ]

    const onSubmit = (form: any) => {
      addDevice(form).then(res => {
        console.log(res);
      })
    };
    const resetForm=(item:number)=>{
      forms.list[item].type='';
      forms.list[item].ip='';
      forms.list[item].port=undefined;
    }
    const gotoSetStudy=()=>{
      router.push()
    }
    return { onSubmit, options, ...toRefs(forms),resetForm}
  },
  components: {},
});
</script>
<style lang="scss" scoped>
html {
  position: relative;
}

.el-carousel__item h3 {
  display: flex;
  color: #fff;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #fff;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #fff;
}

.el-main {

  .deviceName {
    width: 300px
  }

  .ip {
    width: 300px;
  }
}

.el-header {
  height: 80px;

  .logo {
    height: 80px;
  }
}
</style>
