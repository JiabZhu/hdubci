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
            <el-aside width="200px">Aside</el-aside>
            <el-main>Main</el-main>
          </el-container>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent, reactive, ref, toRefs } from "vue";
export default defineComponent({
  name: "SetStudy",
  setup() {
    return {};
  },

  methods: {

  },
  computed: {
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

