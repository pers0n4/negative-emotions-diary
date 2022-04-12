async function submitSignIn(event) {
  event.preventDefault();

  const formData = new FormData(event.target);

  const response = await fetch("/auth/token", {
    method: "POST",
    body: formData,
  });

  if (response.ok && response.status === 200) {
    alert("로그인에 성공했습니다.");
  } else {
    alert("로그인에 실패했습니다.");
  }
}

async function submitSignUp(event) {
  event.preventDefault();

  const formData = new FormData(event.target);

  if (formData.get("password") !== formData.get("password_confirmation")) {
    alert("패스워드가 일치하지 않습니다.");
    return;
  }

  const response = await fetch("/users", {
    method: "POST",
    body: JSON.stringify({
      email: formData.get("email"),
      password: formData.get("password"),
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok && response.status === 201) {
    alert("회원가입이 완료되었습니다.");
    window.location.href = "/";
    return;
  }
  alert(`${response.status} ${response.statusText}`);
}
