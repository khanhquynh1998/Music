var c = 1
var i;
var file = [];
var files = document.getElementById('urls').innerText;
f = files.split(' ');
for(i = 0; i<f.length; i++){
    if(f[i].startsWith("/")){
        file.push(f[i]);
    }
}
//console.log(file[c]);
var a = document.getElementById('audio');
function btn_next(){
    //alert("Next was clicked")
    console.log(c)
    c = c+1;
    if(c>=file.length){
        c=0;
    }
    document.getElementById('audio').src=file[c];
    a.load()
    
    console.log(file[c])
};
function btn_prev(){
    //alert("Prev was clicked")
    console.log(c)
    c = c-1;
    if(c < 0){
        c=file.length-1;
    }
    document.getElementById('audio').src=file[c];
    a.load()
    
    console.log(file[c]);
};
a.addEventListener('ended', function(){
    document.getElementById('audio').src=file[c];
    a.load();
    console.log(file[c]);
    c++;

    if(c>=file.length){
        c=0;
    }
});

function chatbot(){
    alert("Hello")
}