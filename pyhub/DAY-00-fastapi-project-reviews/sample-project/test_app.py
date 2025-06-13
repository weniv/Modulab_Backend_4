#!/usr/bin/env python3
"""
FastAPI 채팅 애플리케이션 기능 테스트
"""

import requests
import time
import random
import string
import sys

# 테스트 서버 URL
BASE_URL = "http://localhost:8003"

# 테스트용 사용자 정보 생성
def generate_test_user():
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return {
        "username": f"testuser_{random_suffix}",
        "email": f"test_{random_suffix}@example.com",
        "password": "testpassword123"
    }

def test_home_page():
    """홈페이지 접속 테스트"""
    print("1. 홈페이지 접속 테스트...")
    try:
        response = requests.get(f"{BASE_URL}/")
        assert response.status_code == 200
        assert "FastAPI 채팅 애플리케이션" in response.text
        print("✅ 홈페이지 접속 성공")
        return True
    except Exception as e:
        print(f"❌ 홈페이지 접속 실패: {e}")
        return False

def test_register():
    """회원가입 테스트"""
    print("\n2. 회원가입 테스트...")
    test_user = generate_test_user()
    
    try:
        # 회원가입 페이지 접속
        response = requests.get(f"{BASE_URL}/register")
        assert response.status_code == 200
        print("✅ 회원가입 페이지 접속 성공")
        
        # 회원가입 처리
        register_data = {
            "username": test_user["username"],
            "email": test_user["email"],
            "password": test_user["password"],
            "password_confirm": test_user["password"]
        }
        
        response = requests.post(
            f"{BASE_URL}/register",
            data=register_data,
            allow_redirects=False
        )
        
        # 회원가입 성공 시 채팅 페이지로 리다이렉트
        assert response.status_code in [303, 302]
        print(f"✅ 회원가입 성공: {test_user['username']}")
        return test_user
        
    except Exception as e:
        print(f"❌ 회원가입 실패: {e}")
        return None

def test_login(test_user):
    """로그인 테스트"""
    print("\n3. 로그인 테스트...")
    
    try:
        # 로그인 페이지 접속
        response = requests.get(f"{BASE_URL}/login")
        assert response.status_code == 200
        print("✅ 로그인 페이지 접속 성공")
        
        # 로그인 처리
        session = requests.Session()
        login_data = {
            "username": test_user["username"],
            "password": test_user["password"]
        }
        
        response = session.post(
            f"{BASE_URL}/login",
            data=login_data,
            allow_redirects=False
        )
        
        # 로그인 성공 시 채팅 페이지로 리다이렉트
        assert response.status_code in [303, 302]
        print(f"✅ 로그인 성공: {test_user['username']}")
        return session
        
    except Exception as e:
        print(f"❌ 로그인 실패: {e}")
        return None

def test_chat(session):
    """채팅 기능 테스트"""
    print("\n4. 채팅 기능 테스트...")
    
    try:
        # 채팅 페이지 접속
        response = session.get(f"{BASE_URL}/chat")
        assert response.status_code == 200
        assert "AI 채팅" in response.text
        print("✅ 채팅 페이지 접속 성공")
        
        # 메시지 전송
        chat_data = {
            "message": "안녕하세요! 테스트 메시지입니다."
        }
        
        response = session.post(
            f"{BASE_URL}/api/chat",
            data=chat_data,
            allow_redirects=False
        )
        
        # 메시지 전송 후 채팅 페이지로 리다이렉트
        assert response.status_code in [303, 302]
        print("✅ 메시지 전송 성공")
        
        # 채팅 히스토리 확인
        response = session.get(f"{BASE_URL}/chat")
        assert response.status_code == 200
        assert "테스트 메시지입니다" in response.text
        print("✅ 채팅 히스토리 확인 성공")
        
        return True
        
    except Exception as e:
        print(f"❌ 채팅 기능 테스트 실패: {e}")
        return False

def test_logout(session):
    """로그아웃 테스트"""
    print("\n5. 로그아웃 테스트...")
    
    try:
        response = session.post(
            f"{BASE_URL}/logout",
            allow_redirects=False
        )
        
        # 로그아웃 후 메인 페이지로 리다이렉트
        assert response.status_code in [303, 302]
        print("✅ 로그아웃 성공")
        
        # 로그아웃 후 채팅 페이지 접근 시도
        response = session.get(f"{BASE_URL}/chat", allow_redirects=False)
        assert response.status_code in [303, 302]  # 로그인 페이지로 리다이렉트
        print("✅ 인증 확인 성공")
        
        return True
        
    except Exception as e:
        print(f"❌ 로그아웃 테스트 실패: {e}")
        return False

def test_api_endpoints():
    """API 엔드포인트 테스트"""
    print("\n6. API 엔드포인트 테스트...")
    
    try:
        # OpenAPI 문서 확인
        response = requests.get(f"{BASE_URL}/docs")
        assert response.status_code == 200
        print("✅ API 문서 접속 성공")
        
        # 인증 없이 /api/me 접근 시도
        response = requests.get(f"{BASE_URL}/api/me")
        assert response.status_code == 401
        print("✅ API 인증 보호 확인")
        
        return True
        
    except Exception as e:
        print(f"❌ API 엔드포인트 테스트 실패: {e}")
        return False

def main():
    """전체 테스트 실행"""
    print("FastAPI 채팅 애플리케이션 테스트 시작\n")
    print(f"테스트 서버: {BASE_URL}")
    print("-" * 50)
    
    # 서버 연결 확인
    try:
        response = requests.get(BASE_URL, timeout=5)
    except requests.exceptions.ConnectionError:
        print("❌ 서버에 연결할 수 없습니다.")
        print(f"서버가 {BASE_URL}에서 실행 중인지 확인하세요.")
        sys.exit(1)
    
    # 테스트 실행
    test_results = []
    
    # 1. 홈페이지 테스트
    test_results.append(("홈페이지 접속", test_home_page()))
    
    # 2. 회원가입 테스트
    test_user = test_register()
    test_results.append(("회원가입", test_user is not None))
    
    if test_user:
        # 3. 로그인 테스트
        session = test_login(test_user)
        test_results.append(("로그인", session is not None))
        
        if session:
            # 4. 채팅 테스트
            test_results.append(("채팅 기능", test_chat(session)))
            
            # 5. 로그아웃 테스트
            test_results.append(("로그아웃", test_logout(session)))
    
    # 6. API 엔드포인트 테스트
    test_results.append(("API 엔드포인트", test_api_endpoints()))
    
    # 결과 요약
    print("\n" + "=" * 50)
    print("테스트 결과 요약")
    print("=" * 50)
    
    passed = sum(1 for _, result in test_results if result)
    total = len(test_results)
    
    for test_name, result in test_results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:<20} {status}")
    
    print("-" * 50)
    print(f"전체: {passed}/{total} 성공 ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("\n🎉 모든 테스트가 성공했습니다!")
    else:
        print(f"\n⚠️  {total - passed}개의 테스트가 실패했습니다.")

if __name__ == "__main__":
    main()