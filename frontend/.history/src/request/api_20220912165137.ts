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
    IP:
}
export function addDevice(data:){
    return service({
        url:'/addDevice',
        method:'post',
        data
    })
}