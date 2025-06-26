

# 동기 함수
def fetch(url):
    print("fetch 함수 실행")
    return f"Response from {url}"


# 비동기 함수
async def fetch2(url):
    print("fetch2 함수 실행")
    return f"Response from {url}"


# print(fetch("https://www.naver.com"))

import asyncio
print(asyncio.run(fetch2("https://www.naver.com")))
