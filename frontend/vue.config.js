const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    open:true,
    // host: 'localhost',
    host:'0.0.0.0',
  },
})
