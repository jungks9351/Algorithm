// 7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 고른 홀수들 중 최소값을 찾는 프로그램을 작성하세요.

// 내가 한것

function solution1(arr) {
  let sum = 0;
  let odd = [];
  let min;
  arr.forEach((item) => {
    if (item % 2 === 0) return;
    sum += item;
    odd.push(item);
  });
  min = odd.sort((a, b) => a - b)[0];

  const result = `${sum} \n ${min}`;

  return result;
}

let arr1 = [12, 77, 38, 41, 53, 92, 85];
console.log(solution1(arr1));

// 풀이
// for...of

function solution2(arr) {
  let answer = [];
  let sum = 0,
    min = 1000;
  for (let x of arr) {
    if (x % 2 === 1) {
      sum += x;
      if (x < min) min = x;
    }
  }
  answer.push(sum);
  answer.push(min);
  return answer;
}

let arr2 = [12, 77, 38, 41, 53, 92, 85];
console.log(solution2(arr2));
