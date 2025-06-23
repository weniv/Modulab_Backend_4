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
from django.core.files.base import File
from baemin.models import Shop


class BaeminShop(BaseModel):
    name: str
    description: str


class ResponseSchema(BaseModel):
    shop_list: list[BaeminShop]


def make_topics() -> list[BaeminShop]:
    prompt = (
        "배달 서비스 가게 등록을 위해 가게 정보를 3개 생성. 각 가게 정보의 name에는 "
        "반드시 가게의 unique한 이름이 있어야함. '분식 전문점'과 같은 이름은 안 됨."
    )

    llm = OpenAILLM()
    reply = llm.ask(prompt, schema=ResponseSchema)
    return reply.structured_data.shop_list


def make_photo_file(shop: BaeminShop) -> File:
    llm = OpenAILLM(model="dall-e-3")
    image_reply = llm.generate_image(f"""
        아래 키워드의 식당 대표 이미지 생성
        - title: {shop.name}
        - description: {shop.description}
    """)
    return image_reply.to_django_file()


for baemin_shop in make_topics():
    print(baemin_shop)
    photo_file = make_photo_file(baemin_shop)

    shop = Shop()
    shop.name = baemin_shop.name
    shop.description = baemin_shop.description
    shop.photo = photo_file
    shop.save()

    print("saved", shop)

    # break
