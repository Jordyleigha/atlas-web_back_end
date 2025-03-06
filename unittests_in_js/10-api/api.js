const express = require('express');
const app = express();
const port = 7865;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

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

app.get('/available_payments', (req, res) => {
    const payments = {
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      };
    res.status(200).send(payments);
});

app.post('/login', (req, res) => {
    res.status(200).send(`Welcome ${req.body.userName}`);
})

app.listen(port, () => {
    console.log('API available on localhost port 7865');
});