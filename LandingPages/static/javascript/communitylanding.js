
var modal = document.querySelector(".modal");

function toggleModal() {
    modal.classList.toggle("show-modal");
}

/*
document.getElementById("tagcreate").addEventListener("click", function() {
    var menu = document.getElementById("tagadd");
    if (menu.style.display === "none" || menu.style.display === "") {
      menu.style.display = "block";
    } else {
      menu.style.display = "none";
    }


  });
*/
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
            tagButton.value=Tagname;
            tagButton.onclick= () => toggleTag(tagButton);
            tagButtons.appendChild(tagButton);
            Tagname.value='';
            tagButton.className="tagss";
            modal.classList.toggle("show-modal");
        })
        .catch(error=>{
            console.log(error)
            errorMessageElement.textContent = 'Internal error occured';
            errorMessageElement.style.display = 'block';
        })
    }
});

function toggleTag(tagButton) {
    cleartag()
    tagButton.classList.toggle('btn-tag-selected');
    tagvalue=tagButton.value;
    let togvalue=tagButton.getAttribute("data-toggle")
    if (togvalue==="true"){
        tagButton.setAttribute("data-toggle","false");
        filterPosts(tagvalue);
    }
    else{
        tagButton.setAttribute("data-toggle","true");
        cleartag()
    }
}

function filterPosts(tagvalue) {
   const posts= document.getElementById("posts-list")
   let childrenposts= Array.from(posts.children)
   console.log(childrenposts)
   childrenposts.forEach(post => {
    let posttag = post.getAttribute("data-tag");
    if (posttag===tagvalue){
        console.log("perfect")
        post.style.display=''

    }
    else{
        post.style.display='none'
    }

   });
}

function cleartag(){
    //for tags
    let tagdiv=document.getElementById("tags")
    let taglist= Array.from(tagdiv.children)
    taglist.forEach(tag=>{
        let insidetags=tag.classList
        tag.classList.remove('btn-tag-selected');
        tag.setAttribute("data-toggle","true");
    });
    //for posts
    const posts= document.getElementById("posts-list")
    let childrenposts= Array.from(posts.children)
    childrenposts.forEach(post => {
        let posttag = post.getAttribute("data-tag");
        post.style.display=''

   });
}

function deletetag(){
    let tagdiv=document.getElementById("tags")
    let taglist= Array.from(tagdiv.children)
    taglist.forEach(tag=>{
        let insidetags=tag.classList
        /*
        tag.style.animation('shake 0.5s');
        tag.style.animationIterationCount('infinite')
        */
        tag.setAttribute("data-toggle","true");
        

    });
}

const triggerButton = document.getElementById('tagcreate');
triggerButton.addEventListener('click', function () {
    console.log("clicked");
    toggleModal();
})

const closeButton = document.getElementById('close-btn');
closeButton.addEventListener('click', function () {
    console.log("closed");
    toggleModal();
})
//dynamic scrolling
let currentPage=3
var has_next= true
var endcredits=true

window.addEventListener('scroll',function(){
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        loadData();
    }
})

function loadData(){
    const load=document.getElementById('load');
    if (has_next == false){
        if (endcredits){
            const Endpost = document.createElement('p');
            Endpost.className = "publish-date";
            Endpost.textContent = "This is the end of posts";
            load.appendChild(Endpost)
            endcredits=false
        }
        return ;
    }
    const area=load.getBoundingClientRect();
    if (area.top >= 0 &&
        area.left >= 0 &&
        area.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        area.right <= (window.innerWidth || document.documentElement.clientWidth)){
        channelID=document.getElementById("communityid").value
        if (has_next){
            axios.get('/@community/api/'+channelID+'/?page='+currentPage)
            .then(response=>{

                console.log(response)
                response.data.posts.forEach(post=>{
                    const card = document.createElement('div');
                    card.classList.add('card');
                    card.innerHTML = `
                    <div class="card-header flex flex-center">
                        <div class="card-img">
                        </div>
                        <div class="card-text">
                        <div class="text-heading" onclick="window.location='/@post/view/${postid}'>
                            <h4>${post.title}</h4>
                        </div>
                        <div class="text-body">
                            <p>${post.description}</p>
                        </div>
                        </div>
                    </div>
                    <div class="card-footer flex flex-between">
                        <div class="card-actions">
                        <div class="date-time">${post.dateofpost}</div>
                        </div>
                        <div>
                        <a href="#" style="color:black">${post.postuser}</a>
                        </div>
                        <div class="action-buttons">
                        <input type="button" onclick="window.location='/@${post.uuid}/delete'" value="Delete Post" class="act-btn">
                        <input type="button" onclick="window.location='/@${post.uuid}/edit'" value="Edit Post" class="act-btn">
                        </div>
                    </div>
                    `;
                    document.getElementById("post-list").appendChild(card);
                })
            })
            .catch(error=>console.log(error))
            currentPage+=1;
        }

    }
}

/*new filter drop down*/
