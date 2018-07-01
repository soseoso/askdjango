from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView

class PostListView1(View):
	# 그냥 View 클래스 사용.
	def get(self, request):
		name = '방법1'
		html = get_template_string().format(name=name)
		return HttpResponse(html)

	def get_template_string(self):
		return '''
			<h1>AskDjango</h1>
			<p>{name}</p>
		'''
	# 이런 식의 코딩은 함수 기반 뷰에서는 불가능한 것!
post_list1 = PostListView1.as_view()

class PostListView2(TemplateView):
	template_name = 'dojo/post_list.html'

post_list2 = PostListView2.as_view()

class PostListView3(object):
	pass

class ExcelDownloadView(object):
	pass