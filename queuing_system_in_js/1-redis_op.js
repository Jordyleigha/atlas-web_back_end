import { createClient } from "redis";

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
    client.set(schoolName, value).then((res) => {
        console.log(res);
    });
}

async function displaySchoolValue(schoolName) {
    client.get(schoolName).then((res) => {
        console.log(res);
    });
}