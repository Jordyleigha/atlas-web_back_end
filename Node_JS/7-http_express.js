const express = require('express');
const fs = require('fs');
const readline = require('node:readline');
const process = require('process');

const db = process.argv[2];

const app = express();

const port = 1245;

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    await countStudents(db)
      .then((data) => {
        let returnLine = ''
        const lineOne = 'This is the list of our students\n';
        returnLine = lineOne;
        let listLines = ''
        let index = 0;
        for (const [key, value] of Object.entries(data)) {
          index += value.length;
          const fieldList = [];
          for (const student of value) {
            fieldList.push(student.first);
          }
          fieldLine = `Number of students in ${key}: ${value.length}. List: ${fieldList}\n`;
          listLines += fieldLine;
        }
        const lineTwo = `Number of students: ${index}\n`;
        returnLine += lineTwo;
        returnLine += listLines;
        res.send(returnLine);
      });
  } catch(error) {
    console.log(error);
    res.send('Cannot load the database');
  }
})

app.listen(port, () => {
  console.log('listing on port '+port);
});

module.exports = app;


async function countStudents(path) {
  if (!path) {
    throw 'Cannot load the database';
  }
  try {
    const fileStream = fs.createReadStream(path);
    const rl = readline.createInterface({ input: fileStream });

    const studentFields = {};
    let index = 0;
    for await (const line of rl) {
      const data = line.split(',');
      if (index > 0 && line !== '') {
        const newStudent = {
          first: data[0],
          last: data[1],
          age: data[2],
          field: data[3],
        };
        if (!(newStudent.field in studentFields)) {
          studentFields[newStudent.field] = [newStudent];
        } else {
          studentFields[newStudent.field].push(newStudent);
        }
      }
      if (line !== '') {
        index += 1;
      }
    }
    index -= 1;
    return studentFields;
  } catch (error) {
    console.log(error)
    throw 'Cannot load the database';
  }
}