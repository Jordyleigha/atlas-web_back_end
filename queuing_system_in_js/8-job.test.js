const expect = require('chai').expect;
const sinon = require('sinon');
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';


const failedData = "I am not an array";
const validData = [
    {
        phoneNumber: '4154318781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4151218782',
        message: 'This is the code 4321 to verify your account'
    }
]

describe('createPushNotificationJobs', () => {
    let spy = null;
    const queue = kue.createQueue();
    beforeEach(function() {
        spy = sinon.spy(console, 'log');
    });
    before(() => {
        queue.testMode.enter();
    });
    afterEach(() => {
        queue.testMode.clear();
        sinon.restore();
    });
    after(() => {
        queue.testMode.exit();
    });
    it('should fail if a datatype besides an Array is passed', () => {
        expect(createPushNotificationsJobs.bind(createPushNotificationsJobs, failedData, queue)).to.throw('Jobs is not an array');
    });
    it('should create two jobs successfully', () => {
        expect(createPushNotificationsJobs.bind(createPushNotificationsJobs, validData, queue)).to.not.throw('Jobs is not an array');
    });
})