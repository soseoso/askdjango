from django import forms
from .models import Post


# 원래 validator는 모델에 정의하는 것이다.
# def min_length_3_validator(value):
# 	if len(value) < 3:
# 		raise forms.ValidationError('3글자 이상 입력해주세요.')

class PostModelForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'content']

	# title = forms.CharField(validators=[min_length_3_validator])
	# # 유저로부터 입력받은 title 값이 검증될 떄,
	# # min_length_3_validator 함수의 value 값에 title 값이 전달된다.
	# content = forms.CharField(widget = forms.Textarea)

	# def save(self, commit=True):
	# 	post = Post(**self.cleaned_data)  # <-- self.instance == post
	# 	if commit:
	# 		post.save()
	# 	return post