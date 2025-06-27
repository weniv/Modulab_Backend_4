# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    # 유저명은 username 필드 (User 모델)
    def clean_username(self):
        # 이 메서드는 유효성 검사 시에 자동으로 호출됩니다.
        username = self.cleaned_data.get("username")
        if username:
            if username in ["trump"]:
                raise ValidationError("허용되지 않은 유저명입니다.")
        return username
