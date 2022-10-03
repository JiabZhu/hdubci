import service from ".";
import { experienceInt } from "@/type/experience";
export function rsvpOffline(){
    return service({
        url:'/study/rsvp_offline',
        method:'GET'
    })
}

// addDevice
interface deviceInfo{
    type:string,
    ip:string,
    port:number,
}

export function addDevice(data:deviceInfo){
    return service({
        url:'/adddevice',
        method:'post',
        data
    })
}

export function setStudy(data:experienceInt){
    return service({
        url:'/setstudy',
        method:'post',
        data
    })
}