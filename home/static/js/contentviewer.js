//get all elements with class="innercontent"  and hide them
tabcontent=document.getElementsByClassName("innercontent");
for(var i=0;i<tabcontent.length;i++){
tabcontent[i].style.display="none";
}

function InnerContentShow(tabName){
    
    //get all elements with class="innercontent"  and hide them
tabcontent=document.getElementsByClassName("innercontent");
for(var i=0;i<tabcontent.length;i++){
tabcontent[i].style.display="none";
}
    
    //show the current tab inner content
document.getElementById(tabName).style.display="block";
    
}

function ChangeNewsBar(hide,show){
    hide=document.getElementById(hide);
    show=document.getElementById(show);
    
    hide.style.display = "none";
    show.style.display = "block";
    
}

function Complaint_follow(){
    
    complaints_follow=document.getElementsByClassName("complaints_follow");
    for(var i=0;i<complaints_follow.length;i++){
    complaints_follow[i].style.display="none";
    }
    
    InnerContentShow('suggestion4');
    complainter_id = document.getElementById('complainter-id').value;
    div_id = document.getElementsByClassName(complainter_id);
    for(var i=0;i<div_id.length;i++){
    div_id[i].style.display="block";
    }
    return false;
    
}
