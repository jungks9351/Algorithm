function solution(a, b, c) {
  let result = a;
  if (a > b) {
    result = b;
  }
  if (b > c) {
    result = c;
  }
  return result;
}

console.log(solution(11, 12, 14));
