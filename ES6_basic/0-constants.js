// taskFirst.js

export function taskFirst() {
    const task = 'I prefer "const" when I can.'; // Added quotes around the string
    return task;
  }
  
  export function getLast() {
    return ' is okay';
  }
  
  export function taskNext() {
    let combination = 'But sometimes "let"'; // Added quotes around the string
    combination += getLast();
    return combination;
  }