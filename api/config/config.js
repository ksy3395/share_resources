/* This file has the below configuration settings:
	1. MONGODB Connection Settings
	2. Global Paths to avoid hard coding in every file.
	3. Third Party SECRET KEYS

 */

var config = {};

//Config parameters of the database.
config.MONGO_DB_URI="mongodburi";
config.DATABASE="SHARE_RESOURCES";

// Config for the PATHS. Make sure to check the below paths that are commonly used.
config.ROUTES_PATH="./api/routes/";
config.CONTROLLERS_PATH="../controllers/";
config.MODELS_PATH="./api/models/";
config.APPLICATION_CONFIG="./config/";

module.exports = config;