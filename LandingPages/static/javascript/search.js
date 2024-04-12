let currentPage= 1
var has_next= true
var endcredits=true
searchterm=""
window.onload=function() {
    searchterm=document.getElementById("searchterm").value
    const load=document.getElementById('load');
    const area=load.getBoundingClientRect();
    if (area.top >= 0 &&
        area.left >= 0 &&
        area.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        area.right <= (window.innerWidth || document.documentElement.clientWidth)){
            console.log("test")
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
    axios.get('/@community/search/api/'+searchterm+'/?page='+currentPage)
    .then(response=>{
        console.log("test2")
        const data=response.data;
        parentElement=document.getElementById("articles-list")
        if (has_next){
            data.Community.forEach(comm=>{
                console.log("test3")
                /*
                
                card=document.createElement('div')
                card.className="card"
                body=document.createElement('div')
                body.className="card-body"
                title=document.createElement('h4')
                for (let i in x){
                    console.log(i)
                }
                title.textContent=x.title
                
                card.append(body)
                parentElement.append(card)
                body.append(title)*/
                // Create card container
                const card = document.createElement('div');
                card.className = "card";

                // Create card body
                const body = document.createElement('div');
                body.className = "card-body";
                

                // Create community link
                const communityLink = document.createElement('a');
                communityLink.href = `/@community/`+comm.Communityid;
                communityLink.textContent = comm.title;

                // Create description element
                const description = document.createElement('p');
                description.className = "card-text";
                description.textContent = comm.description;

                // Create read more link
                const readMore = document.createElement('span');
                readMore.className = "read-more";
                const readMoreLink = document.createElement('a');
                readMoreLink.href = `/@community/`+comm.Communityid;
                readMoreLink.textContent = "View Community";
                readMore.appendChild(readMoreLink);

                // Append elements to card body
                body.appendChild(communityLink);
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