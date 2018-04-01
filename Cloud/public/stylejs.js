var autobtn = document.getElementById("autobtn");
var manualbtn = document.getElementById("manualbtn");
var waterbtn = document.getElementById("waterbtn");
var waternowbtn = document.getElementById("waternowbtn");


autobtn.addEventListener("click",function(){
	waternowbtn.style.visibility = "hidden";
    waterbtn.style.visibility = "hidden";
});

manualbtn.addEventListener("click",function(){
	waternowbtn.style.visibility = "visible";
    waterbtn.style.visibility = "visible";
});


