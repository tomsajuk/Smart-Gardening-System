var express = require('express');
var router = express.Router();
var PythonShell = require('python-shell');
var mongoose        = require("mongoose");
Weather            = require("../models/weather");

    
   
router.get("/connect", function(req,res){

console.log('connect')
  
var weatherData = mongoose.model('Weather', weatherData);

  var query = weatherData.find({ });

  query.sort({_id:-1});

  query.limit(1);

  query.exec(function (err, wdata) {
  if (err) return handleError(err);

  if (wdata[0].precipitation <= 5){

  res.send("YES");	
  
  PythonShell.run('server.py', function (err) {
    if (err) throw err;
   console.log('finished');
  });

    

  } else{
    res.send("NO");
  }

  });
 
});


router.get("/manual", function(req, res){
console.log('manual')
  
	PythonShell.run('manual.py', function (err) {
	if (err) throw err;
	console.log('finished');
	});

	var newDate = new Date();
	var time = newDate.toTimeString().toString().substring(0,8);
	var date = newDate.toLocaleDateString();
	var x = date + " " + time;

	var tempD = {
	d : x
	}

	res.send(tempD);

});

module.exports = router;

