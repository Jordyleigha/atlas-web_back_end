const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');
const { response } = require('express');

const rl = readline.createInterface({ input, output });

rl.question('Welcome to Holberton School, what is your name?\n', (response) => {
    console.log('Your name is: ${response}');
    console.log('This important software is now closing');
});