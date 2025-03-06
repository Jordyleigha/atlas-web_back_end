import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.connect().then(() => {
    console.log('Redis client connected to the server');
    client.subscribe('holberton school channel', (message) => {
        if (message === 'KILL_SERVER') {
            client.quit();
        } else {
            console.log(message);
        }
    })
});