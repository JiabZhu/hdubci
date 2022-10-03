import service from ".";

export function rsvpOffline(){
    return service({
        url:'/study/rsvp_offline',
        method:'GET'
    })
}

// addDevice
interface deviceInfo{
    name:string,
    ip:string,
    port:string
}

export function addDevice(data:deviceInfo){
    return service({
        url:'/adddevice',
        method:'post',
        data
    })
}