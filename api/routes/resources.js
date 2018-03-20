var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
//var Resources = require('../models/resources.js');
var resources_controller = require(config.CONTROLLERS_PATH+'resourcesController');


/* GET ALL RESOURCES */
router.get('/',resources_controller.getallresources);

/* GET ALL RESOURCES BY CUSTOMER_ID OR EMAIL_ID */
router.get('/:id',resources_controller.getresourcesbycustomerId);

/* ADD NEW RESOURCES UNDER THE USER ACCOUNT */
router.post('/', resources_controller.addresourcebycustomerId);

/* UPDATE RESOURCE DETAILS */
router.put('/:id',resources_controller.updateresourcebycustomerid);

/* DELETE PRODUCT */
router.delete('/:id',resources_controller.deleteresourcebycustomerid);

module.exports = router;
