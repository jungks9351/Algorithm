function solution(s) {
  let result = '';
  for (let x of s) {
    if (x == 'A') {
      result += '#';
    } else {
      result += x;
    }
  }
  return result;
}

let str = 'BANANA';
console.log(solution(str));
