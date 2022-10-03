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
                            <el-header style="height:400px">
                                <h2>实验设置</h2>
                                <el-form :model="experienceData" label-width="120px" style="margin-top:20px">
                                    <el-form-item label="刺激呈现时间">
                                        <el-input v-model="experienceData.pic_duration" style="width:200px;" />
                                    </el-form-item>
                                    <el-form-item label="时间窗口">
                                        <el-input v-model="experienceData.time_window" style="width:200px;" />
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
                            <el-aside width="200px">Aside</el-aside>
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

export default defineComponent({
    name: "AdminView",
    setup() {
        const form = reactive(new OnExperience())
        return { ...toRefs(form), }
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
  