<template>
  <div class="home">
    <el-container>
      <el-header>
        <el-row :gutter="20">
          <el-col :span="4"><img src="../assets/BCI_title.jpg" class="logo" /></el-col>
        </el-row>
      </el-header>
      <el-container>
        <el-main>
          
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref } from "vue";
import { useRouter, useRoute } from 'vue-router'
import {rsvpOffline} from '../request/api'

export default defineComponent({
  name: "HomeView",
  setup() {
    const router=useRouter()
    const dialogTableVisible = ref(false)
    const dialogFormVisible = ref(false)
    const formLabelWidth = '140px'
    const form = reactive({
      region: '',
    })
    const submitForm=(FormEl:any)=>{
//       离线数据采集
// 模型在线训练
// 离线模型测试
      if(FormEl.region === "离线数据采集"){
        rsvpOffline().then(res=>{
          console.log(res);
          router.push('/adddevice');
        })
      }
    }
    return { form, dialogFormVisible, formLabelWidth,submitForm}
  },
  components: {},
});
</script>
<style lang="scss" scoped>
.el-button--text {
  margin-right: 15px;
}

.el-select {
  width: 300px;
}

.el-input {
  width: 300px;
}

.dialog-footer button:first-child {
  margin-right: 10px;
}

html {
  position: relative;
}

.el-header {
  height: 80px;

  .logo {
    height: 80px;
  }
}

.neuro_box {
  width: 600px;
  overflow: hidden;
}

.common-layout {
  position: absolute;
  left: 15%;
  top: 20%;
}

.neuro1 {
  width: 100%;
  height: 700px;
}

.gtec {
  width: 100%;
  height: 300px;
}

.emotive {
  width: 100%;
  height: 300px;
}

.neuro2 {
  width: 600px;
}

.el-card {
  --el-card-padding: 0px;
}
</style>
