import service from ".";

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
    port:Int32Array
}

export function addDevice(data:deviceInfo){
    return service({
        url:'/adddevice',
        method:'post',
        data
    })
}