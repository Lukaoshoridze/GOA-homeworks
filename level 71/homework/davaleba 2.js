function removeDiv(){
    let div = document.getElementById("davaleba 1-div");
    if (div.style.display === "none"){
        div.style.display = "block";
    } else {
        div.style.display = "none";
        
    }
    console.log(div.style.display)
}