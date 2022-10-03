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

        <h2 style="width:20px;float:right;margin-right:10%;margin-top:5%">离线采集</h2>
        <el-form :model="experienceData" label-width="120px"
          style="width:800px;position:absolute;left:50%;margin-left:-400px;margin-top:10px;">


          <el-form-item label="目标：非目标">

            <el-form :inline="true" :model="experienceData" class="demo-form-inline">
              <el-form-item>
                <el-input v-model.number="experienceData.target_proportion" />
              </el-form-item>
              <el-form-item label=":" style="margin-left:-20px;">
                <el-input v-model.number="experienceData.non_target_proportion" />
              </el-form-item>
            </el-form>

          </el-form-item>


          <el-form-item label="实验次数">
            <el-input style="width:410px;" v-model.number="experienceData.trial_num" />
          </el-form-item>

          <el-form-item label="目标mack值">

            <el-form :inline="true" :model="experienceData" class="demo-form-inline">
              <el-form-item>
                <el-input v-model.number="experienceData.target_mark" />
              </el-form-item>
              <el-form-item label="非目标mark值">
                <el-input v-model.number="experienceData.non_target_mark" />
              </el-form-item>
            </el-form>

          </el-form-item>

          <el-form-item label="准备时间">
            <el-input style="width:410px;" v-model.number="experienceData.fixation_duration" />
          </el-form-item>

          <el-form-item label="刺激呈现时间">
            <el-input style="width:410px;" v-model.number="experienceData.pic_duration" />
          </el-form-item>

          <el-form-item label="准备阶段图片">

            <el-upload action="" v-model:file-list="startImage" class="upload-demo" :auto-upload="false" multiple
              :limit="1" :on-change="uploadFixation">
              <el-button type="primary">选择图像</el-button>
            </el-upload>

          </el-form-item>

          <el-form-item label="目标图片">

            <el-upload v-model:file-list="targetList" class="upload-demo" :auto-upload="false" multiple ref="uploadFile"
              :on-Change="uploadTargetPic" :show-file-list="false" :limit="10000000000">
              <el-input v-model="checkStartlength" :autosize="{ minRows: 1, maxRows: 4 }" type="textarea"
                style="width:520px" />
            </el-upload>
            <!-- <el-button @click="clearFiles">重置</el-button> -->
          </el-form-item>

          <el-form-item label="非目标图片">

            <el-upload v-model:file-list="nonTargetList" class="upload-demo" :auto-upload="false" multiple
              :on-Change="uploadNonTargetPic" :show-file-list="false" :limit="10000000000">
              <el-input v-model="checkEndLength" :autosize="{ minRows: 1, maxRows: 4 }" type="textarea"
                style="width:520px" />
            </el-upload>

          </el-form-item>

          <el-form-item label="结束图片">

            <el-upload v-model:file-list="endImage" class="upload-demo" :auto-upload="false" multiple :limit="1"
              :on-Change="uploadEnd">
              <el-button type="primary">选择图像</el-button>
            </el-upload>

          </el-form-item>

          <el-form-item style="margin-left: 20%;">
            <el-button type="primary" @click="onSubmit">提交实验</el-button>
          </el-form-item>

          <el-form-item style="margin-left: 20%;">
            <el-button type="primary" :disabled="check" @click="startStudy">开始实验</el-button>
            <span style="margin-left:5px">{{time}}s后开始实验</span>
          </el-form-item>

        </el-form>
        <img :src=url>

      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, toRefs } from "vue";
import { useRouter, useRoute } from 'vue-router'
import { genFileId } from 'element-plus';
import { ElMessage, ElMessageBox } from 'element-plus'
import { setOffStudy, readyOffStudy, startOffStudy } from '../request/api'
import type { UploadProps, UploadUserFile, UploadInstance, UploadRawFile } from 'element-plus'
import { OffExperience } from '../type/experience'
import { takeRightWhile } from "lodash";
export default defineComponent({
  name: "SetStudy",
  setup() {
    const form = reactive(new OffExperience())
    const router = useRouter()
    let check = ref(true)
    let url = ref("")
    let time = ref(5)
    const startImage = ref<UploadInstance>()
    const endImage = ref<UploadUserFile>()

    const targetList = ref<UploadUserFile[]>([])
    const nonTargetList = ref<UploadUserFile[]>([])

    const handleFixationChange: UploadProps['onChange'] = (file, fileLists) => {
      form.experienceData.fixation_pic = file.name;

    }
    const handleTargetChange: UploadProps['onChange'] = (file) => {
      form.experienceData.target_pic_list.push(file.name);
      // console.log(file.raw);

    }
    const handleNonTargetChange: UploadProps['onChange'] = (file) => {
      form.experienceData.non_target_pic_list.push(file.name)
    }
    const handleEndChange: UploadProps['onChange'] = (file) => {
      form.experienceData.end_pic = file.name;
    }
    const onSubmit = () => {
      check.value = false;
      console.log(form.experienceData);
      setOffStudy(form.experienceData).then(res => {
        console.log(res);
      });
    }
    
    const countDown = () =>{
      time.value--;
    }

    const startStudy = () => {
      readyOffStudy().then(res => {
        console.log(res);
      });

      setInterval(countDown,1000)

      // setTimeout(() => {
      //   startOffStudy().then(res => {
      //     console.log(res);
      //   })
        
      //   window.open('/startOffStudy.html')
      // }, 5000);
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
      handleEndChange,
      check,
      startStudy,
      url,
      time,
    }
  },
  methods: {
    uploadFixation(file: any, fileList: any) {
      // let base64Str = await this.getBase64(file.file);
      //   console.log(base64Str);
      // this.imgString = base64Str.split(',');
      // console.log(this.imgString);
      this.getBase64(file.raw).then(res => {
        // this.url=res as string;
        // console.log(res);
        this.experienceData.fixation_pic = res as string;
      })
    },

    uploadTargetPic(file: any) {
      this.getBase64(file.raw).then(res => {
        this.experienceData.target_pic_list.push(res as string)
      })
    },

    uploadNonTargetPic(file: any) {
      this.getBase64(file.raw).then(res => {
        this.experienceData.non_target_pic_list.push(res as string)
      })
    },

    uploadEnd(file: any) {
      this.getBase64(file.raw).then(res => {
        this.experienceData.end_pic = res as string
      })
    },
    getBase64(file: any) {
      return new Promise(function (resolve, reject) {
        let reader = new FileReader();
        let imgResult = "";
        reader.readAsDataURL(file);
        reader.onload = function () {
          imgResult = reader.result as string;
        };
        reader.onerror = function (error) {
          reject(error);
        };
        reader.onloadend = function () {
          resolve(imgResult);
        };
      });
    },
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
    },
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

