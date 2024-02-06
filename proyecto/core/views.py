from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from modelo import models

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "mi 2 super web 2"})


class SamplePageView(TemplateView):
    template_name = "core/sample.html"


class ScannerPageView(LoginRequiredMixin, TemplateView):
    template_name = "core/scanner.html"
    login_url = reverse_lazy('admin:login')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def view_detalles_alumno(request):
    if request.method == 'POST':
        result_qr = request.POST.get('datoqr')
        try:
            alumnoBD = models.Alumno.objects.get(id=result_qr)
            return JsonResponse({'id_alumno': alumnoBD.id})
        except models.Alumno.DoesNotExist:
            return JsonResponse({'id_alumno': 0})
    return JsonResponse({'error': 'Solicitud no válida'})


def detalles_alumno(request):
    id_alumno = request.GET.get('id')
    if id_alumno is not None:
        try:
            alumno = models.Alumno.objects.get(id=id_alumno)
            return render(request, "core/detalles_busqueda.html", {"alumno": alumno})
        except models.Alumno.DoesNotExist:
            error_message = f"No existe ningún registro para el ID de alumno: {id}"
            return render(request, "error.html", {"error_message": error_message})
    else:
        return JsonResponse("No se proporcionó el parámetro 'id' en la URL.")
