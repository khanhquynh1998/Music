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
var dashboard_header = document.getElementById("dashboard_header");
var canvas = document.getElementById("myChart");

songs_list.hidden = true;
songs_header.hidden = true;
playlists_header.hidden = true;
playlists.hidden = true;
users_header.hidden = true;
users_list.hidden = true;
dashboard_header.hidden = false;
canvas.hidden = false;

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
draw_chart('bar',ctx);
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
      songs_list.hidden = true;
      songs_header.hidden = true;
      playlists_header.hidden = true;
      playlists.hidden = true;
      users_header.hidden = true;
      users_list.hidden = true;
      dashboard_header.hidden = false;
      canvas.hidden = false;
      draw_chart('bar',canvas.getContext('2d'));
    }
    else{
      myChart.destroy();
      if(current[0].id == "songs"){
        songs_header.hidden = false;
        songs_list.hidden = false;
        playlists_header.hidden = true;
        playlists.hidden = true;
        users_header.hidden = true;
        users_list.hidden = true;
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
        dashboard_header.hidden = true;
        canvas.hidden = true;
      }
    }
  });
}

/*
(function () {
    console.log(items)
    'use strict'
  
    feather.replace()
    
    // Graphs
    
  })()
  */