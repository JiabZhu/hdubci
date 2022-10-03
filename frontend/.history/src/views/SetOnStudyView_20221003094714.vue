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
            <el-aside width="40%" style="margin:5%">
              <el-form :model="experienceData" label-width="120px">

                <el-form-item label="准备时间">
                  <el-input v-model.number="experienceData.fixation_duration" style="width:200px;" />
                </el-form-item>

                <el-form-item label="刺激呈现时间">
                  <el-input v-model.number="experienceData.pic_duration" style="width:200px;" />
                </el-form-item>

                <el-form-item label="准备阶段图片">

                  <el-upload v-model:file-list="startImage" class="upload-demo" :auto-upload="false" multiple :limit="1"
                    :on-change="uploadFixation">
                    <el-button type="primary">选择图像</el-button>
                  </el-upload>

                </el-form-item>

                <el-form-item label="目标图片">

                  <el-upload v-model:file-list="targetList" class="upload-demo" :auto-upload="false" multiple
                    ref="uploadFile" :on-Change="uploadTargetPic" :show-file-list="false" :limit="10000000000">
                    <el-input v-model="checkStartlength" :autosize="{ minRows: 1, maxRows: 4 }" type="textarea"
                      style="width:400px" />
                  </el-upload>
                  <!-- <el-button @click="clearFiles">重置</el-button> -->
                </el-form-item>

                <el-form-item label="结束图片">

                  <el-upload v-model:file-list="endImage" class="upload-demo" :auto-upload="false" multiple :limit="1"
                    :on-Change="uploadEnd">
                    <el-button type="primary">选择图像</el-button>
                  </el-upload>

                </el-form-item>

                <el-form-item label="时间窗口">
                  <el-input v-model.number="experienceData.time_window" style="width:200px;" />
                </el-form-item>

                <el-form-item>
                  <el-button type="primary" @click="onSubmit">提交实验</el-button>
                </el-form-item>

                <el-form-item style="margin-left: 20%;">
                  <el-button type="primary" :disabled="check" @click="startStudy">开始实验</el-button>
                  <!-- <span>{{num}}</span> -->
                </el-form-item>

              </el-form>
            </el-aside>
            <el-main>
              <!-- <div class="demo-image__preview" style="width:100px;height:100px;float:left;margin-left:10px;margin-top:10px" v-for="url in imgUrl"
                :key="url" @click="inputUrl(url)">
                <el-image style="width: 100px; height: 100px" :src=url fit="fill" :preview-src-list="srcList"/>
              </div> -->
              <div class="demo-image__preview" v-for="url in imgUrl" :key="url">
    <el-image
      style="width: 100px; height: 100px"
      :src=url
      :preview-src-list="srcList"
      :initial-index="4"
      fit="cover"
    />
  </div>
            </el-main>
          </el-container>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, getCurrentInstance, onMounted, reactive, ref, toRefs } from "vue";
import { useRouter, useRoute } from 'vue-router'
import { genFileId } from 'element-plus';
import { ElMessage, ElMessageBox } from 'element-plus'
import { setOnStudy } from '../request/api'
import { setOffStudy, readyOffStudy, startOffStudy } from '../request/api'
import type { UploadProps, UploadUserFile, UploadInstance, UploadRawFile } from 'element-plus'
import { OnExperience } from '../type/experience'
import { onBeforeMount } from 'vue'
import { useStore } from 'vuex'
import io from 'socket.io-client'

export default defineComponent({
  name: "SetStudy",
  setup() {
    const form = reactive(new OnExperience())
    let check = ref(true)
    const startImage = ref<UploadInstance>()
    const endImage = ref<UploadUserFile>()
    const socket = io("ws://10.1.125.51:19782")
    const targetList = ref<UploadUserFile[]>([])
    const nonTargetList = ref<UploadUserFile[]>([])

    var imgUrl = ref<string[]>([])
    imgUrl.value.push("https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg")
var srcList = [
  'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg',
  'https://fuss10.elemecdn.com/1/34/19aa98b1fcb2781c4fba33d850549jpeg.jpeg',
  'https://fuss10.elemecdn.com/0/6f/e35ff375812e6b0020b6b4e8f9583jpeg.jpeg',
  'https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg',
  'https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg',
  'https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
  'https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg',
]

    const barrageArr = ref<any>([])
    const onSubmit = () => {
      check.value = false;
      setOnStudy(form.experienceData).then(res => {
        console.log(res);
      });
      // window.open('/startOffStudy.html')
    }
    const startStudy = () => {
      readyOffStudy().then(res => {
        console.log(res);
      });
      setTimeout(() => {
        startOffStudy().then(res => {
          console.log(res);
        });
      }, 5000);
    }
    onMounted(() => {
      socket.on('connect', () => {
        console.log('connect: websocket 连接成功！')
      })
      //给被试看的
      socket.on('sti pic', (data) => {
        var t = JSON.parse(data)
        console.log(t.mark)
      });
      socket.on('predict res', (msg) => {
        //    console.log(msg)
        var t = JSON.parse(msg)
        console.log(t.predict)
        if (t.predict == 1) imgUrl.value.push(t.pic)
      });

    })
    const inputUrl = (url: any) => {
      srcList=[]
      srcList.push(url)
      console.log(srcList)
    }
    return {
      ...toRefs(form),
      onSubmit,
      startImage,
      endImage,
      targetList,
      nonTargetList,
      check,
      startStudy,
      htmlSrc: '/startOffStudy.html',
      imgUrl,
      srcList,
    }
  },
  methods: {
    uploadFixation(file: any, fileList: any) {
      this.getBase64(file.raw).then(res => {
        this.experienceData.fixation_pic = res as string;
      })
    },

    uploadTargetPic(file: any) {
      this.getBase64(file.raw).then(res => {
        this.experienceData.pic_list.push(res as string)
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
    // iframeMethods(){
    //   this.$refs.iframe.contentWindow.triggerByVue('通过Vue触发iframe中的方法');
    // },
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

.wrap {
  width: 100%;
  height: 500px;
  display: none;
}
</style>

