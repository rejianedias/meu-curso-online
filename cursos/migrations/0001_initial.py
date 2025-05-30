# Generated by Django 5.2 on 2025-05-22 18:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=255)),
                ('resposta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alunos_favoritos', models.ManyToManyField(blank=True, related_name='cursos_favoritos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('professor', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='cursos/')),
                ('url_video', models.URLField()),
                ('materiais', models.FileField(blank=True, null=True, upload_to='materiais/')),
                ('alunos_favoritos', models.ManyToManyField(blank=True, related_name='favoritos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='cursos.cursos')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulos', to='cursos.cursos')),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('video_url', models.URLField()),
                ('concluida_por', models.ManyToManyField(blank=True, related_name='aulas_concluidas', to=settings.AUTH_USER_MODEL)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aulas', to='cursos.module')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('correta', models.BooleanField(default=False)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternativas', to='cursos.pergunta')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='cursos.cursos')),
            ],
        ),
        migrations.AddField(
            model_name='pergunta',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perguntas', to='cursos.quiz'),
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=300)),
                ('correta', models.BooleanField(default=False)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='cursos.pergunta')),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontuacao', models.IntegerField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.quiz')),
            ],
        ),
    ]
