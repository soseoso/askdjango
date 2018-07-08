from django import forms
from django.db import models

def min_length_3_validator(value):
 	if len(value) < 3:
 		raise forms.ValidationError('3글자 이상 입력해주세요.')

# Create your models here.
# class Post(models.Model):
# 	title = models.CharField(max_length=100, validators = [min_length_3_validator])
# 	# 이렇게 모델에 다 해놓으면, 모델 폼을 생성할 때, 모든 내역을 다 가져온다.
# 	content = models.TextField()
# 	ip = models.CharField(max_length=15)
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	updated_at = models.DateTimeField(auto_now = True)