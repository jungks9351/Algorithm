// 내가 한것.

function solution1(n) {
  let das = n / 12;
  let result;
  if (n % 12 === 0) {
    result = das;
  } else {
    result = parseInt(das + 1);
  }
  return result;
}
console.log(solution1(25));

// 풀이
// Math.ceil() 함수는 주어진 숫자보다 크거나 같은 숫자 중 가장 작은 숫자를 정수 로 반환합니다.

function solution2(n) {
  let answer;
  answer = Math.ceil(n / 12);
  return answer;
}

console.log(solution2(178));
