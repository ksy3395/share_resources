var express = require('express');
var jobsrouter = express.Router();
var mongoose = require('mongoose');
//var Resources = require('../models/resources.js');
var jobs_controller = require('../controllers/jobsController');


/* GET ALL RESOURCES */
jobsrouter.get('/',jobs_controller.getalljobs);

/* GET ALL JOBS BY CUSTOMER_ID OR EMAIL_ID */
jobsrouter.get('/:id',jobs_controller.getjobsbycustomerId);

/* ADD NEW RESOURCES UNDER THE USER ACCOUNT */
jobsrouter.post('/', jobs_controller.addjobsbycustomerId);

/* UPDATE RESOURCE DETAILS */
jobsrouter.put('/:id',jobs_controller.updatejobstatus);

/* DELETE PRODUCT */
jobsrouter.delete('/:id',jobs_controller.deletejobbycustomerid);

module.exports = jobsrouter;
