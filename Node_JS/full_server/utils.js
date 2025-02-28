const fs = require('fs').promises;

export async function readDatabase(path) {
  if (!path) {
    console.log('path invalid')
    throw 'Cannot load the database';
  }
  try {
    const content = await fs.readFile(path, 'utf-8');
    const lines = content.split('\n');
    const studentFields = {};
    let index = 0;
    for (const line of lines) {
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