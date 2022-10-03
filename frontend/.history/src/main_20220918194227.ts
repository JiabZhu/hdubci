import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import VueNativeSock from "vue-native-websocket-vue3";

const app=createApp(App);
// app.use(VueNativeSock,'');
app.use(router).use(ElementPlus).mount('#app')
export default app;
