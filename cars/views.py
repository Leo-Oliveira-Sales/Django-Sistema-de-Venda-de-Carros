from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm


def cars_view(request):
    cars = Car.objects.all().order_by("model")  # Ordena os carros por data de criação, do mais recente para o mais antigo
    search = request.GET.get("search")  # Obtém o valor do parâmetro de busca da URL

    if search:
        cars = cars.filter(model__icontains=search)  # Filtra os carros pelo modelo, usando uma busca case-insensitive

    return render(request, "cars.html", {"cars": cars}) # Renderiza o template "cars.html" e passa a lista de carros filtrada como contexto para o template


def new_cars_view(request):
    if request.method == "POST":
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():  # Verifica se o formulário é válido
            new_car_form.save()  # Salva o novo carro no banco de dados
            return redirect("cars_list")  # Redireciona para a lista de carros após salvar o novo carro
    else:
        new_car_form = CarForm()  
    return render(request, "new_car.html", {"new_car_form": new_car_form}) 