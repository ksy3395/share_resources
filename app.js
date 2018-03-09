var express = require('express');
var bodyParser = require('body-parser');
var path= require('path');
var app= express();
var resources = require('./api/routes/resources');
var router= express.Router();

//logger middleware
var logger= function(req,res,next){
console.log('Logging....');
next();

}
app.use(logger);

//body parser middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));
app.use('/api/v1',router);
router.use('/resources',resources);


app.listen(3000,function(){
	console.log('Server started on port 3000');
})