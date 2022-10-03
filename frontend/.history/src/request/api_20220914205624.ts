import service from ".";
import { offExperienceInt,onExperienceInt } from "@/type/experience";
export function rsvpOffline(){
    return service({
        url:'/study/rsvp_offline',
        method:'GET'
    })
}

export function rsvpOnline(){
    return service({
        url:'/study/rsvp_online',
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

// export function

export function setOffStudy(data:offExperienceInt){
    return service({
        url:'/setstudy',
        method:'post',
        data
    })
}

export function setOnStudy(data:onExperienceInt){
    return service({
        url:'/setstudy',
        method:'post',
        data
    })
}