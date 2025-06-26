// 이 파일은 장고 외적으로
// 웹브라우저가 아닌 nodejs 라는 별도의 js runtime 으로 실행.

// 1) await를 사용하는 방식 : async 함수 내에서만 사용
async function main1() {
  try {
    const res = await fetch("http://127.0.0.1:8000/baemin/1/");
    const text = await res.text();
    console.log("text :", text);
  }
  catch(error) {
    console.error(error);
  }
}
// main1();


function main2() {
  fetch("http://127.0.0.1:8000/baemin/1/")
    .then((res) => res.text())   // 정상처리 되었을 때 호출되는 함수를 지정.
    .then(text => {
      console.log("text :", text);
    })
    .catch((error) => {
      console.error(error);
    });  // 오류상황일 때 호출되는 함수를 지정
}
main2();
