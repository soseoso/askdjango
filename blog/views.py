from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
	qs = Post.objects.all()
	# 아직 이 시점에는 DB 엑세스가 이뤄지지 않았다

	return render(request, 'blog/post_list.html', {
			'post_list': qs,  # 쿼리셋을 인자로 넘겨줌
		})