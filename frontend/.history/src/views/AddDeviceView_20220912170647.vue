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

            <el-select v-model="form.name" class="m-2 deviceName" placeholder="Select">
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
            <el-button type="primary" @click="onSubmit(form)" style="margin-left:200px">连接</el-button>
          </el-form-item>
        </el-form>
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
      name: '',
      ip: '',
      port: '',
    });
    const onSubmit = (form:any) => {
      addDevice(form).then(res=>{
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
  --el-main-padding: 100px 500px;

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
