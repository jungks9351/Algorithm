function solution(s) {
  let result;
  let mid = Math.floor(s.length / 2);
  if (s.length % 2 === 1) result = s.substring(mid, mid + 1);
  else result = s.substring(mid - 1, mid + 1);

  return result;
}
console.log(solution('study'));
