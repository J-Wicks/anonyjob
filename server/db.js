const Sequelize = require('sequelize')

const writingSamplesDB = new Sequelize( process.env.DATABASE_URL || 'postgres://localhost:5432/writingsamples', {
	logging: false
})

const anonyjobsDB = new Sequelize(process.env.DATABASE_URL || 'postgres://localhost:5432/anonyjobs-app', {
  logging: false
});


module.exports = {writingSamplesDB, anonyjobsDB}
