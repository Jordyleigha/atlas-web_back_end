export default function taskBlock(trueOrFalse) {
    let task = false;
    let task2 = true;
  
    if (trueOrFalse) {
      let taskLocal = true;
      let task2Local = false;
  
      task = taskLocal;
      task2 = task2Local;
    }
  
    return [task, task2];
  }