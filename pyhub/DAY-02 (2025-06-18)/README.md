# Day-02 (2025-06-16)

> 💡 **Tip**: git 을 단순히 스토리지로만 사용하지 마셨으면 합니다. 매 실습 시마다 프로젝트 코드를 복제하지마시고, git 로그 기능을 적극 활용해주세요. git 로그 보기에 익숙해지셔야 합니다.

## 참고

+ [위니북스 Django 베이스 캠프](https://www.books.weniv.co.kr/basecamp-django)
+ [Claude Code를 통해 리서치한 Django vs FastAPI](https://claude.ai/public/artifacts/54ef9ef0-a3d9-4b29-a2a0-85b352005731)

## 오늘의 목표

+ [ ] [LLM_CHEATSHEETS.md](../LLM_CHEATSHEETS.md) 참고하여, 다양한 목적으로 LLM을 활용할 수 있다.
    - 보다 많은 예시는 [pyhub-llm 치트시트](https://github.com/pyhub-kr/pyhub-llm/blob/main/CHEATSHEET.md) 참고
+ [ ] 환경변수를 설정하고, 애플리케이션에서 활용할 수 있다.
+ [ ] 장고 프로젝트를 생성하고, View/Urls/Templates/Static 의 역할을 간략하게나마 알고 연결할 수 있다.
+ [ ] HTML Form 혹은 JavaScript Fetch를 통해 HTTP 요청을 보내고 응답을 받아 화면에 적용할 수 있다.
+ [ ] `django-debug-toolbar` 를 설치하고, 디버깅 화면을 확인한다.

## 프로젝트 폴더 생성과 가상환경

> 오늘 실습할 폴더(ex: 날짜폴더)에서 가상환경을 생성해주시고, 활성화해주세요.

> 💡 **Tip**: 윈도우 파워쉘에서 가상환경 활성화 시에 [보안 오류](https://www.books.weniv.co.kr/basecamp-django/chapter01/01-3)가 발생하신다면, 윈도우 기본의 파워쉘을 사용하지 마시고, [파워쉘 코어를 설치](https://learn.microsoft.com/ko-kr/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5해서 활용해보세요.

## 환경변수

환경변수는 애플리케이션의 설정값을 외부에서 관리할 수 있게 해주는 변수입니다. 주요 역할은 다음과 같습니다:

1. **보안성 강화**
    - 민감한 정보(DB 비밀번호, API 키 등)를 코드에 직접 노출하지 않고 관리
    - 개발/테스트/운영 환경별로 다른 설정값 적용 가능

2. **유연한 설정 관리**
    - 환경별(개발/테스트/운영) 설정값 분리
    - 코드 수정 없이 설정값 변경 가능

3. **배포 용이성**
    - 환경별 설정 파일만 교체하여 배포 가능
    - CI/CD 파이프라인에서 환경변수 주입 용이

4. **협업 효율성**
    - 팀원들과 설정값 공유 시 보안 유지
    - `.env.example`을 통한 설정 가이드 제공 가능

### Windows

1. **시스템 환경변수 설정**
    - 제어판 > 시스템 > 고급 시스템 설정 > 환경 변수
    - 시스템 변수에 새로 추가
    - 명령 프롬프트에서는 `setx` 명령어 사용:

```cmd
setx VARIABLE_NAME "value"
```

2. **임시 환경변수 설정**

```cmd
set VARIABLE_NAME=value
```

### macOS/Linux

#### 쉘 환경변수 설정

쉘 사용 시에 자동으로 적용됩니다. 현재 사용쉘은 `echo $SHELL` 명령으로 확인할 수 있습니다.

현재 사용하는 쉘에 맞춰

- bash 쉘인 경우 : `~/.bash_profile` 에 아래 코드 추가하면, 쉘 구동 시에 지정 환경변수 자동 지정
- zsh 쉘인 경우 : `~/.zshrc` 에 아래 코드 추가하면, 쉘 구동 시에 지정 환경변수 자동 지정

```bash
export VARIABLE_NAME="value"
export OPENAI_API_KEY="..."
export UPSTAGE_API_KEY="..."
```

> 💡 **Tip**: `~/.zshrc` 파일 편집은 `code ~/.zshrc` 명령어로 Visual Studio Code를 통해 편집할 수 있습니다. 이렇게 하면 일반 텍스트 에디터보다 더 편리하게 환경변수를 편집할 수 있습니다.

설정 적용:

```bash
source ~/.bash_profile  # 또는 source ~/.zshrc
```

#### **임시 환경변수 설정**

```bash
export VARIABLE_NAME="value"
```

### Python에서 환경변수 사용

#### django-environ을 통한 환경변수 로딩 및 파싱 예시

`.env` 파일 로딩 시에 `python-dotenv` 라이브러리도 많이 쓰지만, 우리는 `django`를 익힐 것이기에
`django` 개발 편의성을 도와주는 `django-environ` 라이브러리를 사용하겠습니다.

1. **requirements.txt** 파일 생성

```
django-environ
```

1. **django-environ 설치**

```bash
python -m pip install -r requirements.txt
```

2. **.env 파일 예시**

> ⚠️ **Warning**: 환경변수 설정 시 등호(=) 앞뒤로 띄어쓰기가 있으면 해당 라인은 무시됩니다.

```
OPENAI_API_KEY="..."
UPSTAGE_API_KEY="..."
```

3. **일반 Python 파일에서 환경변수 사용 예시**

```python
# hello-env.py

import environ
form pathlib import Path

# 현재 소스파일 경로(__file__)의 부모 => 디렉토리 경로
BASE_DIR = Path(__file__).parent
# .env 경로는 프로젝트 상황에 맞춰 다양하게 변경하시거나,
# 여러 .env 경로를 사용해서 로딩하실 수도 있습니다.
env_path = BASE_DIR / ".env"  # Path 객체

env = environ.Env()

# .env 파일이 현재 디렉토리에 있다면, 환경변수로서 로딩합니다.
if env_path.exists():
    print("loading", env_path)
    # 이미 로딩된 환경변수 Key가 할지라도 덮어쓰기(overwrite)로서 동작
    env.read_env(env_path, overwrite=True)

# 지정 Key의 환경변수를 문자열(str)로서 변환하고, 해당 key의 환경변수가 없을 경우 default값을 반환
#  - default 값이 없을 경우 django.core.exceptions.ImproperlyConfigured 예외 발생
OPENAI_API_KEY = env.str('OPENAI_API_KEY', default=None)
UPSTAGE_API_KEY = env.str('UPSTAGE_API_KEY', default=None)

print('OPENAI_API_KEY:', OPENAI_API_KEY)
print('UPSTAGE_API_KEY:', UPSTAGE_API_KEY)
```

- 위 예시는 Django 프로젝트가 아닌 일반 Python 파일에서도 django-environ을 활용해 `.env` 파일의 환경변수를 쉽게 불러올 수 있음을 보여줍니다.
- 실제 서비스 코드에서는 API KEY 등 민감 정보가 노출되지 않도록 주의하세요.

4. `pyhub-llm` 예시에서 `.env` 파일의 API Key 내역을 로딩해서 적용해보세요.

+ [pyhub-llm 치트시트](https://github.com/pyhub-kr/pyhub-llm/blob/main/CHEATSHEET.md)

## django 명령

### django 버전 확인

`django`를 설치하면 `django-admin` 명령이 설치되며, 이는 `python -m django` 명령과 동일합니다.
`django-admin` 명령을 못 찾는 이슈가 발생할 때에는 `python -m django` 명령을 활용해보세요.

```
python -m django --version
```

### 현재 프로젝트에서 지원하는 모든 명령

```
python manage.py --help
```

### 프로젝트 생성

현재 디렉토리(`.`)에 장고 프로젝트 생성

```
python -m django startproject config .
```

### 데이터베이스 생성

```
python manage.py migrate
```

### 슈퍼유저 생성

현재 데이터베이스 상에 슈퍼 유저 생성

```
python manage.py createsuperuser
```

### 장고 개발서버 구동

디폴트로 127.0.0.1 주소에 8000 포트로 구동됩니다.

```
python manage.py runserver

python manage.py runserver 0.0.0.0:8888  # 0.0.0.0 주소로 8888 포트로 listen
```

