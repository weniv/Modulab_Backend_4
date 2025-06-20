# 이 파일은 장고 프로젝트 외적인 파일입니다.
# 장고 밖에서 장고의 리소스를 활용해보고
# LLM을 통해서 블로그 포스팅을 생성해보겠습니다.

# 모든 장고를 활용할려는 파이썬 코드는 무조건 DJANGO_SETTINGS_MODULE 환경변수 지정이 필요합니다.
# 현재의 파이썬 코드를 통해 사용할 settings의 경로를 알려줘야만 합니다.
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

# 이제 장고 리소스를 활용할 준비가 끝났습니다.

from pyhub.llm import OpenAILLM, UpstageLLM
from pydantic import BaseModel
from django.conf import settings
from blog.models import Post


class BlogPost(BaseModel):
    title: str
    content: str

llm = OpenAILLM(
    api_key=settings.OPENAI_API_KEY,
    # model="gpt-4o",  # dall-e-3
    system_prompt="""
        너는 여행 블로거야. 유저가 제시하는 내용에 맞춰,
        블로그 포스팅의 제목과 내용을 1000자 이상 작성해줘.
    """,
    max_tokens=8000,  # default: 1000 (최대: ??)
)
reply = llm.ask("대전 성심당 튀김소보로", schema=BlogPost)
print(reply)
blog_post: BlogPost = reply.structured_data
# blog_post.title  # str
# blog_post.content  # str

post = Post()
post.title = blog_post.title
post.content = blog_post.content
post.save()

print("saved post #", post.id)

# print(reply.structured_data.title)
# print(reply.structured_data.content)

# title = reply.text.splitlines()[0]
# content = "\n".join(reply.text.splitlines()[1:])

# Post 임포트 하시고 나서
# Post.objects.create(title=title, content=content)  # 수행하시면, 데이터베이스에 저장이 됩니다.

# print("# title :", title)
# print("----")
# print(content)

# print(reply.text)  # str 타입 : 제목과 내용이 붙어나옵니다.

# qs = Post.objects.all()
# print("posts :", qs)
