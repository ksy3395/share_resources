/*

This file contains the model of the Resources Collection
Use this model to populate the Resources table

*/
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// create a schema
var resourceSchema = new Schema({
  ip_address: { type: String,unique: true},
  ram: { type: Number, required: true, unique: true },
  cores: { type: Number, required: true },
  cpus: Number,
  gpus: Number,
  status: String,
  active_from:{
     type: Date,
     default: Date.now   

  },
  active_to:{
    type: Date,
    default: Date.now

  },
  created_at: {type:Date, default: Date.now},
  updated_at: {type:Date, default: Date.now}
});

// the schema is useless so far
// we need to create a model using it
var resources = mongoose.model('User', resourceSchema);

// make this available to our users in our Node applications
module.exports = resources;
