from django.shortcuts import render, redirect
from .forms import PersonaForm

def registrar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirige a la página de éxito
    else:
        form = PersonaForm()
    return render(request, 'registro/registro_form.html', {'form': form})

def success(request):
    return render(request, 'registro/success.html')  # Renderiza la página de éxito
