from django.shortcuts import render, get_object_or_404, redirect
from .models import Cursos, Comentario, Aula
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Quiz, Pergunta, Resposta, ResultadoQuiz
from .models import FAQ
from .forms import DúvidaForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import ComentarioForm  



def catalogo(request):
    busca = request.GET.get('q', '')
    cursos = Cursos.objects.all()
    if busca:
        cursos = cursos.filter(Q(titulo__icontains=busca) | Q(descricao__icontains=busca))
    return render(request, 'curso/catalogo.html', {'cursos': cursos, 'busca': busca})

def detalhes_curso(request, curso_id):
    curso = get_object_or_404(Cursos, id=curso_id)
    comentarios = curso.comentarios.all()
    return render(request, 'curso/detalhes.html', {
        'curso': curso,
        'comentarios': comentarios,
    })

@login_required
def concluir_aula(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    aula.concluida_por.add(request.user)
    return redirect('detalhes_curso', curso_id=aula.modulo.curso.id)

@login_required
def favoritar_curso(request, curso_id):
    curso = get_object_or_404(Cursos, id=curso_id)
    if request.user in curso.alunos_favoritos.all():
        curso.alunos_favoritos.remove(request.user)
    else:
        curso.alunos_favoritos.add(request.user)
    return redirect('detalhes_curso', curso_id=curso_id)

#parte do quiz



@login_required
def fazer_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    perguntas = quiz.perguntas.all()

    if request.method == 'POST':
        pontuacao = 0
        for pergunta in perguntas:
            resposta_id = request.POST.get(str(pergunta.id))
            if resposta_id:
                resposta = Resposta.objects.get(id=int(resposta_id))
                if resposta.correta:
                    pontuacao += 1
        ResultadoQuiz.objects.create(aluno=request.user, quiz=quiz, pontuacao=pontuacao)
        return render(request, 'curso/resultado_quiz.html', {
            'pontuacao': pontuacao,
            'total': perguntas.count(),
        })

    return render(request, 'curso/quiz.html', {
        'quiz': quiz,
        'perguntas': perguntas,
    })

# perfil do aluno


@login_required
def perfil_aluno(request):
    favoritos = request.user.cursos_favoritos.all()
    concluidas = request.user.aulas_concluidas.all()
    return render(request, 'curso/perfil.html', {
        'favoritos': favoritos,
        'aulas_concluidas': concluidas,
    })

# views para suporte

def suporte(request):
    faqs = FAQ.objects.all()
    enviado = False

    if request.method == 'POST':
        form = DúvidaForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            send_mail(
                f"[DÚVIDA] {assunto}",
                mensagem,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],  # ou email de suporte
            )
            enviado = True
    else:
        form = DúvidaForm()

    return render(request, 'curso/suporte.html', {
        'faqs': faqs,
        'form': form,
        'enviado': enviado,
    })

# View da Aula com Comentários

@login_required
def detalhes_aula(request, aula_id):
    aula = get_object_or_404(Aula, id=aula_id)
    comentarios = aula.comentarios.order_by('-criado_em')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.aula = aula
            comentario.save()
            return redirect('detalhes_aula', aula_id=aula.id)
    else:
        form = ComentarioForm()

    return render(request, 'curso/aula.html', {
        'aula': aula,
        'comentarios': comentarios,
        'form': form,
    })

