function solution(s) {
  let result;
  //console.log(s.indexOf("student"));
  result = s.filter((v, i) => {
    //console.log(v, i);
    if (s.indexOf(v) === i) return v;
  });

  return result;
}
let str = ['good', 'time', 'good', 'time', 'student'];
console.log(solution(str));
