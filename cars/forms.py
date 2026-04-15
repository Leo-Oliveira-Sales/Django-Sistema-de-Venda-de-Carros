from django import forms
from cars.models import Brand, Car


class CarForm(forms.Form):
    model = forms.CharField(max_length=200)  # Campo para o modelo do carro
    brand = forms.ModelChoiceField(Brand.objects.all()) # Campo para selecionar a marca do carro, usando um ModelChoiceField que exibe as opções disponíveis no modelo Brand
    factory_year = forms.IntegerField()  # Campo para o ano de fabricação do carro
    model_year = forms.IntegerField()  # Campo para o ano do modelo do carro
    plate = forms.CharField(max_length=10)  # Campo para a placa do carro
    value = forms.FloatField()  # Campo para o valor do carro
    photo = forms.ImageField()  # Campo para a foto do carro, usando um ImageField que permite o upload de arquivos de imagem




# class CarModelForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields = '__all__'