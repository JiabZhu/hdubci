import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import VueNativeSock from "vue-native-websocket-vue3";
// import {createStore} from 'vuex'
import websocket from './store/websocket'
import VueSocketIO from 'vue-socket.io'
import Viewer from 'v-viewer'
import 'viewerjs/dist/viewer.css'

const app=createApp(App);
// app.use(VueNativeSock,'');
// app.use(new VueSocketIO({
//     debug: true,   
//     connection: "ws://10.1.125.51:19782"
// }))
app.use(Viewer as any)

Viewer.setDefaults({
    Options: {
      'inline': true,
      'button': true,
      'navbar': true,
      'title': true,
      'toolbar': true,
      'tooltip': true,
      'movable': true,
      'zoomable': true,
      'rotatable': true,
      'scalable': true,
      'transition': true,
      'fullscreen': true,
      'keyboard': true,
      'url': 'data-source'
    }
},
app.config.globalProperties.$websocket=websocket,
app.use(router).use(ElementPlus).mount('#app')

export default app;
