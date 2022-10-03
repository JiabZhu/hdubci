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
        const url =
            'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg'
        const srcList = [
            'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg',
            'https://fuss10.elemecdn.com/1/34/19aa98b1fcb2781c4fba33d850549jpeg.jpeg',
            'https://fuss10.elemecdn.com/0/6f/e35ff375812e6b0020b6b4e8f9583jpeg.jpeg',
            'https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg',
            'https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg',
            'https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
            'https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg',
        ]
        return { ...toRefs(form), onSubmit, url, srcList }
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
  