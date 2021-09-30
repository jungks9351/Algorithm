// 숫자 각자리 수 구하기

function solution(num) {
  result = [];
  numLength = num.toString().length;
  for (let i = numLength; i > 0; i--) {
    result.push(parseInt((num % 10 ** i) / 10 ** (i - 1)));
  }
  return result;
}

let num = 94321;
console.log(solution(num));
