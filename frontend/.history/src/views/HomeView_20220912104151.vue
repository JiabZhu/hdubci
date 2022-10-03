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
          <div class="common-layout">
            <el-container>
              <el-aside width="600px">
                <el-card shadow="always" @click="dialogFormVisible = true" style="cursor: pointer;">

                  <el-dialog v-model="dialogFormVisible" title="RSVP">
                    <el-form :model="form">
                      <el-form-item label="实验类型" :label-width="formLabelWidth">
                        <el-select v-model="form.region" placeholder="请选择你的实验类型">
                          <el-option label="离线数据采集" value="离线数据采集" />
                          <el-option label="模型在线训练" value="模型在线训练" />
                          <el-option label="离线模型测试" value="离线模型测试" />
                        </el-select>
                      </el-form-item>
                    </el-form>
                    <template #footer>
                      <span class="dialog-footer">
                        <el-button @click="dialogFormVisible = false">取消</el-button>
                        <el-button type="primary" @click="submitForm(form)">确定</el-button>
                      </span>
                    </template>
                  </el-dialog>

                  <img src="../assets/neuro1.jpg" class="neuro1" />
                </el-card>
              </el-aside>
              <el-container>
                <el-header style="height:380px;">
                  <el-card shadow="always" class="neuro_box">
                    <img src="../assets/neuro2.png" class="neuro2" />
                  </el-card>
                </el-header>
                <el-main style="overflow:hidden">
                  <el-aside width="300px" style="float:left">
                    <el-card shadow="always">
                      <img src="../assets/gtec.jpg" class="gtec" />
                    </el-card>
                  </el-aside>
                  <el-aside width="300px" style="float: right;">
                    <el-card shadow="always">
                      <img src="../assets/emotive.png" class="emotive" />
                    </el-card>
                  </el-aside>
                </el-main>
              </el-container>
            </el-container>
          </div>
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
          // console.log(res);
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
  left: 20%;
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
