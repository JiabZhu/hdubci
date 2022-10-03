<template>
    <div class="home">
        <el-container>
            <el-header>
                <el-row :gutter="20">
                    <el-col :span="4"><img src="../assets/BCI_title.jpg" class="logo" /></el-col>
                </el-row>
            </el-header>
            <el-divider />
            <el-container>
                <el-aside width="400px" style="margin-left:20px">
                    <div class="common-layout">
                        <el-container>
                            <el-header style="height:200px">
                                <h2 style="margin-top:20px">实验设置</h2>
                                <el-form :model="experienceData" label-width="120px" style="margin-top:20px">
                                    <el-form-item label="刺激呈现时间">
                                        <el-input v-model="experienceData.pic_duration" style="width:200px;" />
                                    </el-form-item>
                                    <el-form-item label="时间窗口">
                                        <el-input v-model="experienceData.time_window" style="width:200px;" />
                                    </el-form-item>
                                    <el-form-item>
                                        <el-button type="primary" @click="onSubmit">提交实验</el-button>
                                    </el-form-item>
                                </el-form>

                            </el-header>
                            <el-main>Main</el-main>
                        </el-container>
                    </div>
                </el-aside>
                <el-main>
                    <div class="demo-image__preview" id="viewerjs">
                        <img style="width: 100px; height: 100px;float:left;margin-left:10px;margin-top:10px"
                            v-for="url in imgUrl" :key="url" :src=url />
                    </div>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>
  
<script lang="ts">
import { defineComponent, onMounted, reactive, ref, toRefs } from "vue";
import { useRouter } from 'vue-router'
import { rsvpOffline, rsvpOnline } from '../request/api'
import { OnExperience } from '../type/experience'
import { setOnStudy } from '../request/api'
import type { UploadProps, UploadUserFile } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import Viewer from "viewerjs";
import io from 'socket.io-client'
import 'viewerjs/dist/viewer.css';


export default defineComponent({
    name: "AdminView",
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
                show: function () {
                    viewer.update()
                }
            })
        })
        const form = reactive(new OnExperience())
        const onSubmit = () => {
            setOnStudy(form.experienceData).then(res => {
                console.log(res);
            })
        }
        var imgUrl = ref<string[]>([])
        var srcList = ref<string[]>([])
        const socket = io("ws://10.1.125.51:19782")
        imgUrl.value.push('https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg')
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
                if (t.predict == 1) {
                    imgUrl.value.push(url)
                }
            });
        })
        return { ...toRefs(form), onSubmit, imgUrl, }
    },
    components: {},
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
  