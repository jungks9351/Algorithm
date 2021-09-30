function solution(s, t) {
  let result = s.split(t).length;
  return result - 1;
}

let str = 'COMPUTERPROGRAMMING';
console.log(solution(str, 'R'));
