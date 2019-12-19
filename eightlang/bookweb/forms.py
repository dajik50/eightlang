from django import forms
class GuestForm(forms.Form):
    username = forms.CharField(error_messages={'required': '大名不可以为空哦！'})
    content = forms.CharField(error_messages={'required': '内容不可以为空哦！'})