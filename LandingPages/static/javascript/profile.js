let currentPage= 1
var has_next= true
var endcredits=true
window.onload=function() {
    const load=document.getElementById('load');
    const area=load.getBoundingClientRect();
    if (area.top >= 0 &&
        area.left >= 0 &&
        area.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        area.right <= (window.innerWidth || document.documentElement.clientWidth)){
            loadData()
        }
}
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
    //const load=document.getElementById('load');
    const area=load.getBoundingClientRect();
    if (area.top >= 0 &&
        area.left >= 0 &&
        area.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        area.right <= (window.innerWidth || document.documentElement.clientWidth)){
    axios.get('/@post/profile/?page='+currentPage)
    .then(response=>{
        const data=response.data;
        parentElement=document.getElementById("articles-list")
        if (has_next){
            data.posts.forEach(post=>{
                // Create card container
                const card = document.createElement('div');
                card.className = "card";

                // Create card body
                const body = document.createElement('div');
                body.className = "card-body";

                // Create title element
                const title = document.createElement('h5');
                title.className = "card-title";
                title.textContent = post.title;

                // Create community link
                const communityLink = document.createElement('a');
                communityLink.href = `/@community/`+post.Community_id;
                communityLink.textContent = post.Community_name;

                // Create publish date element
                const publishDate = document.createElement('p');
                publishDate.className = "publish-date";
                publishDate.textContent = post.date;

                // Create description element
                const description = document.createElement('p');
                description.className = "card-text";
                description.textContent = post.description;

                // Create read more link
                const readMore = document.createElement('span');
                readMore.className = "read-more";
                const readMoreLink = document.createElement('a');
                readMoreLink.href = `/@post/view/`+post.postid;
                readMoreLink.textContent = "View Post";
                readMore.appendChild(readMoreLink);

                // Append elements to card body
                body.appendChild(title);
                body.appendChild(communityLink);
                body.appendChild(publishDate);
                body.appendChild(description);
                body.appendChild(readMore);

                // Append card body to card
                card.appendChild(body);

                // Append card to parent element
                parentElement.appendChild(card);
            })
        has_next=data.has_next
        }
    })
    .catch(error=>{console.log(error)})
    currentPage+=1;
    }
}