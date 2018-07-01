from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from .forms import PostModelForm
from .models import Post


# Create your views here.

def mysum(request, x, y=0):	# 하나의 인자만 받는다, x.
	# request : HttpResponse의 인스턴스
	return HttpResponse(int(x) + int(y))	# 그냥 전달받은 x 값을 보여준다.

def hello(request, name, age):
	return HttpResponse('안녕하세요, {}. {}살이시네요'.format(name, age))

def post_list1(request):
	name = '방법1'
	return HttpResponse('''
		<h1>AskDjango</h1>
		<p>{name}</p>
		'''.format(name=name)
		# 주의사항 : 여기서는 name에 접근할 때,
		# 중괄호가 이렇게 {{ }} 두 개가 아니라 한 쌍 { } 이다.
	)

def post_list2(request):
	name = '방법2'
	return render(request, 'dojo/post_list2.html', {'name': name})

def post_list3(request):
	return JsonResponse({
		'message': '방법3',
		'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS']
		}, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
	# filepath = 'C:/Users/now/PycharmProjects/askdjango/gdplev.xls'
	# 아래가 좀 더 나은 코딩
	filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')
	filename = os.path.basename('filepath')
	with open(filepath, 'rb') as f:  # 파일 오브첵트 f 생성
		reponse = HttpResponse(f, content_type='application/vnd.ms-excel')
		# content_type 디폴트 설정은 'text/html'
		reponse['Content-Disposition'] = 'attachment'; filename="{}".format(filename)
		return reponse



def post_new(request):
	if request.method == "POST":
		form = PostModelForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False) # 아래의 post.save()와 중복이니까 commit = False
			post.ip = request.META['REMOTE_ADDR']
			post.save() 
			# post = Post()
			# post.title = form.cleaned_data['title']
			# post.content = form.cleaned_data['content']
			#  post = Post.objects.create(**form.cleaned_data)
			# post.save()
			# print(form.cleaned_data)  # 사전 형태
			return redirect('/dojo/')
	else:
		form = PostModelForm()
	return render(request, 'dojo/post_form.html', {
		'form': form,
	})

def post_edit(request, id):
	post = get_object_or_404(Post, id=id)
	if request.method == "POST":
		form = PostModelForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.save() 
			return redirect('/dojo/')
	else:
		form = PostModelForm(instance=post)
	return render(request, 'dojo/post_form.html', {
		'form': form,
	})