from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms



class Empregado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + " - " + self.titulo


class Projecto(models.Model):
    autor = models.ForeignKey(Empregado,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500)
    votos = models.IntegerField(default=0)
    texto = models.TextField(max_length=2000,default="")
    data = models.DateTimeField(default=timezone.now)
    imagem = models.TextField(max_length=300,default="")

    def publicaProj(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo



class Comentario(models.Model):
    proj = models.ForeignKey(Projecto, on_delete=models.CASCADE)
    autor = models.CharField(max_length=200)
    texto = models.TextField(max_length=2000,default="")
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.autor

class BlogPost(models.Model):
    titulo = models.CharField(max_length=500, default="")
    subtitulo = models.CharField(max_length=500, default="")
    autor = models.ForeignKey(Empregado, on_delete=models.CASCADE)
    texto = models.TextField(max_length=10000,default="")
    data = models.DateTimeField(default=timezone.now)
    imagem = models.TextField(max_length=300,default="")

    def __str__(self):
        return self.titulo

class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control' })
            self.fields[field].widget.attrs['required'] = 'required'



class EmpregadoForm(ModelForm):
    class Meta:
        model = Empregado
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmpregadoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control' })
            self.fields[field].widget.attrs['required'] = 'required'


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['last_name', 'groups', 'user_permissions','is_staff','is_active','last_login']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field not in ['is_superuser', 'email']:
                print(field)
                self.fields[field].widget.attrs.update({'class': 'form-control' })
                self.fields[field].widget.attrs['required'] = 'required'

            self.fields['email'].widget.attrs.update({'class': 'form-control' })



class ProjectoForm(ModelForm):
    class Meta:
        model = Projecto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProjectoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control' })
            self.fields[field].widget.attrs['required'] = 'required'


