
function createPushNotificationJobs(jobs, queue) {
    if (!(Array.isArray(jobs))) {
        throw new Error('Jobs is not an array');
    }
    for (const job of jobs) {
        const queuedJob = queue.create('push_notification_code_3', job).save(() => {
            console.log(`Notification job created: ${queuedJob.id}`)
        });

        queuedJob.on('progress', (progress) => {
            console.log(`Notification job ${queuedJob.id} ${progress}% complete`)
        });
        queuedJob.on('complete', () => {
            console.log(`Notification job ${queuedJob.id} completed`);
        });
        queuedJob.on('failed', (errorMessage) => {
            console.log(`Notification job ${queuedJob.id} failed: ${errorMessage}`)
        });
    }
}

module.exports = createPushNotificationJobs;