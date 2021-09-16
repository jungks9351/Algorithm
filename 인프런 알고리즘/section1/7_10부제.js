// 주어진 날짜와 자동차의 일의 자리 숫자를 보고 10부제를 위반하는 차량의 대수를 출력합니다.

// 내 풀이

function solution(day, arr) {
  let result = 0;
  arr.forEach((car) => {
    if (car % 10 === day % 10) {
      result += 1;
    }
  });
  return result;
}

let arr1 = [25, 23, 11, 47, 53, 17, 33];
let arr2 = [12, 20, 54, 30, 87, 91, 30];
console.log(solution(7, arr1));
console.log(solution(30, arr2));

// 풀이
// 풀이가 잘못된거 같다.

function solution2(day, arr) {
  let answer = 0;
  for (let x of arr) {
    if (x % 10 == day) answer++;
  }

  return answer;
}

let arr3 = [25, 20, 11, 40, 53, 17, 33];
console.log(solution2(20, arr3));
