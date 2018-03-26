
/**
 * Return the ratio of the inline text length of the links in an element to
 * the inline text length of the entire element.
 *
 * @param {Node} node - Types or not: either works.
 * @throws {PartyError|Hearty} Multiple types work fine.
 * @returns {Number} Types and descriptions are both supported.
 */

var Resources = require('../models/resources'); 
/* GET ALL RESOURCES */
exports.getallresources = function(req, res) {

 Resources.find(function (err, resources) {
    if (err) return next(err);
    res.json(resources);
  });
};

/* GET ALL RESOURCES BY CUSTOMER_ID OR EMAIL_ID */
exports.getresourcesbycustomerId = function(req, res) {
    res.send('NOT IMPLEMENTED: Book detail: ');
};

/* ADD NEW RESOURCES UNDER THE USER ACCOUNT */
exports.addresourcebycustomerId = function(req, res) {

	//sample method call to add users to the database.

var chris = new User({
  name: 'Chris',
  username: 'sevilayha',
  password: 'password' 
});

chris.save(function(err) {
  if (err) throw err;

  console.log('User saved successfully!');
});

    res.send('User Saved successfully',200);
};

/* UPDATE RESOURCE DETAILS */
exports.updateresourcebycustomerid = function(req, res) {
    res.send('NOT IMPLEMENTED: Book create POST');
};

/* DELETE PRODUCT */
exports.deleteresourcebycustomerid = function(req, res) {
    res.send('NOT IMPLEMENTED: Book delete');
};
