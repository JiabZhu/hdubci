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

            <el-upload v-model:file-list="fileList" class="upload-demo"
              action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15" :auto-upload="false" multiple :show-file-list="false"
              :on-preview="handlePreview" :on-remove="handleRemove" :before-remove="beforeRemove" :limit="10000000000"
              :on-exceed="handleExceed">
              <el-button type="primary">Click to upload</el-button>
              <el-input v-model="fileList" autosize type="textarea" />
            </el-upload>

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
import { ElMessage, ElMessageBox } from 'element-plus'

import type { UploadProps, UploadUserFile } from 'element-plus'

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

    const fileList = ref<UploadUserFile[]>([

    ])
    
    const handleRemove: UploadProps['onRemove'] = (file, uploadFiles) => {
      console.log(file, uploadFiles)
    }

    const handlePreview: UploadProps['onPreview'] = (uploadFile) => {
      console.log(uploadFile)
    }

    const handleExceed: UploadProps['onExceed'] = (files, uploadFiles) => {
      ElMessage.warning(
        `The limit is 3, you selected ${files.length} files this time, add up to ${files.length + uploadFiles.length
        } totally`
      )
    }

    const beforeRemove: UploadProps['beforeRemove'] = (uploadFile, uploadFiles) => {
      return ElMessageBox.confirm(
        `Cancel the transfert of ${uploadFile.name} ?`
      ).then(
        () => true,
        () => false
      )
    }
    return { form, onSubmit, formInline, fileList, handleRemove, handlePreview, handleExceed, beforeRemove }
  },

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
