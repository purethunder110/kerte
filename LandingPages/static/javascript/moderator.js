function promoteadmin(uuid){
    var form= new FormData()
    form.append('csrfmiddlewaretoken',document.getElementById("csrfmiddlewaretoken").value)
    form.append('user_uuid',uuid)
    form.append('role',"ADMIN")

    axios.post('',form)
    .then(result=>{
        location.reload()
    })
    .catch(error=>{
        alert("unexpected error occured. please try again")
    })
}

function promotemod(uuid){
    var form= new FormData()
    form.append('csrfmiddlewaretoken',document.getElementById("csrfmiddlewaretoken").value)
    form.append('user_uuid',uuid)
    form.append('role',"MOD")
    axios.post('',form)
    .then(result=>{
        location.reload()
    })
    .catch(error=>{
        alert("unexpected error occured. please try again")
    })
}

function demote(uuid){
    var form= new FormData()
    form.append('csrfmiddlewaretoken',document.getElementById("csrfmiddlewaretoken").value)
    form.append('user_uuid',uuid)
    form.append('role',"USER")
    axios.post('',form)
    .then(result=>{
        location.reload()
    })
    .catch(error=>{
        alert("unexpected error occured. please try again")
    })
}