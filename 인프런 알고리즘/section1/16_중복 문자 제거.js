function solution(s) {
  let result = '';
  for (let i = 0; i < s.length; i++) {
    console.log(s.indexOf(s[i]));
    if (s.indexOf(s[i]) === i) result += s[i];
  }
  return result;
}
console.log(solution('ksekkset'));
