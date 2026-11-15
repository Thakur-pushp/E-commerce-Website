const check = document.getElementById("checkbox")
const sidebar = document.getElementById("sidebar")

check.addEventListener('change',()=>{
    if(check.checked){
        sidebar.classList.remove('inactive')
    }
    else{
        sidebar.classList.add('inactive')
    }
})