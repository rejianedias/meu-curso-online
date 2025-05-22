from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo_cursos'),
    path('curso/<int:curso_id>/', views.detalhes_curso, name='detalhes_curso'),
    path('aula/concluir/<int:aula_id>/', views.concluir_aula, name='concluir_aula'),
    path('favoritar/<int:curso_id>/', views.favoritar_curso, name='favoritar_curso'),
    path('quiz/<int:quiz_id>/', views.fazer_quiz, name='fazer_quiz'),
    path('perfil/', views.perfil_aluno, name='perfil_aluno'),
    path('suporte/', views.suporte, name='suporte'),


]
