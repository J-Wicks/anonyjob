const db = require('../db').anonyjobsDB;
const Sequelize = require('sequelize');

const Application = db.define('application', {
	coverLetter: {
		type: Sequelize.TEXT,
		allowNull: false,
		unique: true
	}
})


module.exports = Application;
