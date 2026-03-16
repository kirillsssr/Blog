from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

from articles.models import Article


def archive(request):
    return render(request, 'archive.html', {'posts': Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, "article.html", {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {
            'text': request.POST["text"],
            'title': request.POST["title"]
        }
        # Проверка названия на уникальность
        if Article.objects.filter(title=form['title']).exists():
            form['errors'] = "Название поста не уникально"
            return render(request, 'create_post.html', {'form': form})
        # в словаре form будет храниться информация, введенная пользователем
        if form["text"] and form["title"]:
            # если поля заполнены без ошибок
            article = Article.objects.create(text=form["text"],
                                             title=form["title"],
                                             author=request.user)
            return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
        else:
            # если введенные данные некорректны
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'create_post.html', {})


def registration(request):
    if request.method == "POST":
        form = {
            "username": request.POST["username"],
            "password1": request.POST["password1"],
            "password2": request.POST["password2"],
        }

        # Проверка на пустые поля
        if not form["username"] or not form["password1"] or not form["password2"]:
            form["errors"] = "Все поля должны быть заполнены"
            return render(request, "registration.html", {"form": form})

        # Проверка совпадения паролей
        if form["password1"] != form["password2"]:
            form["errors"] = "Пароли не совпадают"
            return render(request, "registration.html", {"form": form})

        # Проверка уникальности username
        if User.objects.filter(username=form["username"]).exists():
            form["errors"] = "Пользователь с таким именем уже существует"
            return render(request, "registration.html", {"form": form})

        # Создание пользователя
        User.objects.create_user(
            username=form["username"],
            password=form["password1"]
        )

        # После регистрации сразу на главную
        return redirect("archive")

    return render(request, "registration.html")


def login(request):
    if request.method == "POST":
        form = {
            "username": request.POST["username"],
            "password": request.POST["password"]
        }

        # проверка на пустые поля
        if not form["username"] or not form["password"]:
            form["error"] = "Заполните все поля"
            return render(request, "login.html", {"form": form})

        # аутентификация
        user = authenticate(
            request,
            username=form["username"],
            password=form["password"]
        )

        # если пользователь найден
        if user is not None:
            login_user(request, user)
            return redirect("archive")

        # если неверный логин/пароль
        else:
            form["error"] = "Нет аккаунта с таким логином или паролем"
            return render(request, "login.html", {"form": form})

    return render(request, "login.html", {})
