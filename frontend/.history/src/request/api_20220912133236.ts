import service from ".";

export function rsvpOffline(){
    return service({
        url:'/study/rsvp_offline',
        method:'GET'
    })
}