let previous = document.querySelector('#pre');
let play = document.querySelector('#play');
let next = document.querySelector('#next');
let recent_volume= document.querySelector('#volume');
let volume_show = document.querySelector('#volume_show');
let slider = document.querySelector('#duration_slider');
let show_duration = document.querySelector('#show_duration');
let auto_play = document.querySelector('#auto');
let present = document.querySelector('#present');
let total = document.querySelector('#total');


let timer;
let autoplay = 0;

let index_no = 0;
let Playing_song = false;


//create a audio Element
let track = document.createElement('audio');

var i;
var file = [];
var files = document.getElementById('urls').innerText;
f = files.split('_ ');
for(i = 0; i<f.length; i++){
    if(f[i] != " "){
        file.push(f[i]);
    }
}
for (i=0; i<file.length; i++){
	file[i] = file[i].split(','); 
}

/* FILE = [
			[
				song_name,
				song_audio_URL,
				song_image_URL,
				song_artist_name
			],
			...
]*/

// function load the track
function load_track(index_no){
	clearInterval(timer);
	reset_slider();
	track.src = file[index_no][1];
    //console.log("Hello");
	title.innerHTML = file[index_no][0];	
	track_image.src = file[index_no][2];
    artist.innerHTML = file[index_no][3];
    track.load();
    track.autoplay = true;
    Playing_song = true;
    play.innerHTML = '<i class="fa fa-pause" aria-hidden="true"></i>';
	timer = setInterval(range_slider ,1000);
	total.innerHTML = file.length;
	present.innerHTML = index_no + 1;
}

load_track(0);

//mute sound function
function mute_sound(){
	track.volume = 0;
	volume.value = 0;
	volume_show.innerHTML = 0;
}


// checking.. the song is playing or not
 function justplay(){
 	if(Playing_song==false){
 		playsong();

 	}else{
 		pausesong();
 	}
 }


// reset song slider
 function reset_slider(){
 	slider.value = 0;
 }

// play song
function playsong(){
  track.play();
  Playing_song = true;
  play.innerHTML = '<i class="fa fa-pause" aria-hidden="true"></i>';
}

//pause song
function pausesong(){
	track.pause();
	Playing_song = false;
	play.innerHTML = '<i class="fa fa-play" aria-hidden="true"></i>';
}


// next song
function next_song(){
	if(index_no < file.length - 1){
		index_no += 1;
		load_track(index_no);
		playsong();
	}else{
		index_no = 0;
		load_track(index_no);
		playsong();

	}
}


// previous song
function previous_song(){
	if(index_no > 0){
		index_no -= 1;
		load_track(index_no);
		playsong();

	}else{
		index_no = file.length;
		load_track(index_no);
		playsong();
	}
}


// change volume
function volume_change(){
	volume_show.innerHTML = recent_volume.value;
	track.volume = recent_volume.value / 100;
}

// change slider position 
function change_duration(){
	slider_position = track.duration * (slider.value / 100);
	track.currentTime = slider_position;
}

// autoplay function
function autoplay_switch(){
	if (autoplay==1){
       autoplay = 0;
       auto_play.style.background = "rgba(255,255,255,0.2)";
	}else{
       autoplay = 1;
       auto_play.style.background = "#FF8A65";
	}
}


function range_slider(){
	let position = 0;
        
        // update slider position
		if(!isNaN(track.duration)){
		   position = track.currentTime * (100 / track.duration);
		   slider.value =  position;
	      }

       
       // function will run when the song is over
       if(track.ended){
       	 play.innerHTML = '<i class="fa fa-play" aria-hidden="true"></i>';
           if(autoplay==1){
			   if(file.length > 1){
				   index_no += 1
			   }
		       load_track(index_no);
		       playsong();
           }
	    }
     }


	 var songs = document.getElementById("songs_arr").innerText.split('<QuerySet ')[1];
	 songs = songs.split(', ');
	 for (var i=0; i<songs.length; i++){
	   songs[i] = songs[i].replace('[', '');
	   songs[i] = songs[i].replace('<', '');
	   songs[i] = songs[i].replace('>', '');
	   songs[i] = songs[i].replace(']', '');
	   songs[i] = songs[i].replace('>', '');
	   songs[i] = songs[i].split('Song: ')[1];
	 }
	 console.log(songs);
	 var countries = songs;
	 
	 function autocomplete(inp, arr) {
	   /*the autocomplete function takes two arguments,
	   the text field element and an array of possible autocompleted values:*/
	   var currentFocus;
	   /*execute a function when someone writes in the text field:*/
	   inp.addEventListener("input", function(e) {
		   var a, b, i, val = this.value;
		   /*close any already open lists of autocompleted values*/
		   closeAllLists();
		   if (!val) { return false;}
		   currentFocus = -1;
		   /*create a DIV element that will contain the items (values):*/
		   a = document.createElement("DIV");
		   a.setAttribute("id", this.id + "autocomplete-list");
		   a.setAttribute("class", "autocomplete-items");
		   /*append the DIV element as a child of the autocomplete container:*/
		   this.parentNode.appendChild(a);
		   /*for each item in the array...*/
		   for (i = 0; i < arr.length; i++) {
			 /*check if the item starts with the same letters as the text field value:*/
			 if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
			   /*create a DIV element for each matching element:*/
			   b = document.createElement("DIV");
			   /*make the matching letters bold:*/
			   b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
			   b.innerHTML += arr[i].substr(val.length);
			   /*insert a input field that will hold the current array item's value:*/
			   b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
			   /*execute a function when someone clicks on the item value (DIV element):*/
				   b.addEventListener("click", function(e) {
				   /*insert the value for the autocomplete text field:*/
				   inp.value = this.getElementsByTagName("input")[0].value;
				   /*close the list of autocompleted values,
				   (or any other open lists of autocompleted values:*/
				   closeAllLists();
			   });
			   a.appendChild(b);
			 }
		   }
	   });
	   /*execute a function presses a key on the keyboard:*/
	   inp.addEventListener("keydown", function(e) {
		   var x = document.getElementById(this.id + "autocomplete-list");
		   if (x) x = x.getElementsByTagName("div");
		   if (e.keyCode == 40) {
			 /*If the arrow DOWN key is pressed,
			 increase the currentFocus variable:*/
			 currentFocus++;
			 /*and and make the current item more visible:*/
			 addActive(x);
		   } else if (e.keyCode == 38) { //up
			 /*If the arrow UP key is pressed,
			 decrease the currentFocus variable:*/
			 currentFocus--;
			 /*and and make the current item more visible:*/
			 addActive(x);
		   } else if (e.keyCode == 13) {
			 /*If the ENTER key is pressed, prevent the form from being submitted,*/
			 e.preventDefault();
			 if (currentFocus > -1) {
			   /*and simulate a click on the "active" item:*/
			   if (x) x[currentFocus].click();
			 }
		   }
	   });
	   function addActive(x) {
		 /*a function to classify an item as "active":*/
		 if (!x) return false;
		 /*start by removing the "active" class on all items:*/
		 removeActive(x);
		 if (currentFocus >= x.length) currentFocus = 0;
		 if (currentFocus < 0) currentFocus = (x.length - 1);
		 /*add class "autocomplete-active":*/
		 x[currentFocus].classList.add("autocomplete-active");
	   }
	   function removeActive(x) {
		 /*a function to remove the "active" class from all autocomplete items:*/
		 for (var i = 0; i < x.length; i++) {
		   x[i].classList.remove("autocomplete-active");
		 }
	   }
	   function closeAllLists(elmnt) {
		 /*close all autocomplete lists in the document,
		 except the one passed as an argument:*/
		 var x = document.getElementsByClassName("autocomplete-items");
		 for (var i = 0; i < x.length; i++) {
		   if (elmnt != x[i] && elmnt != inp) {
		   x[i].parentNode.removeChild(x[i]);
		 }
	   }
	 }
	 /*execute a function when someone clicks in the document:*/
	 document.addEventListener("click", function (e) {
		 closeAllLists(e.target);
	 });
	 }
	 
	 autocomplete(document.getElementById("myInput"), countries);