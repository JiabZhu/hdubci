const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    open:true,
    host: 'localhost',
    proxy:{// 通过代理实现跨域
      // http://127.0.0.1
      '/':{
        target:'http://127.0.0.1:5000', //要替换的服务端地址
        changeOrigin:true, //开启代理 允许跨域请求数据
        // rewrite:path=>path.replace(/^\/path/,'')//设置重写路径
      }
    }
  },
  // server:{ //配置中转服务器
  //   proxy:{// 通过代理实现跨域
  //     // http://127.0.0.1
  //     '/path':{
  //       target:'http://127.0.0.1', //要替换的服务端地址
  //       changeOrigin:true, //开启代理 允许跨域请求数据
  //       rewrite:path=>path.replace(/^\/path/,'')//设置重写路径
  //     }
  //   }
  // }
})
