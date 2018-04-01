
var mongoose = require("mongoose");

var weatherSchema = new mongoose.Schema({
  temp: String,
  humidity: String,
  precipitation: String,
  lastdate: String

});

module.exports = mongoose.model("Weather",weatherSchema);

