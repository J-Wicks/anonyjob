// const router = require('express').Router();
//
// router.use('/applications', require('./applications'));
// router.use('/companies', require('./companies'));
// router.use('/postings', require('./postings'));
// router.use('/login', require("./login"));
// router.use('/auth', require('./auth'));
// router.use('/users', require('./users')); // matches all requests to /api/users/
//
// router.use(function (req, res, next) {
//   const err = new Error('Not found.');
//   err.status = 404;
//   next(err);
// });
//
// module.exports = router;


const router = require('express').Router();

router.get('/', function(req, res, next){
	res.status(200).send('good job hitting the route, but i\'m not going to send you any of our user data')
})

router.use('/writing-samples', require('./writing-samples'))
router.use('/applications', require('./applications'));
router.use('/companies', require('./companies'));
router.use('/users', require('./users')); // matches all requests to /api/users/
router.use('/postings', require('./postings'));
router.use('/login', require("./login"));
// router.use('/auth', require('./auth'));
//
// router.use('/', function (req, res, next) {
//   const err = new Error('Not found.');
//   err.status = 404;
//   next(err);
// });

module.exports = router
