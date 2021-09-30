function solution(s) {
  let result = '';
  for (let x of s) {
    let num = x.charCodeAt();
    if (num >= 97 && num <= 122) result += String.fromCharCode(num - 32);
    else result += x;
  }

  return result;
}

let str = 'ItisTimeToStudy';
console.log(solution(str));
