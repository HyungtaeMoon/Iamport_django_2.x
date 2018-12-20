from uuid import uuid4

from django.conf import settings
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    amount = models.PositiveIntegerField()
    photo = models.ImageField()
    is_public = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # 32개의 16진수 숫자로 만들어지는 UUID 를 생성하여 주문에 대한 고유한 값을 가짐
    merchant_uid = models.UUIDField(default=uuid4, editable=False)
    # imp_uid 는 iamport 에서 가입하면 발급받는 가맹점 식별코드로 imp+<int>의 값을 가짐
    imp_uid = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, verbose_name='상품명')
    amount = models.PositiveIntegerField(verbose_name='결제금액')
    # 결제 상태를 총 4개의 상태 코드로 설정하고 기본값은 '미결제'로 설정
    status = models.CharField(
        max_length=9,
        choices=(
            ('ready', '미결제'),
            ('paid', '결제완료'),
            ('cancelled', '결제취소'),
            ('failed', '결제실패'),
        ),
        default='ready',
        # status 필드에 index 를 추가하기 때문에 DB 에서 status 필드에
        # 빠르게 접근하여 조회가 가능
        db_index=True
    )
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
