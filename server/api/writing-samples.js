const router = require('express').Router();
const User = require('../appDBModels').User
const Gender = require('../appDBModels').Gender
const Orientation = require('../appDBModels').Orientation
const Race = require('../appDBModels').Race

router.get('/', function(req, res, next){
	res.status(200).send('good job hitting the route, but i\'m not going to send you any of our user data')
})

router.get('/allData', function(req, res, next) {
	User.findAll(
		{include:
	[{model: Gender}, {model: Race}, {model: Orientation}]
	})
.then(foundUsers => {
	const usersPack = []
	foundUsers.forEach( user => {

		let newUser ={
			gender: user.gender.name,
			orientation: user.orientation.name,
			race: user.race.name,
			writing: user.writing
		}
		usersPack.push(newUser)
	})

	res.status(200).json(usersPack)
	})
	.catch( err => {
		res.send(err)
	})
})

router.get('/gender', function(req, res, next){
	Gender.findAll()
	.then( foundGenders => {
		res.send(foundGenders)
	})
})

router.get('/race', function(req, res, next){
	Race.findAll()
	.then( foundRaces => {
		res.send(foundRaces)
	})
})

router.get('/orientation', function(req, res, next){
	Orientation.findAll()
	.then( foundOrientations => {
		res.send(foundOrientations)
	})
})

router.post('/', (req, res, next) => {
	User.create({
		age: req.body.age,
		race: req.body.race,
		writing: req.body.writingSample,
	})
	.then( createdUser => {
		Gender.findOrCreate({where: {name: req.body.gender}})
		.spread( (gender, created) => {
			gender.addUser(createdUser)
		})
		Orientation.findOrCreate({where: {name: req.body.orientation}})
		.spread( (orientation, created) => {
			orientation.addUser(createdUser)
		})
		Race.findOrCreate({where: {name: req.body.race}})
		.spread ((race, created)=>{
			race.addUser(createdUser)
		})
	})
	res.status(200).send('Database Row Added')
})
module.exports = router
