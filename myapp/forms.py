from django import forms

class EmpForm(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))

    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))

    salary=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))

    location=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))

    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))

    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-warning"}))