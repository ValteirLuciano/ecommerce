from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth import authenticate, get_user_model


def home_page(request):
    context = {
                    "title": "Página Home",
                    "content": "Bem vindo a página home",
              }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
                    "title": "Página Sobre",
                    "content": "Bem vindo a página sobre"
              }
    return render(request, "about/about.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
                    "title": "Página de Contato",
                    "content": "Bem vindo a página de contato",
                    "form": contact_form
              }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/contact.html", context)
