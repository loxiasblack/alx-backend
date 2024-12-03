const  kue = require('kue')
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '555-123-4567',
  message: 'This is the code to verify your account'
};

const job = queue.create('push_notification_code', jobData)
    .save((err) => {
        if (!err) {
            console.log(`Notification job created: ${job.id}`);
        } else {
            console.log(err);
        }
    });

job.on('complete', () => {
    console.log('Notification job completed');
}).on('failed', () => {
    console.log('Notification job failed');
});

