const express = require('express');

const app = express();

const port = 1245;

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
})

app.listen(port, () => {
  console.log('listing on port '+port);
});

module.exports = app;