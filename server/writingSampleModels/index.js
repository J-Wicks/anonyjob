const db = require('../db.js').writingSamplesDB
const Sequelize = require('sequelize')

const User = db.define('user', {
	age: {type: Sequelize.INTEGER},
	degree: {type: Sequelize.STRING},
	workYrs: {type: Sequelize.INTEGER},
	mgmtYrs: {type: Sequelize.INTEGER},
	execYrs: {type: Sequelize.INTEGER},
	writing: {type: Sequelize.TEXT}
})

const Gender = db.define('gender', {
	name: { type: Sequelize.STRING}
})

const Orientation = db.define('orientation', {
	name: { type: Sequelize.STRING}
})

const Race = db.define('race', {
	name: { type: Sequelize.STRING}
})

User.belongsTo(Gender)
User.belongsTo(Orientation)
User.belongsTo(Race)

Gender.hasMany(User)
Orientation.hasMany(User)
Race.hasMany(User)

module.exports = {User, Gender, Orientation, Race}
