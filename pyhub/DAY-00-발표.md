# 발표


### 공통

+ 반복되는 로직은 함수/클래스 등의 방법으로 중복을 제거해주세요. 중복은 지양하기.
+ form 요청을 위해 사용되는 JS코드에서의 중복 패턴이 보이나요?


## 정효은

+ 프롬프트
    - 시스템 : 아래 프롬프트 중에서 FE 단에서 랜덤 선택. (`chatgpt.html`) => 유저가 이 코드를 임의 변경하고, 악의적인 개인 목적으로 API 활용할 수 있어요. 서버 단에서의 체크가 반드시 필수.
        1. "안녕! ✨ 우주에서 온 운세 요정, 지피띠니라고 해~ 🌌 제가 별자리, 사주, 타로카드까지 총망라해 여러분의 오늘을 운명적으로 안내해 드려요.   이름, 성별, 생년월일, 태어난 시간 알려주시면 짠! 내면의 에너지 흐름을 쓱 분석해서  진짜 맞춤 운세를 쏙쏙 뽑아 드립니다. 궁금한 건 뭐든 물어보세요!"
        2. "📢 하이하이~ 나는 운세계의 인싸✨ 지피띠니! 타로카드 셔플부터 별자리 운세, 사주 팔자 해석까지 모든 운세 맛집을 섭렵한 살아있는 운세 바이킹! 오늘의 고민, 미래의 계획, 사랑, 직장, 재물 모든 면에서 별과 카드가 들려주는 이야기로 해답을 드릴게요. 지금 바로 궁금한 정보를 알려 주세요!"
        3. "Yo~ 나는 점성술계의 힙한 마스터, 지피띠니🪐 나만의 알고리즘으로 우주의 기운을 스캔하고 사주와 타로카드 데이터를 결합해 초고강도 맞춤 운세 리포트를 제공합니다. 이름, 성별, 생년월일, 태어난 시간까지 알려주시면 당신의 운명을 구체적으로 분석해 오늘의 길흉화복을 한눈에 보여 드릴게요. 자, 이제 당신의 이야기를 들려주세요!"

+ 운세 보기를 좋아하신다.
+ SQL 부분을 잘 모르겠다. 인도 선생님. 다시 공부해야할까.
+ **Ajax 라는 존재가 페이지 새로고침없이 통신되는 것까지는 알겠는 데, 그 이상은 잘 모르겠다.**
    - 왜 사용하는 지. 왜 필요한지에 대해서 궁금증이 있으신?
   - fetch (브라우저 기본 지원), axios 라이브러리
+ 새로운 회원가입을 해도, 똑같은 비밀번호를 사용하면 보안 오류가 뜬다?
    - 해싱 : **input 이 같으면 output이 항상 같음.**
        - 그런데 현재는 output을 보면 input 예측이 가능 => 비밀번호 데이터베이스가 유출되었을 때, 해커가 손쉽게 비밀번호 역계산 가능.
        - 별도의 랜덤 Key 문자열과 조합한 해싱 + 해싱을 여러 번 수행하여 복잡도 올리기 (수만번)
+ [QUESTIONS] **새로고침할 때, 대화 기록이 계속 날라가는 데, 어떻게 더 건드릴 수가 없었다.**
   - 확인 : 대화내역 목록을 프론트 단에서 배열로 관리하기 때문에, 그럴 수 밖에 없습니다. => DB 저장이 필요. 브라우저의 local storage도 해커가 악의적인 목적으로 접근하여 조회/변경 가능.
+ GPT/유튜브에 대한 의존도가 높아서 아쉬웠다.
    - 별코딩, 1분코딩

+ 김성주 강사님 피드백
    - FE/BE/DB 연동의 Flow를 해보신 경험에 대해서 잘 해주셨다.
    - 흥미로운 주제.
    - 비밀번호를 평문으로 저장하는 부분에 대해서 어떻게 풀 수 있을까?
    - 에러처리가 좀 더 티테일했으면.
        - ex) POST 요청 시의 오류 상황에 대한 대처는 어떻게 하면 좋을까?
    - 데이터베이스 연결에 대해서 매번 새로 연결(Connection)을 맺는 부분에 대한 비용은?

+ sqlite3 + raw sql을 통해 대화 로그 및 운세 결과를 저장을 구현하셨음.


## 배근호

+ 마음날씨를 AI가 분석하여, 상황에 가장 적절한 잠언 말씀을 추천하기.
    - 기독교. AI로 성경 말씀을 추천하면 어떨까?
+ JWT 인증
    - 코멘트 : **이후 강의에서 언급할 테지만, JWT는 웹서비스에서는 득보다 실이 많은 인증방법이며, 세션 인증을 추천.**. 앱 서비스에서는 JWT 필요.
        - FastAPI는 세션/인증에 대해서 직접 설정하고 구현해야할 부분이 많음. 세션보다 JWT가 세팅비용이 적어서 간단한 세팅의 JWT를 선호하는 것일 지도.
        - 장고에서는 세션과 인증은 기본 제공되는 기능이기에 세션은 그냥 사용하면 되고, 편의성도 높고, 보안에도 유리.
+ OpenAI API 환경변수 설정
+ fe/index.html 파일을 직접 열거나, Live Server로 여셨음. -> CORS 이슈 ?
    - [DAY-00-웹 API를 위한 인증 중 일부.pdf](./DAY-00-웹%20API를%20위한%20인증%20중%20일부.pdf) 참고
+ API 테스트 : Thunder Client

+ 로그인. 인증된 유저만 채팅 메시지를 보낼 수 있고, 대화 목록 조회 가능

+ 시행착오
    - ChatGPT API를 연동하고 API 테스트 진행과정에서 경로 에러 (429(Rate Limit), 404)를 많이 발생.
    - 기쁨, 슬픔, 무기력함, 분노, 불안의 5가지 감정 분석 => 어떤 오류 ??
        - 감정을 5가지로 고정을 했다보니, 복합적인 감정, 다른 감정에 대해서는 적절한 답변이 없었다. 아마도 Key Error ?
        - 이진석 : 잠언 말씀에 대해, 다양한 감정에 대해서 데이터베이스에서 미리 분류를 해보면 ?
    - UI/UX 디자인 부분 CSS/JS가 막막했다.
    - 없어도 되는 데 있으면 편한 기능에 대해서도 고민을 해봤었다.
    - AI를 통해 구현하다보니, 전체적인 이해도가 아쉬웠다.
    - 이메일 인증, 비밀번호 찾기 등 미구현
    - 환영합니다. 편의성 문구 미구현

### 참고

+ [잠언 웹 문서](https://nocr.net/?act=&error_return_url=&vid=&mid=korkrv&category=&search_target=title_content&search_keyword=%EC%9E%A0%EC%96%B8)
+ [DAY-00-crawl-잠언.py](./DAY-00-crawl-잠언.py)
+ OpenAI API 에서는 [Structured Output[(https://platform.openai.com/docs/guides/structured-outputs?api-mode=chat)을 지원합니다.
    - 신뢰할 수 있는 유형 안전성: 잘못 포맷된 응답을 검증하거나 다시 시도할 필요가 없습니다.
    - 명시적 거부: 안전 기반 모델 거부는 이제 프로그래밍 방식으로 감지 가능합니다.
    - 더 간단한 프롬프트: 일관된 형식을 얻기 위해 강력한 표현의 프롬프트가 필요하지 않습니다.


## 최은빈

+ 사회복지. 상담일지 기반 상담 도우미
    - 사회복지사가 상담내용을 효율적으로 기록할 수 있도록 하고, 그에 기반한 상담 도우미.
+ **GPT 연동**에 큰 목적을 두었다.
    - GPT 연동에서 여러 에러가 떠서 애를 먹었다. => API 상황에서는 Rate Limit 등의 오류나, 네트워크 오류가 발생할 여지가 항상 있습니다.
+ 느낀 점
    - 실제 동작하는 애플리케이션을 한 번 만들어보니 큰 그림을 그릴 수 있었다.
    - 로그아웃 등의 기능을 시간 내에 완성하지 못해서 아쉬움.
    - 일지 완성 부분도 AI에게 요청해보려 했으나, 설계의 어려움이 있어, 채팅을 통해 도움을 받도록 변경했음.
        -  코멘트: DOM에서 커스텀 이벤트 리스너를 두고, 처리하는 방식이 유용.

+ 김성주 강사님 피드백
    - 저장할 때 암호화해서 저장하는 로직이 있어서 잘 하셨다.
    - 로딩 Indicator 구현
    - Modal을 통해 상세정보 표현


## 윤하정

+ 프롬프트
    - 시스템 : "assistant는 감정에 맞는 철학자 명언을 한국어와 영어로 제공하는 지혜로운 철학자다."
    - 유저 : f"오늘 나는 '{data.mood}' 기분이야. 그 기분에 맞는 철학 명언을 **첫 줄은 한국어, 두 번째 줄은 영어로만** 알려줘."

+ 대학원에서 gpt/노션을 활용한 프로젝트를 했었다.
+ gpt가 기분/감정 피드백을 안정적으로 줬다.

+ 기능
    - 명언 생성 : 기본 입력 후 gpt가 한국어/영어 명언 변환
    - 채팅 복원 : 새로고침 오류가 떠서 못했음.

+ 어려웠던 점
    - 로그인 : 교안에 오탈자/괄호 오류가 많아서, 다음 단계로 넘어가는 걸 엄두를 못 냈다.
    - 포트 충돌 문제 인식이 늦어 시간이 많이 걸렸다.
    - **명언을 받고 나서, 저장 요청 시에 화면이 새로고침이 되는 오류을 늦게 발견하게 되었고, 아직 오류를 해결하지 못했다. 새로고침이 되면 앞서 받은 명언이 사라진다. **

+ 느낀 점
    - GPT 활용하면 빠르게 결과를 낼 수는 있는 데, 직접 한 것이 아니라서 실제 오류 해결에 대해서 감을 잡지 못하겠더라.

+ 김성주 강사님 피드백
    - `app` 폴더 만드시고 fe/be 분리 잘 하셨음.
    - 로그인 시스템에서 닉네임으로만 인증하는 부분이 아쉬웠음.
    - FE는 단순하고 명확하게 구현하셨음.
    - 새로고침 문제는 좀 더 디테일하게 파보셨으면.


## 배주완

+ 프롬프트
    - "당신은 친근한 점심 메뉴 추천 전문가입니다. 사용자의 지역, 용도, 취향 등을 고려하여 적합한 점심 메뉴를 추천해주세요."

+ 점심 메뉴 추천
+ 회원가입 : 아이디 중복 검증, 비밀번호 형식 검증 (영문, 특수문자, 8자 이상)
    - endpoint 함수 내에서 하나 하나 유효성 검사
+ 로그인 성공 시 쿠키에 사용자 정보 저장해서 세션 유지

+ tailwind css는 gpt로 구현했음.

+ Q
    - 암호는 평문으로 저장해서, 평문 비교 ?
    - 웹브라우저 단에서의 폼 유효성 검사는 의도한 것인지?
    - 위니브 API 특성 상, Streaming 응답은 불가.

+ 김성주 강사님 피드백
    - tailwind 선택 이유는? 수업에서 잠깐 봤지만, 강력해보여서.
    - 기능적으로 단순화가 많이 되어있다.


## 심희현

+ 프롬프트
    - 시스템 : "당신은 요리 전문가입니다. 요리 레시피, 재료, 조리법, 맛에 대한 질문에만 답변해주세요. 친근하고 자세하게 설명해주세요."

+ 나만의 레시피 상담 서비스
+ 핵심 기능
    - 세션 기반 인증으로 로그인 상태 유지, 비밀번호 sha256 해싱
    - 로그인 권한 검증
    - 비밀번호 4자리 이상
    - 모바일용으로 화면 조절 기능 추가
    - 기록 삭제 기능
    - 자신의 레시피만 수정할 수 있는 기능.

+ 응답이 느리다.
    - 스트리밍 처리가 되어있지 않아서입니다.

+ 아쉬웠던 부분
    - AI를 쓰긴 했지만 이해가 잘 안 되던 부분이 있었고, 이를 구글링 등을 통해 채웠고, 기간만 더 길면 더 완성도를 높일 수 있겠다.

+ 요리/레시피 관련 질문인지 확인하여, 요리/레시피 질문이 아니면 요청 거부
    - `chatgpt_service.py` 에서 요리, 레시피, 음식 등의 키워드가 있는 지 확인

+ Q
    - 회원가입에 대한 유효성 검사는 ? : 아이디 중복 검사 등
        - 채팅 메시지 입력에서는 별도 유효성 검사 함수가 있음.


## 김가영

+ 프롬프트

+ 견종 정보 백과 챗봇
    - 견종 이름을 입력하면, 해당 견종의 정보를 챗봇 형식으로 알려줌
    - 서버에 JSON 으로 견종 별로 크기, 체고, 출신, 체중, 이름 유래, 주의사항이 저장

+ "견종에 대해 알려줘" 포맷이 아니면 요청 거부
    - AI 호출이 없었다.
    - 정규표현식 매칭 : `if not re.match(r"^.+에 대해 알려줘$", req.question):`
    - 답변을 JSON 으로 저장

- Q
    - templates 내에 css/img/js 파일이 있습니다. templates를 활용하지 않는 지?

+ 아쉬웠던 점
    - 채팅 부분에서 시간이 많이 걸려서 아쉬웠다.
    - live server 주소와 fast api 주소의 포트 번호가 달라서, 쿠키 전송이 안 되는 문제가 있었다.
       - 그래서 주소를 맞춰서 쿠키 전송을 해줬다.

+ 김성주 강사님 피드백
    - 견종 검색 기능이 있으면 좀 더 퀄리티


## 김유미

+ 분야별 최신 뉴스를 불러와 요약 제공
+ ChatGPT API 사용이 필요하다.


## 유수진

+ 나이/직업/취미를 처음에 물어서, 가깝거나 꿈꾸는 미래를 카드로 보여주는 챗봇을 만들어주고 싶었다.
    - 1일차 : 상상과 현실이 달라서 괴리를 느꼈다.
    - 2일차/3일차 : 목표를 바꿔, 어떻게든 진행율을 높이고자 함.
    - GPT가 없었으면 불가능했다고 느낄 정도로 GPT 의존도가 높았다.
+ FE/BE 간의 통신이 어떻게 이뤄지는 데에 이해도가 높아질 수 있었다.
+ 인증 등의 자료를 프로젝트 전에 미리 숙지할 수 있었으면, 시행착오를 줄일 수 있지 않았을까 생각.

+ 김성주 강사님 피드백
    - RESTful 설계가 잘 되어있으시고, UI 완성도가 높다.


## 임지은

+ 아주 작은 습관 GPT
   - "아주 작은 습관" 도서가 인상적이어서, 습관 추천
+ alpine.js, tailwind css 사용
    - claude 에서 추천
    - 메뉴를 열고 숨기는 등의 JS에서는 적은 코드로 가능했다.
    - 두 기술 모두 진입장벽이 있었고, 입맛대로 수정이 어려웠고, 사소한 오류에도 어려움이 있었다.
+ 비동기로 API 응답성이 높였다. 방법은?
    - alpine.js로 로딩 UI 표현
+ 최대 20개까지 대화 목록을 보내어, 대화 맥락 전달
+ Claude가 정말 똑똑함을 알게 되었고, AI를 잘 사용하기 위해서는 기술에 대한 기반 이해가 필요함을 느꼈다.

+ 사용자의 말이 API 응답 후에 보여지는 부분이 아쉽다.

+ 김성주 강사님 피드백
    - alpine.js를 통한 상태 관리가 돋보인다.
    - 기존 sha256으로 비밀번호를 해싱하고 있는 데, bcrypt를 통한 해싱을 추천드린다.
