import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import VueNativeSock from "vue-native-websocket-vue3";
// import {createStore} from 'vuex'
import websocket from './store/websocket'
import VueSocketIO from 'vue-socket.io'
// import VueDirectiveImagePreviewer from 'vue-directive-image-previewer'
// import 'vue-directive-image-previewer/dist/assets/style.css'
import Viewer from 'viewerjs';
import 'viewerjs/dist/viewer.css';

Viewer.setDefaults({
    navbar: true,
    title: true,
    toolbar: {
      prev: true,
      next: true,
    },
  });

const app=createApp(App);
// app.use(VueDirectiveImagePreviewer)
app.use(()=>Viewer)
app.config.globalProperties.$websocket=websocket
app.use(router).use(ElementPlus).mount('#app')

export default app;
