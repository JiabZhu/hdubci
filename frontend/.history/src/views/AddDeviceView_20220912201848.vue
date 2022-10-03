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


        <el-carousel :autoplay="false" indicator-position="outside" style="width:600px;margin:0px auto">
          <el-carousel-item v-for="item in 6" :key="item">

            <el-form :model="list[item]" label-width="120px" style="margin-left:50px;margin-top:70px">
              <el-form-item label="设备类型">

                <el-select v-model="list[item].type" class="m-2 deviceName" placeholder="Select">
                  <el-option v-for="x in options" :key="x.value" :label="x.label" :value="x.value" />
                </el-select>

              </el-form-item>

              <el-form-item label="IP">
                <el-input v-model="list[item].ip" class="ip" />
              </el-form-item>
              <el-form-item label="端口号">
                <el-input v-model="list[item].port" class="ip" />
              </el-form-item>

              <el-form-item style="float:left;">
                <span>请求成功</span>
                <el-button type="primary" @click="onSubmit(list[item])" style="margin-left:100px">连接</el-button>
              </el-form-item>
            </el-form>
          </el-carousel-item>
        </el-carousel>

      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { Devices ,device} from "../type/device"
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
    }
    return { onSubmit, options, ...toRefs(forms) }
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
