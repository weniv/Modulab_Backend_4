# baemin/models.py


from django.db import models


# 1 측
class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # photo = models.FileField()  # 모든 파일 포맷 저장 가능
    photo = models.ImageField()  # 이미지만 받아요.


# N 측에 1에 대한 외래키 필드를 추가
class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    content = models.TextField()
    # rating = models.IntegerField()  # 음수/양수 다 담을 수 있어요.
    # rating = models.PositiveIntegerField()   # 양수만 담을 수 있어요. 담을 수 있는 양수의 범위가 2배 커져요.
    rating = models.PositiveSmallIntegerField()  #

    # 1 bit => 0 과 1을 표현 => 값을 2가지 표현 가능
    # 2 bit => 2 ** 2 => 총 4가지 표현 가능
    # 3 bit => 8가지
    # 4 bit => 16, 5 => 32, 6 => 64, 7 => 128, 8 => 256가지 숫자를 표현 가능.
    # 1 byte <= 8비트

    # 일반적인 숫자 변수는 4바이트(32비트)로 숫자를 표현. 물론 8바이트(64비트)로 표현도 해요.
