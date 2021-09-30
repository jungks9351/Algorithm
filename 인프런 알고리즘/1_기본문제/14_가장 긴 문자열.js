function solution(s) {
  let result = '',
    max = Number.MIN_SAFE_INTEGER;
  for (let x of s) {
    if (x.length > max) {
      max = x.length;
      result = x;
    }
  }
  return result;
}
let str = ['teacher', 'time', 'student', 'beautiful', 'good'];
console.log(solution(str));
