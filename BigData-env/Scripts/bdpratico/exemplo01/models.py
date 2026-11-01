from django.db import models

class pessoa(models.Model):
 nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
 email = models.CharField(max_length=50, null=False, blank=False, verbose_name='eMail')
 celular = models.CharField(max_length=20, null=True, blank=True, verbose_name='celular')
 funcao = models.CharField(max_length=30, null=True, blank=True, verbose_name='Funcao')
 def __str__(self):
  return self.nome
 class Meta:
  ordering = ['nome']# Create your models here.
