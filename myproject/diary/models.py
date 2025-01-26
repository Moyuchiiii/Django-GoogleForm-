from django.db import models
from django.contrib.auth.models import User
import uuid


class Page(models.Model):
    answertf = models.BooleanField(default=False, verbose_name="回答")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    title = models.CharField(max_length=100, verbose_name="タイトル")
    q1 = models.CharField(max_length=100, verbose_name="質問1", default="")
    q2 = models.CharField(max_length=100, verbose_name="質問2", default="", blank=True)
    q3 = models.CharField(max_length=100, verbose_name="質問3", default="", blank=True)
    q4 = models.CharField(max_length=100, verbose_name="質問4", default="", blank=True)
    q5 = models.CharField(max_length=100, verbose_name="質問5", default="", blank=True)
    q6 = models.CharField(max_length=100, verbose_name="質問6", default="", blank=True)
    q7 = models.CharField(max_length=100, verbose_name="質問7", default="", blank=True)
    q8 = models.CharField(max_length=100, verbose_name="質問8", default="", blank=True)
    q9 = models.CharField(max_length=100, verbose_name="質問9", default="", blank=True)
    q10 = models.CharField(max_length=100, verbose_name="質問10", default="", blank=True)
    a1 = models.TextField(max_length=2000, verbose_name="回答1", default="")
    a2 = models.TextField(max_length=2000, verbose_name="回答2", default="")
    a3 = models.TextField(max_length=2000, verbose_name="回答3", default="")
    a4 = models.TextField(max_length=2000, verbose_name="回答4", default="")
    a5 = models.TextField(max_length=2000, verbose_name="回答5", default="")
    a6 = models.TextField(max_length=2000, verbose_name="回答6", default="")
    a7 = models.TextField(max_length=2000, verbose_name="回答7", default="")
    a8 = models.TextField(max_length=2000, verbose_name="回答8", default="")
    a9 = models.TextField(max_length=2000, verbose_name="回答9", default="")
    a10 = models.TextField(max_length=2000, verbose_name="回答10", default="")
    page_date = models.DateTimeField(auto_now_add=True, verbose_name="日付")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作成者", default=1)

    def __str__(self):
        return self.title