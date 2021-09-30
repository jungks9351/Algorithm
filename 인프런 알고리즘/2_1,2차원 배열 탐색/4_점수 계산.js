function solution(arr) {
  let result = 0;
  let count = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 1) {
      count++;
      result += count;
    } else count = 0;
  }

  return result;
}

let arr = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0];
console.log(solution(arr));

// 정답 for of 문 사용

function solution2(arr) {
  let answer = 0,
    cnt = 0;
  for (let x of arr) {
    if (x === 1) {
      cnt++;
      answer += cnt;
    } else cnt = 0;
  }

  return answer;
}

console.log(solution2(arr));
