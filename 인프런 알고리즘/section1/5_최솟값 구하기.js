// 내가 한 것
// arr.sort((a, b) => a - b) 오름차순
// arr.sort((a, b) => b - a) 내림차순
function solution1(arr) {
  const result = arr.sort((a, b) => a - b).slice(0, 1)[0];
  return result;
}

let arr1 = [5, 7, 3, 1, 9, 30];
console.log(solution1(arr1));

// 풀이
// Number.MAX_SAFE_INTEGER 상수는 JavaScript에서 안전한 최대 정수값을 나타냅니다. (2^53 - 1).

function solution2(arr) {
  let answer,
    min = Number.MAX_SAFE_INTEGER;
  // console.log(min);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < min) min = arr[i];
  }
  answer = min;
  return answer;
}

let arr2 = [5, 7, 3, 20, 9, 11];
console.log(solution2(arr2));
