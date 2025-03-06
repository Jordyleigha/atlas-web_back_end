const kue = require('kue')
    , queue = kue.createQueue();

const job = queue.create('push_notification_code', {
    phoneNumber: '111-222-3333',
    message: 'Hi there, this is a message!',
  }).save((err) => {
    if (err) {
        console.log('Notification job failed')
    } else {
        console.log(`Notification job created: ${job.id}`)
    }
  });

job.on('complete', () => {
    console.log('Notification job completed');
});