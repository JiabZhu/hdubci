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

            <el-upload ref="uploadStart" class="upload-demo"
              :limit="1" :on-exceed="handleExceedStart"
              :auto-upload="false">
              <template #trigger>
                <el-button type="primary">选择</el-button>
              </template>
            </el-upload>

          </el-form-item>

          <el-form-item label="目标图片">

            <el-upload v-model:file-list="fileList" class="upload-demo" :auto-upload="false" multiple
              :show-file-list="false" :limit="10000000000">
              <el-input v-model="checklength" :autosize="{ minRows: 2, maxRows: 4 }" type="textarea"
                style="width:520px" />
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
import { genFileId } from 'element-plus';

import type { UploadProps, UploadUserFile, UploadInstance, UploadRawFile } from 'element-plus'

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
    const uploadStart = ref<UploadInstance>()
    const handleExceedStart: UploadProps['onExceed'] = (files) => {
      uploadStart.value!.clearFiles()
      const file = files[0] as UploadRawFile
      file.uid = genFileId()
      uploadStart.value!.handleStart(file)
    }
    const fileList = ref<UploadUserFile[]>([])

    return { form, onSubmit, formInline, fileList ,handleExceedStart, uploadStart}
  },
  computed: {
    checklength() {
      var name = ""
      if (this.fileList.length == 0) return undefined;
      else {
        for (let i = 0; i < this.fileList.length; i++)
          name += this.fileList[i].name + ' ';
        return name;
      }
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

