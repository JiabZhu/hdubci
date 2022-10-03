<template>
  <div>
    <el-container>
      <el-header>
        <el-row :gutter="20">
          <el-col :span="4"><img src="../assets/BCI_title.jpg" class="logo" /></el-col>
        </el-row>
      </el-header>
      <el-container>
        <el-main>
          <div class="common-layout">
            <el-container>
              <el-aside width="600px">
                <el-card shadow="always" @click="dialogFormVisible = true" style="cursor: pointer;">

                  <img src="../assets/neuro1.jpg" class="neuro1" />
                </el-card>
              </el-aside>
              <el-container>
                <el-header style="height:380px;">
                  <el-card shadow="always" class="neuro_box">
                    <img src="../assets/neuro2.png" class="neuro2" />
                  </el-card>
                </el-header>
                <el-main style="overflow:hidden">
                  <el-aside width="300px" style="float:left">
                    <el-card shadow="always">
                      <img src="../assets/gtec.jpg" class="gtec" />
                    </el-card>
                  </el-aside>
                  <el-aside width="300px" style="float: right;">
                    <el-card shadow="always">
                      <img src="../assets/emotive.png" class="emotive" />
                    </el-card>
                  </el-aside>
                </el-main>
              </el-container>
            </el-container>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {


    return {}
  }
})
</script>

<style scoped>

</style>