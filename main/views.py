from .models import Editora, Categoria, Autor
from .forms import Frm_Autor, Frm_Categoria, Frm_Editora
from django.http import HttpResponse

from django.shortcuts import render , redirect , get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

def autorTodos(request) :
    autor_todos = Autor.objects.all()
    return render(request, 'main/autor_todos.html',{'autor_todos': autor_todos})

def autor_create(request):
    if request.method == 'POST':
        form = Frm_Autor(request.POST)
        if form.is_valid():
            autor = form.save(commit=False)            
            autor.save()
            return redirect(reverse('autores'))
    else:
        form = Frm_Autor()
    
    return render(request, 'main/autor_form.html', {'form': form})

def autor_update(request, id):
    autor = get_object_or_404(Autor, pk=id)
    form = Frm_Autor(instance=autor)
    
    if (request.method == 'POST'):

        form = Frm_Autor(request.POST, instance=autor)

        if (form.is_valid()):
            autor.save()
            return redirect('autores')
        else:
            return render(request, 'main/autor_form.html', {'form' : form, 'autor': autor})
    else:
        return render(request, 'main/autor_form.html', {'form': form , 'autor': autor})

def autor_delete(request, id):
    autor = get_object_or_404(Autor, pk=id)
    autor.delete()
    return redirect('autores')