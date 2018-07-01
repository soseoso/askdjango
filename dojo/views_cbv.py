from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView

class PostListView1(View):
	def get(self, request):
		name = '방법1'
		html = '''
			<h1>AskDjango</h1>
			<p>{name}</p>
		'''.format(names=name)
		return HttpResponse(html)

class PostListView2(TemplateView):
	template_name = 'dojo/post_list2.html'

class PostListView3(object):
	pass

class ExcelDownloadView(object):
	pass