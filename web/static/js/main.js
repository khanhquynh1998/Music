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
a.addEventListener('ended', function(){
    document.getElementById('audio').src=file[c];
    a.load();
    //console.log(file[c]);
    c++;

    if(c>=file.length){
        c=0;
    }
});