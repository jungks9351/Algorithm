function solution(arr) {
  let max = 0;
  let count = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
      count++;
      max = arr[i];
    }
  }
  return count;
}

let arr = [130, 135, 148, 140, 145, 150, 150, 153];

console.log(solution(arr));

// 정답

function solution2(arr) {
  let answer = 1,
    max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      answer++;
      max = arr[i];
    }
  }
  return answer;
}
