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
                    <div class="common-layout">
                        <el-container>
                            <el-aside width="200px">
                                <el-upload v-model:file-list="fileList"
                                    action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                                    list-type="picture-card" :on-preview="handlePictureCardPreview"
                                    :on-remove="handleRemove">
                                </el-upload>
                                <el-dialog v-model="dialogVisible">
                                    <img w-full :src="dialogImageUrl" alt="Preview Image" />
                                </el-dialog>
                            </el-aside>
                            <el-main>Main</el-main>
                        </el-container>
                    </div>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>
  
<script lang="ts">
import { defineComponent, reactive, ref, toRefs } from "vue";
import { useRouter } from 'vue-router'
import { rsvpOffline, rsvpOnline } from '../request/api'
import { OnExperience } from '../type/experience'
import { setOnStudy } from '../request/api'
import type { UploadProps, UploadUserFile } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'

export default defineComponent({
    name: "AdminView",
    setup() {
        const form = reactive(new OnExperience())
        const onSubmit = () => {
            setOnStudy(form.experienceData).then(res => {
                console.log(res);
            })
        }
        const fileList = ref<UploadUserFile[]>([
            {
                name: 'food.jpeg',
                url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
            },
            {
                name: 'plant-1.png',
                url: '/images/plant-1.png',
            },
            {
                name: 'food.jpeg',
                url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
            },
            {
                name: 'plant-2.png',
                url: '/images/plant-2.png',
            },
            {
                name: 'food.jpeg',
                url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
            },
            {
                name: 'figure-1.png',
                url: '/images/figure-1.png',
            },
            {
                name: 'food.jpeg',
                url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
            },
            {
                name: 'figure-2.png',
                url: '/images/figure-2.png',
            },
        ])

        const dialogImageUrl = ref('')
        const dialogVisible = ref(false)

        const handleRemove: UploadProps['onRemove'] = (uploadFile, uploadFiles) => {
            console.log(uploadFile, uploadFiles)
        }

        const handlePictureCardPreview: UploadProps['onPreview'] = (uploadFile) => {
            dialogImageUrl.value = uploadFile.url!
            dialogVisible.value = true
        }
        return { ...toRefs(form), onSubmit, dialogVisible, dialogImageUrl ,fileList,handlePictureCardPreview,handleRemove}
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
  