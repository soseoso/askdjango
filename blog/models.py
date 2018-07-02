from django.db import models

class Post(models.Model):
	# 길이 제한이 있는 문자열
	title = models.CharField(max_length=100,
		choices = (
			# ('실제 저장될 값', 'UI에 보여질 레이블')
			('해의 등불', '제목1 레이블'),
			('제목2', '제목2 레이블'),
			('제목3', '제목3 레이블'),
		),
		verbose_name='제목')
	# 길이 제한이 없는 문자열
	content = models.TextField(verbose_name="내용")
	# auto_now_add=True 옵션 : Post 레코드 하나가 
	# '최초'로 생성/저장될 때의 일시가 저장될 것.
	created_at = models.DateTimeField(auto_now_add=True)
	# auto_now=True 옵션 : 
	# 해당 레코드가 갱신될 때마다의 일시가 저장된다.
	updated_at = models.DateTimeField(auto_now=True)
