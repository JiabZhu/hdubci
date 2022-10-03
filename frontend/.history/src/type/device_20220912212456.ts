export interface device{
    type:string;
    ip:string;
    port:number | undefined;
}
export class Devices{
    list:device[]=[];
    private maxCount = 6
    constructor() {
       this.initDevices() 
    }

    private initDevices = () => {
        for(let i = 0; i < this.maxCount; i++) {
           this.list.push({
            type: '',
            ip: '',
            port: undefined
           }) 
        }
    }
}