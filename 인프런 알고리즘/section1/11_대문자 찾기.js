function solution(s) {
  let result = 0;
  for (let x of s) {
    if (x === x.toUpperCase()) result++;
  }

  return result;
}

let str = 'KoreaTimeGood';
console.log(solution(str));
