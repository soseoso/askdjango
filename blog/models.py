import re
from django.db import models
from django.forms import ValidationError

def lnglat_validator(value):
	if not re.match(r'^([+-]\d+\.?\d*), (\d+\.?\d*)$', value):
		raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
	STATUS_CHOICES = (
			('d', 'Draft'),
			('p', 'Published'),
			('w', 'Withdrawn'),
		)

	author = models.CharField(max_length=20) # migrations 연습
	title = models.CharField(max_length=100, verbose_name='제목',
		help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.')
	content = models.TextField(verbose_name="내용")
	# blank option 활용
	tags = models.CharField(max_length=100, blank=True)
	lnglat = models.CharField(max_length=50, blank=True,
		# 함수를 호출하는 것이 아니라 함수 자체를 넘겼다. 
		validators=[lnglat_validator],
		help_text='경도/위도 포맷으로 입력')
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title