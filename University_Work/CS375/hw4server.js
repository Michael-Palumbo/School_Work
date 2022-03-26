
// imports express
var express = require("express");
var request = require("request");

// creates an instance of express server
var app = express();

AERIS_ID = "atxWOzRRE4DHADahStr7g";
AERIS_Key = "m5c6zHwsCpL3ITOzU8WoFzyredFLBK0t9MruheIf";

app.use(express.static("public"));

app.get("/getweather", function (req, res) {
	let lat = req.query.lat;
	let lon = req.query.lon;

	let url = `https://api.aerisapi.com/forecasts/${lat},${lon}?&format=json&filter=day&limit=7&client_id=${AERIS_ID}&client_secret=${AERIS_Key}`;
	request(url, {json: true}, function( err, api_res, data) {
		if(api_res.statusCode == 200){
			if(data.success){
				res.send(api_res);
			}
		}else{
			res.send(err);
		}
	});
});
	

app.listen(8080);

