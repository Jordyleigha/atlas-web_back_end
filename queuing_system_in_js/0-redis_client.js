import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.connect().then(() => {
    console.log('Redis client connected to the server');
});