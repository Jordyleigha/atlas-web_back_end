const express = require('express');
const app = express();
const port = 7865;

app.get('/', (req, res) => {
    res.status(200).send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
    const reMatch = /^\d+$/;
    const id = req.params.id
    if (id.match(reMatch)) {
        res.status(200).send(`Payment methods for cart ${id}`);
    } else {
        res.status(404).send('Not found');
    }
});

app.listen(port, () => {
    console.log('API available on localhost port 7865');
});