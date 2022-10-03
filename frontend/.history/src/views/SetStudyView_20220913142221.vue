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

        <el-form :model="form" label-width="120px"
          style="width:800px;position:absolute;left:50%;margin-left:-400px;margin-top:100px;">


          <el-form-item label="目标：非目标">

            <el-form :inline="true" :model="formInline" class="demo-form-inline">
              <el-form-item>
                <el-input v-model="formInline.user" />
              </el-form-item>
              <el-form-item label=":" style="margin-left:-20px;">
                <el-input v-model="formInline.user" />
              </el-form-item>
            </el-form>

          </el-form-item>


          <el-form-item label="实验次数">
            <el-input style="width:410px;" v-model="formInline.user"/>
          </el-form-item>

          <el-form-item label="目标mack值">

            <el-form :inline="true" :model="formInline" class="demo-form-inline">
              <el-form-item >
                <el-input v-model="formInline.user" />
              </el-form-item>
              <el-form-item label="非目标mark值">
                <el-input v-model="formInline.user" />
              </el-form-item>
            </el-form>

          </el-form-item>

          <el-form-item label="准备时间">
            <el-input style="width:410px;" v-model="formInline.user"/>
          </el-form-item>

          <el-form-item label="刺激呈现时间">
            <el-input style="width:410px;" v-model="formInline.user"/>
          </el-form-item>

          <el-form-item label="Resources">
            <el-radio-group v-model="form.resource">
              <el-radio label="Sponsor" />
              <el-radio label="Venue" />
            </el-radio-group>
          </el-form-item>
          <el-form-item label="Activity form">
            <el-input v-model="form.desc" type="textarea" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">Create</el-button>
            <el-button>Cancel</el-button>
          </el-form-item>
        </el-form>

      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, toRefs } from "vue";
import { useRouter, useRoute } from 'vue-router'
import { addDevice } from "@/request/api";

export default defineComponent({
  name: "SetStudy",
  setup() {
    const form = reactive({
      name: '',
      region: '',
      date1: '',
      date2: '',
      delivery: false,
      type: [],
      resource: '',
      desc: '',
    })

    const formInline = reactive({
      user: '',
      region: '',
    })
    const onSubmit = () => {
      console.log('submit!')
    }
    return { form, onSubmit, formInline }
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
