const http = require('http');
const url = require('url');
const process = require('process');
const fs = require('fs');

const db = process.argv[2];

const app = http.createServer((req, res) => {
  const reqUrl = url.parse(req.url).pathname;
  if (reqUrl === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (reqUrl === '/students') {
    try {
      const fileContents = fs.readFileSync(db, 'utf-8');
      const studentFields = {};
      let index = 0;
      fileContents.split(/\r?\n/).forEach((line) => {
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
      });
      index -= 1;
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${index}\n`);
      for (const [key, value] of Object.entries(studentFields)) {
        const fieldList = [];
        for (const student of value) {
          fieldList.push(student.first);
        }
        res.write(`Number of students in ${key}: ${value.length}. List: ${fieldList}\n`);
      }
      res.end();
    } catch (error) {
      res.write('Cannot load the database');
    }
  }
});

app.listen(1245, () => {
  console.log('listing on 1245!');
});