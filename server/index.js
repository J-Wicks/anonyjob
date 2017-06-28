'use strict';
const express = require('express')
const app = express()
const path = require ('path')
const morgan = require('morgan')
const bodyParser = require ('body-parser')
const writingDB = require('./db').writingSamplesDB;
const appDB = require('./db').anonyjobsDB;


var port = process.env.PORT || 8080;
var server = app.listen(port, function (err) {
  if (err) throw err;
  console.log('HTTP server patiently listening on port', port);
  writingDB.sync()
  .then(function () {
    console.log('Oh and btw the postgres server is totally connected, too');
  })
  .then(function() {
    appDB.sync()
  });
});

app.use(morgan('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}))

app.use('/', express.static(path.join(__dirname + '/../public')))

app.get('/data-form', function (req, res) {
  res.sendFile(path.join(__dirname, '../public/data-collection.html'))
})

app.use('/api', require('./api'))

app.get('*', function (req, res) {
	res.sendFile(path.join(__dirname,'../public/index.html'))
})

// app.use(function (err, req, res, next) {
//   console.error(err);
//   console.error(err.stack);
//   res.status(err.status || 500).send(err.message || 'Internal server error.');
// });

module.exports = server;
