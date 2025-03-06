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
        })
    })
});