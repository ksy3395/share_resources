var express = require('express');
var bodyParser = require('body-parser');
//var path= require('path');
config = require('./api/config/config');
var app= express();
var resources = require(config.ROUTES_PATH+'resources');
var jobs = require(config.ROUTES_PATH+'jobs');
var router= express.Router();

//logger middleware
var logger= function(req,res,next){
console.log('Logging....');
next();

}
app.use(logger);
module.exports=app;
//body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));
app.use('/api/v1',router);
router.use('/resources',resources);
router.use('/jobs',jobs);


app.listen(3000,function(){
	console.log('Server started on port 3000');
})