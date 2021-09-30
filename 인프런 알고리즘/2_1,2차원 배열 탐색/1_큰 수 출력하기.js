function solution(arr) {
  // let arr = [];

  // for (let i = 0; i < n; i++) {
  //   const ran = Math.floor(Math.random() * 100 + 1);
  //   if (arr.indexOf(ran) < 0) {
  //     arr.push(ran);
  //   } else i--;
  // }

  let result = [];

  result.push(arr[0]);

  for (let j = 1; j < arr.length; j++) {
    if (arr[j] > arr[j - 1]) result.push(arr[j]);
  }
  return result;
}

// let n = 6;
let arr = [7, 3, 9, 5, 6, 12];

console.log(solution(arr));

// 문제를 잘못 이해했었다
