import { createClient } from "redis";
import { print } from "redis";

const client = createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.connect().then(() => {
    console.log('Redis client connected to the server');
    displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    displaySchoolValue('HolbertonSanFrancisco');
});

async function setNewSchool(schoolName, value) {
    const res = await client.set(schoolName, value);
    console.log(res);
}

async function displaySchoolValue(schoolName) {
    const res = await client.get(schoolName);
    console.log(res);
}