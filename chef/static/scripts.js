// configure eslint
/*eslint-env jquery*/
/* global L:false */

var mymap;
var country;

// execute when the DOM is fully loaded
$(function () {

    mymap = L.map('mapid').setView([51.505, -0.09], 2);

    L.tileLayer('https://api.mapbox.com/styles/v1/capp88/cjb42s7nm0bdd2rmsgotqsc15/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiY2FwcDg4IiwiYSI6ImNqYjE2NDV0ejgxYW0yd3A4eTRvZGN5aDAifQ.dALOOghO3sHg8Wa1gnbR3Q', {
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 18,
        zoom: 2
    }).addTo(mymap);
    
    var myStyle = {
        "weight": 0,
        "opacity": 0,
        fillOpacity: 0
    };

    $.getJSON('https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson', function(data) {
      var geojson = L.geoJson(data, {style: myStyle}).addTo(mymap);
    
        geojson.eachLayer(function (layer) {
            layer.bindPopup((country = layer.feature.properties.name) + '<div class="row"><button type="button" id="recipes-button" class="btn btn-default" data-toggle="modal" data-target="#myModal" onclick="showRecipes(country)">Show recipes</button>');
        });
    });

});

function showRecipes(country) {
	$.getJSON(Flask.url_for("recipes"), "country=" + country)
	.done(function( data, textStatus, jqXHR ){

		// iterate over array of objects and create HTML template
		$.each(data, function(i, {link, title}) {
			console.log('test', data);
			content += ( "<li><a href='" + data[i].link + "'>" + data[i].title + "</a></li>" );
			if (i === 4) {
				return false;
			}
		})
		// close tag
		content += "</ul>";
	})
	.fail(function(jqXHR, textStatus, errorThrown) {

		// log error to browser's console
		console.log(errorThrown.toString());
		}
	);
}