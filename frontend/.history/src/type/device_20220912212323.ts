export interface device{
    type:string;
    ip:string;
    port:number;
}
export class Devices{
    list:device[]=[];
    maxCount = 6
    constructor() {
       this.initDevices() 
    }

    initDevices = () => {
        for(let i = 0; i < this.maxCount; i++) {
           this.list.push({
            type: '',
            ip: '',
            port: -1
           }) 
        }
    }
}