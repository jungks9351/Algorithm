// Array.from() 메서드는 유사 배열 객체(array-like object)나 반복 가능한 객체(iterable object)를 얕게 복사해 새로운Array 객체를 만듭니다. (MDN)

// 유사 배열 객체를 변환하여 배열을 생성한다.
//Array.from({ length: 2, 0: 'a', 1: 'b' });
// --> ['a', 'b']

//이터러블을 변환하여 배열을 생성한다. 문자열은 이터러블이다.
//Array.from('Hello');
// --> ['H', 'e', 'l', 'l', 'o']

// Array.from은 두 번째 인수로 전달한 콜백 함수의 반환값으로 구성된 배열을 반환한다.

// Array.from({ length: 3}, (_, i) => i);
// [0, 1, 2]

function solution(arr) {
  let n = arr.length;
  let result = Array.from({ length: n }, () => 1);
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (arr[j] > arr[i]) result[i]++;
    }
  }
  return result;
}

let arr = [87, 89, 92, 100, 76];
console.log(solution(arr));
