var express       = require('express'),
    app           = express(),
    mongoose        = require("mongoose"),
    bodyParser    = require("body-parser"),
    Weather            = require("./models/weather"),
    LastData            = require("./models/lastData"),
    user = require('./user');
     connect = require('./routes/connect');

app.use('/', connect);


app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static(__dirname + "/public"));

app.set("view engine","ejs");
/*app.use(express.static("images"));*/

mongoose.connect("mongodb://localhost/esiot");

app.get("/",function(req,res){
  res.render("login");
});


app.get("/register",function(req, res){
  res.render("register");
});


app.get("/login", function(req, res){
  res.render("login");
});


 app.use('/',user);




 app.get("/getdata",function(req, res){

  var requestify = require('requestify'); 
console.log("Connecting with API");
requestify.get('http://api.wunderground.com/api/6a959789736ce3a4/conditions/q/CA/thiruvananthapuram.json').then(function(response) {
	// Get the response body
	console.log("Connected");
	//console.log(response.getBody());
	var data = response.getBody();
	data = data.current_observation;
	

  var newDate = new Date();

  var time = newDate.toTimeString().toString().substring(0,8);
  var date = newDate.toLocaleDateString();
  var x = date + " " + time;

	var tempDetails = {
		Temp : data.temp_c,
		Humidity: data.relative_humidity,
		Precipitation: data.precip_today_in,
        Lastdate : x
	}

  console.log(tempDetails);
//write data to the database
     var temp = data.temp_c;
     var humidity = data.relative_humidity;
     var precipitation = data.precip_today_in;
     var lastdate = x;

	 
     var newWeather = {temp: temp, humidity: humidity, precipitation: precipitation, lastdate: lastdate};
     Weather.create(newWeather,function(err,newlyCreated){
        if(err){
          console.log(err);
        }
        else{
         console.log("done");
        }
     });

     res.send(tempDetails);

});


 });




//start server
app.listen(3000,"192.168.31.199",function(req,res){
  console.log("server has been started!!!");
});
