function readFormData(target = "form") {
  return new FormData(document.querySelector(target));
}

document.addEventListener("DOMContentLoaded", () => {
  const signInButton = document.querySelector("#sign-in");
  const signUpButton = document.querySelector("#sign-up");

  signInButton.addEventListener("click", signInButtonClickHandler);
  signUpButton.addEventListener("click", signUpButtonClickHandler);
});

async function signInButtonClickHandler(event) {
  event.preventDefault();

  const body = readFormData();
  const response = await fetch("/auth/token", {
    method: "POST",
    body,
  });

  if (response.ok) {
    alert("로그인 성공");
  } else {
    alert("로그인 실패");
  }
}

async function signUpButtonClickHandler(event) {
  event.preventDefault();

  const body = readFormData();
  const response = await fetch("/users", {
    method: "POST",
    body: JSON.stringify(Object.fromEntries(body.entries())),
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    alert("가입 성공하였습니다");
  } else {
    alert("이미 가입되었습니다");
  }
}
