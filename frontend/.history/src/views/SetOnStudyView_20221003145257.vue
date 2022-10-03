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
              <div class="demo-image__preview" id="viewerjs">
                <img style="width: 100px; height: 100px;float:left;margin-left:10px;margin-top:10px"
                  v-for="url in imgUrl" :key="url" :src=url />
              </div>
            </el-main>
          </el-container>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, getCurrentInstance, onMounted, reactive, ref, toRefs, watch } from "vue";
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
import Viewer from "viewerjs";
import 'viewerjs/dist/viewer.css';

export default defineComponent({
  name: "SetStudy",
  setup() {
    var viewer: any
    onMounted(() => {
      var viewer = new Viewer(document.getElementById('viewerjs') as HTMLElement, {
        navbar: true,
        title: true,
        toolbar: {
          prev: true,
          next: true,
        },
        show:function(){
          viewer.update()
        }
      })
    })
    // const updateViewer = () => {
    //   const ViewerDom = document.getElementById('image');
    //   console.log(ViewerDom)
    //   if (viewer != null) {
    //     viewer.destroy()
    //   }
    //   viewer = null
    //   viewer = new Viewer(ViewerDom as HTMLElement, {
    //     inline: true,
    //     navbar: false,
    //     title: false,
    //     button: false,
    //     transition: true,
    //     viewed() {
    //       viewer.zoomTo(1);
    //     },
    //     show: function () {
    //       viewer.update();
    //     }

    //   });
    // }
    const form = reactive(new OnExperience())
    let check = ref(true)
    const startImage = ref<UploadInstance>()
    const endImage = ref<UploadUserFile>()
    const socket = io("ws://10.1.125.51:19782")
    const targetList = ref<UploadUserFile[]>([])
    const nonTargetList = ref<UploadUserFile[]>([])

    var imgUrl = ref<string[]>([])
    imgUrl.value.push("https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg")
    var srcList = ref<string[]>([])
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
      const base64ToUrl = (base64: any) => {
        const [type, data] = base64.split(',');
        const bytes = window.atob(data);
        const aryBuffer = new ArrayBuffer(bytes.length);
        new Uint8Array(aryBuffer).set(bytes.split('').map(v => v.charCodeAt(0)));
        return window.URL.createObjectURL(new Blob([aryBuffer], {
          type: type.match(/:(.*?);/)[1]
        }));
      }
      socket.on('connect', () => {
        console.log('connect: websocket 连接成功！')
      })
      //给被试看的
      socket.on('sti pic', (data) => {
        var t = JSON.parse(data)
        console.log(t.mark)
      });
      socket.on('predict res', (msg) => {
        var t = JSON.parse(msg)
        console.log(t.predict)
        var url = base64ToUrl(t.pic)
        console.log(url)
        if (t.predict == 1){
          imgUrl.value.push(url)
        }
      });

    })
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
      viewer
    }
  },
  watch: {
    imgUrl: {
      handler(newVal, oldVal) {
        console.log("-------")
        this.updateViewer()
      },
      deep: true,
    }
  },
  methods: {
    updateViewer() {
      let _this = this
      const ViewerDom = document.getElementById('viewerjs');
      console.log(ViewerDom)
      if (_this.viewer != null) {
        _this.viewer.destroy()
      }
      _this.viewer = null
      _this.viewer = new Viewer(ViewerDom as HTMLElement, {
        navbar: true,
        title: true,
        toolbar: {
          prev: true,
          next: true,
        },
        viewed() {
          _this.viewer.zoomTo(1);
        },
        show: function () {
          _this.viewer.update();
        }

      });
    },

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

