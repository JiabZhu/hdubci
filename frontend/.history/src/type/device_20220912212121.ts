export interface device{
    type:string;
    ip:string;
    port:number;
}
export class Devices{
    list:device[]=[];
    private MAX_COUNT: number = 6
    constructor() {
       this.initDevices() 
    }

    private initDevices = () => {
        for(let i = 0; i < this.MAX_COUNT; i++) {
           this.list.push({
            type: '',
            ip: '',
            port: -1
           }) 
        }
    }
}