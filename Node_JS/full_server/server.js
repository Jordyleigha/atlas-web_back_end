const express = require('express');

const app = express();

const port = 1245;

const routes = require('./routes/index.js');

app.use('/', routes);

app.listen(port, () => {
    console.log(`listening on port ${port}!`);
});