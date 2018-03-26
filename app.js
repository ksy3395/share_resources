var express = require('express');
var bodyParser = require('body-parser');
// Bring Mongoose into the app
var mongoose = require( 'mongoose' );
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



mongoose.set('bufferCommands', false);

// Build the connection string
var dbURI = 'mongodb://localhost/ShareResources';

// Create the database connection
mongoose.connect(dbURI);
mongoose.Promise = global.Promise;


mongoose.connect(dbURI)
  .then(() =>  console.log('connection succesful'))
  .catch((err) => console.error(err));


// When the connection is disconnected
mongoose.connection.on('disconnected', function () {
  console.log('Mongoose default connection disconnected');
});

// When the connection is open
mongoose.connection.on('open', function () {
  console.log('Mongoose default connection is open');
});

// If the Node process ends, close the Mongoose connection
process.on('SIGINT', function() {
  mongoose.connection.close(function () {
    console.log('Mongoose default connection disconnected through app termination');
    process.exit(0);
  });
});

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