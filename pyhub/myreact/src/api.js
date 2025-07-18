async function loadProfile() {
    const config = { credentials: "include" };
    const res = await fetch("http://localhost:8000/accounts/api/v1/profile/", config);
    console.log("res :", res);
    const profile = await res.json();
    console.log(profile);
}

export {
    // "loadProfile": loadProfile,
    // loadProfile: loadProfile,
    loadProfile,
};
