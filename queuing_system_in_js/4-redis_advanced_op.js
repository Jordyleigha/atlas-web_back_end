import { print } from "redis";
import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.connect().then(async () => {
    console.log('Redis client connected to the server');
    client.hSet('HolbertonSchools', 'Portland', 50).then((res) => {
        console.log(res);
    });
    client.hSet('HolbertonSchools', 'Seattle', 80).then((res) => {
        console.log(res);
    });
    client.hSet('HolbertonSchools', 'New York', 20).then((res) => {
        console.log(res);
    });
    client.hSet('HolbertonSchools', 'Bogota', 20).then((res) => {
        console.log(res);
    });
    client.hSet('HolbertonSchools', 'Cali', 40).then((res) => {
        console.log(res);
    });
    client.hSet('HolbertonSchools', 'Paris', 2).then((res) => {
        console.log(res);
    });
    
    client.hGetAll('HolbertonSchools').then((result) => {
        console.log(result)
    });
});