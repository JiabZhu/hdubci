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
        <el-form :model="form" label-width="120px">
          <el-form-item label="设备类型">

            <el-select v-model="form.type" class="m-2 deviceName" placeholder="Select">
              <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
            </el-select>

          </el-form-item>

          <el-form-item label="IP">
            <el-input v-model="form.ip" class="ip" />
          </el-form-item>
          <el-form-item label="端口号">
            <el-input v-model="form.port" class="ip" />
          </el-form-item>

          <el-form-item style="float:left;">
            <span>请求成功</span>
            <el-button type="primary" @click="onSubmit(form)" style="margin-left:100px">连接</el-button>
          </el-form-item>
        </el-form>

        <el-carousel indicator-position="outside">
          <el-carousel-item v-for="item in 4" :key="item">
            <h3 text="2xl" justify="center">{{ item }}</h3>
          </el-carousel-item>
        </el-carousel>


      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref } from "vue";
import { useRouter, useRoute } from 'vue-router'
import { addDevice } from "@/request/api";

export default defineComponent({
  name: "HomeView",
  setup() {
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
    const form = reactive({
      type: '',
      ip: '',
      port: null
    });
    const onSubmit = (form: any) => {
      addDevice(form).then(res => {
        console.log(res);
      })
    }
    return { form, onSubmit, options }
  },
  components: {},
});
</script>
<style lang="scss" scoped>
html {
  position: relative;
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

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
