# accounts/views.py

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from .forms import SignupForm


login = LoginView.as_view(
    template_name="accounts/login_form.html",
)

logout = LogoutView.as_view()


def profile(request):
    return render(request, "accounts/profile.html")


def signup(request):
    if request.method == "GET":
        form = SignupForm()
    else:
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()  # 회원가입 완료 !! 지정 유저 레코드 DB에 저장됨 !!!
            # 회원가입을 했으니, 로그인 페이지로 이동하는 것이 자연스러워요.
            return redirect("/accounts/login/")  # 이 페이지는 아직 없어요.

    return render(request, "accounts/signup_form.html", {
        "form": form,
    })
