/* globals Chart:false, feather:false */
feather.replace()
var ctx = document.getElementById('myChart').getContext('2d');
var myChart;
var songs_header = document.getElementById("songs_header");
var songs_list = document.getElementById("songs_list");
var playlists_header = document.getElementById("playlists_header");
var playlists = document.getElementById("playlists_list");
var users_header = document.getElementById("users_header");
var users_list = document.getElementById("users_list");
var artists_header = document.getElementById("artists_header");
var artists_list = document.getElementById("artists_list");
var comments_header = document.getElementById("comments_header");
var comments_list = document.getElementById("comments_list");
var dashboard_header = document.getElementById("dashboard_header");
var canvas = document.getElementById("myChart");
var addBtn = document.getElementById("addBtn");

songs_list.hidden = true;
songs_header.hidden = true;
playlists_header.hidden = true;
playlists.hidden = true;
users_header.hidden = true;
users_list.hidden = true;
artists_header.hidden = true;
artists_list.hidden = true;
comments_list.hidden = true;
comments_header.hidden = true;
dashboard_header.hidden = false;
canvas.hidden = false;
addBtn.hidden = true;

function draw_chart(chart_type, chart){
  myChart = new Chart(chart, {
      type: chart_type,
      data: {
          labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
          datasets: [{
              label: '# of Votes',
              data: [12, 19, 3, 5, 2, 3],
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });
}
draw_chart('line',ctx);
var menuContainer = document.getElementById("menu");

var items = menuContainer.getElementsByClassName("nav-link");


for (var i = 0; i < items.length; i++) {
  items[i].addEventListener("click", function() {
    console.log(i);
    'use strict'
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
    if(current[0].id == "dashboard"){
      addBtn.hidden = true;
      songs_list.hidden = true;
      songs_header.hidden = true;
      playlists_header.hidden = true;
      playlists.hidden = true;
      users_header.hidden = true;
      users_list.hidden = true;
      artists_header.hidden = true;
      artists_list.hidden = true;
      comments_list.hidden = true;
      comments_header.hidden = true;
      dashboard_header.hidden = false;
      canvas.hidden = false;
      draw_chart('line',canvas.getContext('2d'));
    }
    else{
      myChart.destroy();
      addBtn.hidden = false;
      if(current[0].id == "songs"){
        songs_header.hidden = false;
        songs_list.hidden = false;
        playlists_header.hidden = true;
        playlists.hidden = true;
        users_header.hidden = true;
        users_list.hidden = true;
        artists_header.hidden = true;
        artists_list.hidden = true;
        comments_list.hidden = true;
        comments_header.hidden = true;
        dashboard_header.hidden = true;
        canvas.hidden = true;
      }
      else if(current[0].id == "playlists"){
        songs_header.hidden = true;
        songs_list.hidden = true;
        playlists_header.hidden = false;
        playlists.hidden = false;
        users_header.hidden = true;
        users_list.hidden = true;
        artists_header.hidden = true;
        artists_list.hidden = true;
        comments_list.hidden = true;
        comments_header.hidden = true;
        dashboard_header.hidden = true;
        canvas.hidden = true;
      }
      else if(current[0].id == "users"){
        songs_header.hidden = true;
        songs_list.hidden = true;
        playlists_header.hidden = true;
        playlists.hidden = true;
        users_header.hidden = false;
        users_list.hidden= false;
        artists_header.hidden = true;
        artists_list.hidden = true;
        comments_list.hidden = true;
        comments_header.hidden = true;
        dashboard_header.hidden = true;
        canvas.hidden = true;
      }
      else if(current[0].id == "artists"){
        songs_header.hidden = true;
        songs_list.hidden = true;
        playlists_header.hidden = true;
        playlists.hidden = true;
        users_header.hidden = true;
        users_list.hidden= true;
        artists_header.hidden = false;
        artists_list.hidden = false;
        comments_list.hidden = true;
        comments_header.hidden = true;
        dashboard_header.hidden = true;
        canvas.hidden = true;
      }
      else if(current[0].id == "comments"){
        songs_header.hidden = true;
        songs_list.hidden = true;
        playlists_header.hidden = true;
        playlists.hidden = true;
        users_header.hidden = true;
        users_list.hidden= true;
        artists_header.hidden = true;
        artists_list.hidden = true;
        comments_list.hidden = false;
        comments_header.hidden = false;
        dashboard_header.hidden = true;
        canvas.hidden = true;
      }
    }
  });
}

//var countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Cayman Islands","Central Arfrican Republic","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cuba","Curacao","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Myanmar","Namibia","Nauro","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","North Korea","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States of America","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"];
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