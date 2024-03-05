document.getElementById("tagcreate").addEventListener("click", function() {
    var menu = document.getElementById("tagadd");
    if (menu.style.display === "none" || menu.style.display === "") {
      menu.style.display = "block";
    } else {
      menu.style.display = "none";
    }
  });
  
  document.getElementById("addTagbtn").addEventListener("click", function() {
    var Tagname = document.getElementById("Tagname").value;
    var Tagdescription = document.getElementById("Tagdescription").value;
    const errorMessageElement = document.getElementById('errorMessage');
    if (Tagname!== ''){
        //sending data for saving
        let form=new FormData()
        form.append("csrfmiddlewaretoken",document.getElementById("token").value)
        form.append("Tagname",Tagname)
        form.append("Tagdescription",Tagdescription)
        axios.post('',form)
        .then(result=>{
            const tagButtons= document.getElementById("tags");
            const tagButton=document.createElement('input');
            tagButton.type="button";
            tagButton.title=Tagdescription;
            //tagButton.className= 'border:1px;display:inline-block';
            tagButton.value=Tagname;
            tagButton.onclick= () => toggleTag(tagButton);
            tagButtons.appendChild(tagButton);
            Tagname.value='';
            errorMessageElement.style.display = 'none';
        })
        .catch(error=>{
            console.log(error)
            errorMessageElement.textContent = 'Internal error occured';
            errorMessageElement.style.display = 'block';
        })
    }
  
  });

  function toggleTag(tagButton) {
    tagButton.classList.toggle('btn-tag-selected');
    //filterPosts();
}
/*
function filterPosts() {
    const selectedTags = Array.from(document.querySelectorAll('#posts .btn-tag-selected')).map(btn => btn.textContent);
    if (selectedTags.length === 0) {
        //displayPosts(posts);
    } else {
        const filteredPosts = posts.filter(post => {
            return selectedTags.some(tag => post.tags.includes(tag));
        });
        displayPosts(filteredPosts);
    }
}
*/