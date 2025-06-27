# accounts/views.py

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()  # 회원가입 완료 !! 지정 유저 레코드 DB에 저장됨 !!!
            # 회원가입을 했으니, 로그인 페이지로 이동하는 것이 자연스러워요.
            return redirect("/accounts/login/")  # 이 페이지는 아직 없어요.

    return render(request, "accounts/signup_form.html", {
        "form": form,
    })
