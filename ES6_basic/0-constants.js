// taskFirst.js

const task = 'I prefer const when I can.';

export function taskFirst() {
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();
  return combination;
}