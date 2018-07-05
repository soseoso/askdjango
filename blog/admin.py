from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at']
	actions = ['make_published']  # 함수를 등록

	def content_size(self, post):
		return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
	content_size.short_description = '글자 수'
	# content_size.allow_tags = True 이것은 사라진 옵션..
	def make_published(self, request, queryset):  # status는 필드
		updated_count = queryset.update(status='p')		# QuerySet.update  
		self.message_user(request, '{} successfully marked as published'.format(updated_count))
		# <- django message framework 활용
	make_published.short_description='Mark selected stories as published'

	