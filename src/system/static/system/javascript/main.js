$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

document.getElementById("time").innerHTML = new Date().getFullYear();

window.onscroll = () => {
    if (document.body.scrollTop < 50) document.getElementById("btt").style.display = "none"
    else document.getElementById("btt").style.display = ""
}