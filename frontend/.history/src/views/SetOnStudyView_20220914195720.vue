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
import { defineComponent, reactive, ref, toRefs } from "vue";
import { useRouter, useRoute } from 'vue-router'
import { genFileId } from 'element-plus';
import { ElMessage, ElMessageBox } from 'element-plus'
import { setStudy } from '../request/api'
import type { UploadProps, UploadUserFile, UploadInstance, UploadRawFile } from 'element-plus'
import { Experience } from '../type/experience'
export default defineComponent({
  name: "SetStudy",
  setup() {
    const form = reactive(new Experience())

    const startImage = ref<UploadInstance>()
    const endImage = ref<UploadUserFile>()

    const targetList = ref<UploadUserFile[]>([])
    const nonTargetList = ref<UploadUserFile[]>([])

    const handleFixationChange: UploadProps['onChange'] = (file,fileLists) => {
      form.experienceData.fixation_pic = file.name;
    }
    const handleTargetChange: UploadProps['onChange'] = (file) => {
      form.experienceData.target_pic_list.push(file.name)
    }
    const handleNonTargetChange: UploadProps['onChange'] = (file) => {
      form.experienceData.non_target_pic_list.push(file.name)
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
      handleNonTargetChange,
      handleEndChange
    }
  },
  // mounted() {
  //   //以下代码，有时候可能写法不同，可在控制台打印一层一层的找input，再给加webkitdirectory 属性
  //   this.$refs.uploadFile.$children[0].$refs.input.webkitdirectory = true;
  // },
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

