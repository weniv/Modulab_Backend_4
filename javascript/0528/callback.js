// 비동기 제어
// const user = {};

// setTimeout(() => {
//     user.name = "weniv";
// }, 0);

// console.log(user);

// 콜백함수
const user = {};

// function setUser(callback) {
//     setTimeout(() => {
//         user.name = "weniv";
//         callback(user);
//     }, 0);
// }

function printUser(user) {
    console.log(user);
}

// setUser(printUser);
// setUser((user) => console.log(user));

function setUser(callback) {
    setTimeout(() => {
        user.name = "weniv";
        user.age = 20;
        callback(user);
    }, 0);
}

function printUser(user) {
    console.log(user);
}

function roleCheck(user, callback) {
    setTimeout(() => {
        if (user.age >= 20) {
            user.role = "성인";
        } else {
            user.role = "학생";
        }
        callback(user);
    }, 1000);
}

setUser((user) => roleCheck(user, printUser));

// 콜백 지옥
// func1(function (result1) {
//     func2(result1, function (result2) {
//         func3(result2, function (result3) {
//             // 계속되는 중첩...
//         });
//     });
// });

// 문제 1

// 1단계: 기본 주문 처리

// 주문접수(음식명, 고객명, 콜백함수) 함수 구현
// 1초 후 "주문이 접수되었습니다" 메시지 출력
// 완료 후 콜백 함수 실행

// 2단계: 음식 준비

// 음식준비(음식명, 콜백함수) 함수 구현
// 2초 소요, 준비 완료 메시지 출력
// 완료 후 콜백 함수 실행

// 3단계: 배달 시작

// 배달시작(주소, 콜백함수) 함수 구현
// 3초 소요, 배달 완료 메시지 출력
// 완료 후 콜백 함수 실행

// 4단계: 전체 과정 연결

// 위 3단계를 순서대로 실행하는 코드 작성
// "피자", "서울시 강남구"로 테스트
// 마지막에 "배달 완료!" 메시지 출력

// 피자 주문이 접수되었습니다
// 피자 준비가 완료되었습니다
// 서울시 강남구로 배달을 시작합니다
// 배달이 완료되었습니다
// 배달 완료!

function 주문접수(음식명, callback) {
    console.log(`${음식명} 주문이 접수되었습니다`);
    setTimeout(() => {
        callback(음식명);
    }, 1000);
}

function 음식준비(음식명, callback) {
    console.log(`${음식명} 준비가 완료되었습니다`);
    setTimeout(() => {
        callback();
    }, 2000);
}

function 배달시작(주소, callback) {
    console.log(`${주소}로 배달을 시작합니다`);
    setTimeout(() => {
        console.log("배달이 완료되었습니다");
        callback();
    }, 3000);
}

주문접수("피자", (음식명) => {
    음식준비(음식명, () => {
        배달시작("서울시 강남구", () => {
            console.log("배달 완료!");
        });
    });
});
