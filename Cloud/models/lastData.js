
var mongoose = require("mongoose");

var lastDataSchema = new mongoose.Schema({
  lastWatered: String
});

module.exports = mongoose.model("LastData",lastDataSchema);

