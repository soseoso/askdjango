# from django.http import HttpResponse, JsonResponse
# from django.views.generic import View, TemplateView
# # CBV로 구현할 때, 실제로 View를 상속받아서 쓰는 경우는 거의 없다.
# from django.conf import settings
# import os

# class PostListView1(View):
# 	def get(self, request):
# 		name = '방법1'
# 		html = self.get_template_string().format(name=name)
# 		return HttpResponse(html)  # HttpResponse

# 	# 클래스이기에 다양한 멤버 함수를 줄 수 있다.
# 	# 이런 것은 함수 기반 뷰에서는 불가능하다.
# 	# 좀 더 구조적인 개발이 가능해진다.
# 	def get_template_string(self):
# 		return '''
# 			<h1>AskDjango</h1>
# 			<p>{name}</p>
# 		'''

# # 클래스를 통해서 FBV 생성해준다.
# post_list1 = PostListView1.as_view()  


# # TemplateView
# class PostListView2(TemplateView):
# 	template_name = 'dojo/post_list2.html'

# 	#
# 	def get_context_data(self):
# 		# super()는 파이썬 3에서만 지원해주는 문법이다.
# 		# python2 : super(PostListView2, self).get_context_data()
# 		context = super().get_context_data()
# 		context['name'] = '방법2'
# 		return context

# post_list2 = PostListView2.as_view()

# # Json 형식 응답하기 
# class PostListView3(View):
# 	def get(self, request):
# 		# JsonResponse
# 		return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})

# 	def get_data(self):
# 		return {
# 			'message': '안녕, 파이썬 & 장고',
# 			'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
# 		}

# post_list3 = PostListView3.as_view()

# class ExcelDownloadView(View):
# 	def get(self, request):
# 		filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')
# 		filename = os.path.basename('filepath')
# 		with open(filepath, 'rb') as f:  # 파일 오브첵트 f 생성
# 			reponse = HttpResponse(f, content_type='application/vnd.ms-excel')
# 		# content_type 디폴트 설정은 'text/html'
# 			reponse['Content-Disposition'] = 'attachment'; filename="{}".format(filename)
# 			return reponse

# excel_download = ExcelDownloadView.as_view()