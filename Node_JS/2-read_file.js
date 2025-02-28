const fs = require('fs');

function countStudents(path) {
  try {
    const fileContents = fs.readFileSync(path, 'utf-8');
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
    console.log(`Number of students: ${index}`);
    for (const [key, value] of Object.entries(studentFields)) {
      const fieldList = [];
      for (const student of value) {
        fieldList.push(student.first);
      }
      console.log(`Number of students in ${key}: ${value.length}. List: ${fieldList}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;