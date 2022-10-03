import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import VueNativeSock from "vue-native-websocket-vue3";
// import {createStore} from 'vuex'
import websocket from './store/websocket'
import VueSocketIO from 'vue-socket.io'

const app=createApp(App);

app.config.globalProperties.$websocket=websocket
app.use(router).use(ElementPlus).mount('#app')

export default app;
