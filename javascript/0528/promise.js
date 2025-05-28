// const promise = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         // resolve("요청 성공");
//         reject("요청 실패");
//     }, 1000);
// });

// promise.then((response) => {
//     console.log(response);
// });

// promise
//     .then((response) => {
//         console.log(response);
//     })
//     .catch((error) => {
//         console.log(error);
//     })
//     .finally(() => {
//         console.log("프로미스 종료!");
//     });

const user = {};

function setUser() {
    return new Promise((resolve) => {
        setTimeout(() => {
            user.name = "weniv";
            user.age = 20;
            resolve(user);
        }, 0);
    });
}

function printUser(user) {
    console.log(user);
}

function roleCheck(user) {
    return new Promise((resolve) => {
        setTimeout(() => {
            if (user.age >= 20) {
                user.role = "성인";
            } else {
                user.role = "학생";
            }
            resolve(user);
        }, 0);
    });
}

// setUSer((user) => roleCheck(user, printUser));

// setUser().then((response) => console.log(response));
// setUser()
//     .then(roleCheck)
//     .then((user) => console.log(user));

setUser().then(roleCheck).then(printUser);
