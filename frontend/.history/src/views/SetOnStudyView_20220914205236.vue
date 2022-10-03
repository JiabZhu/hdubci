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
        <div class="common-layout">
          <el-container>
            <el-aside width="50%">
              <el-form :model="experienceData" label-width="120px">

                <el-form-item label="准备时间">
                  <el-input v-model="experienceData.fixation_duration" style="width:200px;"/>
                </el-form-item>

                <el-form-item label="刺激呈现时间">
                  <el-input v-model="experienceData.pic_duration" style="width:200px;"/>
                </el-form-item>

                <el-form-item label="准备阶段图片">

                  <el-upload v-model:file-list="startImage" class="upload-demo" :auto-upload="false" multiple :limit="1"
                    :on-change="handleFixationChange">
                    <el-button type="primary">选择图像</el-button>
                  </el-upload>

                </el-form-item>

                <el-form-item label="目标图片">

                  <el-upload v-model:file-list="targetList" class="upload-demo" :auto-upload="false" multiple
                    ref="uploadFile" :on-Change="handleTargetChange" :show-file-list="false" :limit="10000000000">
                    <el-input v-model="checkStartlength" :autosize="{ minRows: 1, maxRows: 4 }" type="textarea"
                      style="width:520px" />
                  </el-upload>
                  <!-- <el-button @click="clearFiles">重置</el-button> -->
                </el-form-item>

                <el-form-item label="结束图片">

                  <el-upload v-model:file-list="endImage" class="upload-demo" :auto-upload="false" multiple :limit="1"
                    :on-Change="handleEndChange">
                    <el-button type="primary">选择图像</el-button>
                  </el-upload>

                </el-form-item>

                <el-form-item >
                  <el-button type="primary" @click="onSubmit">开始实验</el-button>
                </el-form-item>
              </el-form>
            </el-aside>
            <el-main>Main</el-main>
          </el-container>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, toRefs } from "vue";
import { useRouter, useRoute } from 'vue-router'
import { genFileId } from 'element-plus';
import { ElMessage, ElMessageBox } from 'element-plus'
import { setStudy } from '../request/api'
import type { UploadProps, UploadUserFile, UploadInstance, UploadRawFile } from 'element-plus'
import { OnExperience } from '../type/experience'

export default defineComponent({
  name: "SetStudy",
  setup() {
    const form = reactive(new OnExperience())

    const startImage = ref<UploadInstance>()
    const endImage = ref<UploadUserFile>()

    const targetList = ref<UploadUserFile[]>([])
    const nonTargetList = ref<UploadUserFile[]>([])

    const handleFixationChange: UploadProps['onChange'] = (file, fileLists) => {
      form.experienceData.fixation_pic = file.name;
    }
    const handleTargetChange: UploadProps['onChange'] = (file) => {
      form.experienceData.pic_list.push(file.name)
    }
    const handleEndChange: UploadProps['onChange'] = (file) => {
      form.experienceData.end_pic = file.name;
    }
    const onSubmit = () => {
      setStudy(form.experienceData).then(res => {
        console.log(res);
      })
    }
    return {
      ...toRefs(form),
      onSubmit,
      startImage,
      endImage,
      targetList,
      nonTargetList,
      handleFixationChange,
      handleTargetChange,
      handleEndChange
    }
  },

  methods: {

  },
  computed: {
    checkStartlength() {
      var name = ""
      if (this.targetList.length == 0) return undefined;
      else {
        for (let i = 0; i < this.targetList.length; i++)
          name += this.targetList[i].name + ' ';
        return name;
      }
    },
    checkEndLength() {
      var name = ""
      if (this.nonTargetList.length == 0) return undefined;
      else {
        for (let i = 0; i < this.nonTargetList.length; i++)
          name += this.nonTargetList[i].name + ' ';
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

