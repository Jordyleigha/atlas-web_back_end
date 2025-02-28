import { readDatabase } from "../utils";
const process = require('node:process');

export class StudentsController {

  static async getAllStudents(req, res) {
    const db = process.argv[2];
    try {
      await readDatabase(db)
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
            const fieldLine = `Number of students in ${key}: ${value.length}. List: ${fieldList}\n`;
            listLines += fieldLine;
          }
          const lineTwo = `Number of students: ${index}\n`;
          returnLine += lineTwo;
          returnLine += listLines;
          res.status(200).send(returnLine);
        });
    } catch(error) {
      console.log(error)
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const db = process.argv[2];
    const major = req.params.major;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
    } else {
      try {
        await readDatabase(db)
          .then((data) => {
            let returnLine = '';
            for (const [key, value] of Object.entries(data)) {
              const fieldList = [];
              if (key === major) {
                for (const student of value) {
                  console.log(student.first);
                  fieldList.push(student.first);
                }
              }
              console.log("fieldList: "+fieldList);
              if (fieldList.length > 0) {
                const fieldLine = `List: ${fieldList}\n`;
                returnLine = fieldLine;
              }
            }
            res.status(200).send(returnLine);
          })
      } catch(error) {
        console.log(error)
        res.status(500).send('Cannot load the database');
      }
    }
  }
}