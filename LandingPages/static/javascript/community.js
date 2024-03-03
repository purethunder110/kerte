
document.getElementById("submitbtn").addEventListener("click",function(e){
    e.preventDefault();
    const regex = /^[a-zA-Z]{8,}$/;
    var community=document.getElementById("community").value
    var restricted=document.getElementById("check-yes").checked
    const errorMessageElement = document.getElementById('errorMessage');
    //validating the community name
    if (regex.test(community) && restricted){
        const form=new FormData()
        form.append("Community_name",community)
        form.append("csrfmiddlewaretoken",document.getElementById("csrf_token").value)
        form.append("restricted",restricted)
        form.append("description",document.getElementById("Description"))
        
        axios.post('',form)
        .then(res=>{
            location.href=res.request.responseURL
        })
        .catch(error=>{
            errorMessageElement.textContent = error.response.data.error;
            errorMessageElement.style.display = 'block';
        })
    }
    else{
        errorMessageElement.textContent = 'Please enter a valid name';
        errorMessageElement.style.display = 'block';
    }
});