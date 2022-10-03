import axios from 'axios';
// 创建axios实例
const service=axios.create({
    baseURL: "http://10.253.32.92:19782",
    timeout: 5000,
    headers:{
        "Content-Type":"application/json;charset=utf-8"
    },
    // data:JSON.stringify(config.params)
})
// 请求拦截
service.interceptors.request.use((config)=>{
    config.headers=config.headers||{}
    if(localStorage.getItem('token')){
        config.headers.token=localStorage.getItem('token') || "";
    }
    return config;
})

// 响应拦截
service.interceptors.response.use((res)=>{
    const code:number=res.status
    if(code!=200){
        return Promise.reject(res.data)
    }
    return res.data
},(err)=>{
    console.log(err);
})
export default service