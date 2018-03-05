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
router.use('/resources',resources);
app.use('/api/v1',router);
//app.get('/',function(req,res){

//res.send('Hello World');

//});

app.listen(3000,function(){
	console.log('Server started on port 3000');
})