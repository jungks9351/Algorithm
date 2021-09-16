function solution(s) {
  let result = '';
  for (let x of s) {
    if (x === x.toUpperCase()) result += x.toLowerCase();
    else result += x.toUpperCase();
  }
  return result;
}

console.log(solution('StuDY'));
