const axios = require('axios');
const { expect, assert } = require('chai');

describe('Payment API index', () => {
    it('should return a successful status code and the landing message', () => {
        axios.get('localhost:7865/').then((res) => {
            assert.equal(res.status, 200);
            assert.equal(res.data, 'Welcome to the payment system');
        });
    });
});

describe('Payment API cart', () => {
    it('should return a successful status code with a valid id', () => {
        axios.get('localhost:7865/cart/12').then((res) => {
            assert.equal(res.status, 200);
            assert.equal(res.data, 'Payment methods for cart 12');
        });
    });
    it('should return a 404 status with an invalid id', () => {
        axios.get('localhost:7865/cart/twelve').then((res) => {
            assert.equal(res.status, 404);
            assert.equal(res.data, 'Not found');
        });
    });
});

describe('Payment API login route', () => {
    it('should accept a user name, then welcome that user', () => {
        axios.post('localhost:7865/login', {
            userName: 'Chuck'
        }).then((res) => {
            assert.equal(res.data === 'Welcome Chuck');
        });
    });
});

describe('Payment API payments route', () => {
    it('should return an object listing valid payments', () => {
        axios.get('localhost:7865/payments').then((res) => {
            assert.equal(res.credit_cards, true);
            assert.equal(res.paypal, false);
        });
    });
});