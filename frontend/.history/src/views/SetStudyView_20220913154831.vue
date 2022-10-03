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

        <el-form :model="form" label-width="120px"
          style="width:800px;position:absolute;left:50%;margin-left:-400px;margin-top:100px;">


          <el-form-item label="目标：非目标">

            <el-form :inline="true" :model="formInline" class="demo-form-inline">
              <el-form-item>
                <el-input v-model="formInline.user" />
              </el-form-item>
              <el-form-item label=":" style="margin-left:-20px;">
                <el-input v-model="formInline.user" />
              </el-form-item>
            </el-form>

          </el-form-item>


          <el-form-item label="实验次数">
            <el-input style="width:410px;" v-model="formInline.user" />
          </el-form-item>

          <el-form-item label="目标mack值">

            <el-form :inline="true" :model="formInline" class="demo-form-inline">
              <el-form-item>
                <el-input v-model="formInline.user" />
              </el-form-item>
              <el-form-item label="非目标mark值">
                <el-input v-model="formInline.user" />
              </el-form-item>
            </el-form>

          </el-form-item>

          <el-form-item label="准备时间">
            <el-input style="width:410px;" v-model="formInline.user" />
          </el-form-item>

          <el-form-item label="刺激呈现时间">
            <el-input style="width:410px;" v-model="formInline.user" />
          </el-form-item>

          <el-form-item label="准备阶段图片">
            <template>
              <div id="wrapper" align="center">
                <img id="logo" src="~@/assets/logo_efonmark.png" alt="electron-vue" align="center">
                <div align="center">
                  <h1> Welcome to EfonMark!</h1>
                </div>

                <div align="center">
                  <el-input id="input01" type="textarea" :autosize="{ minRows: 2, maxRows: 10}" placeholder="请选择文件"
                    v-model="textarea">
                  </el-input>
                </div>

                <div align="center">
                  <el-button type="primary" v-on:click="openFile()" round>选择文件</el-button>
                  <el-button type="primary" v-on:click="showRealPath()" round>显示路径</el-button>
                  <input type="file" name="filename" id="open" style="display:none" />
                </div>
              </div>
            </template>
          </el-form-item>

          <el-form-item label="Activity form">
            <el-input v-model="form.desc" type="textarea" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">Create</el-button>
            <el-button>Cancel</el-button>
          </el-form-item>
        </el-form>

      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, toRefs } from "vue";
import { useRouter, useRoute } from 'vue-router'
import type { UploadInstance } from 'element-plus';


export default defineComponent({
  name: "SetStudy",
  setup() {
    const form = reactive({
      name: '',
      region: '',
      date1: '',
      date2: '',
      delivery: false,
      type: [],
      resource: '',
      desc: '',
    })

    const formInline = reactive({
      user: '',
      region: '',
    })
    const onSubmit = () => {
      console.log('submit!')
    }

    const uploadRef = ref<UploadInstance>()

    const submitUpload = () => {
      console.log(uploadRef)
      uploadRef.value!.submit()
    }
    return { form, onSubmit, formInline, textarea: '', }
  },
  methods: {
    openFile: function () {
      document.getElementById('open').click()
    },
    showRealPath: function () {
      document.getElementById('input01').value = document.getElementById('open').files[0].path
    }
  }

});

</script>
<style lang="scss" scoped>
html {
  position: relative;
}

.el-header {
  height: 80px;

  .logo {
    height: 80px;
  }
}
</style>
