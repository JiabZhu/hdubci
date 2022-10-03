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
                <el-aside width="200px">
                    <el-container>
                        <el-header>Header</el-header>
                        <el-main>Main</el-main>
                    </el-container>
                </el-aside>
                <el-main>
                    <el-container>
                        <el-aside width="200px">Aside</el-aside>
                        <el-main>Main</el-main>
                    </el-container>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>
  
<script lang="ts">
import { defineComponent, reactive, ref } from "vue";
import { useRouter } from 'vue-router'
import { rsvpOffline, rsvpOnline } from '../request/api'

export default defineComponent({
    name: "AdminView",
    setup() {
        const router = useRouter()
        const dialogFormVisible = ref(false)
        const formLabelWidth = '140px'
        const form = reactive({
            region: '',
        })
        return { form, dialogFormVisible, formLabelWidth, }
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
  