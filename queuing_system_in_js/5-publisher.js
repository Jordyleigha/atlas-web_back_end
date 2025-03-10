import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.connect().then(() => {
    console.log('Redis client connected to the server');
    publishMessage("Holberton Student #1 starts course", 100);
    publishMessage("Holberton Student #2 starts course", 200);
    publishMessage("KILL_SERVER", 300);
    publishMessage("Holberton Student #3 starts course", 400);
});

function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`)
        client.publish('holberton school channel', message);
    }, time);

}