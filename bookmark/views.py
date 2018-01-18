from django.shortcuts import render
from django.http import HttpResponse
from bookmark.models import Question
import requests
from bs4 import BeautifulSoup
from bookmark.models import Product
from django.contrib.auth.models import User

import datetime

def index(request):
    try:
        email = request.session["email"]
    except KeyError:
        email = None

    return render(request, 'index.html', {"email": email})

def Inquiry(request):
    try:
        email = request.session['email']
    except KeyError as e:
        return render(request, 'login_form.html')

    all_bookmark = None
    if request.method == 'POST':
        Inquiry = Question(
            question=request.POST["bookmark_name"], User_url=request.POST["bookmark_url"]
        )
        Inquiry.save()
        result = {"email": email,
                  "bookmark_name": request.POST["bookmark_name"],
                  "bookmark_url": request.POST["bookmark_url"]}

        return render(request, 'bookmark.html', result)
    else:
        all_bookmark = Question.objects.all()
        result = {"email": email,
                  "all_bookmark": all_bookmark}
        return render(request, 'bookmark.html', result)

def login(request):
    try:
        email = request.session["email"]
    except KeyError:
        email = None
    return render(request, 'login_form.html', {"email": email})

def login_check(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=email)
            if user.check_password(password):
                request.session['email'] = email
                return render(request, 'index.html', {"email": email})
            else:
                status = "비밀번호가 틀렸습니다"
                return render(request, 'login_form.html', {"status": status})
        except User.DoesNotExist:
            status = "존재하지 않는 아이디입니다."
            return render(request, 'login_form.html', {"status": status})


def logout(request):
    try:
        email = request.session['email']
    except KeyError as e:
        return render(request, 'login_form.html')
    return render(request, 'logout_form.html', {"email": email})

def logout_process(request):
    del request.session['email']
    return render(request, 'index.html')

def user_registration(request):
    if request.method == 'POST':
        email = request.POST["email"]

        try:
            User.objects.get(username=email)
            status = "이미 존재하는 아이디입니다"
            return render(request, 'login_form.html', {"status": status})
        except User.DoesNotExist:
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            password = request.POST["passwd"]

            new_user = User.objects.create_user(email, email, password)
            new_user.last_name = lastname
            new_user.first_name = firstname
            new_user.save()
            request.session['login_id'] = email
            return render(request, 'index.html', {"login_id": email})

def product(request):

        search = request.POST.get("search")
        url = 'https://search.shopping.naver.com/search/all.nhn?origQuery=' + str(search) + '&pagingIndex=1&pagingSize=40&viewType=list&sort=price_asc&frm=NVSCTAB&query=' + str(search)
        page = requests.get(url)
        html = page.text
        soup = BeautifulSoup(html, "html.parser")
        try:
            name2 = list()  # 1번 data

            for i in soup.findAll(attrs={'class': 'info'}):
              title = i.next_element.next_element.get('title')
              name2.append(title)

            name = list()
            for i in range(0, 5):
                name.append(name2[i])


            price3 = soup.find_all(attrs={'class': 'num _price_reload'})
            price = list()
            for i in range(0, 5):
                price.append(price3[i].text)

            image2 = list()  # 2번 data
            for i in soup.findAll(attrs={'class': '_productLazyImg'}):
                link = i.attrs['data-original']
                image2.append(link)

            image = list()
            for i in range(0, 5):
                image.append(image2[i])

            place = list()
            for i in soup.findAll(attrs={'class': 'mall_img'}):
                if i.text == str(""):
                    place2 = i.next_element.get('alt')
                    place.append(place2)
                else:
                    place3 = str(i.text)
                    place.append(place3)

            product_list = soup.find_all('li', {'class': '_itemSection'})
            product_list2 = product_list[0:5]

            link = list()
            for i in product_list2:
                link.append(i.find('div', {'class': 'info'}).find('a').attrs['href'])

            result = [{'name' : name[i], 'price' : price[i], 'image' : image[i], 'place' : place[i], 'link' : link[i]} for i in range(5)]

            for i in range(5):
                productlog = Product.objects.create(search=request.POST["search"],
                                           product_name=name[i], product_place=place[i],
                                           product_price=price[i])

                productlog.save()

        except:
            result = 'Error'

        return render(request, 'product.html', {'result' : result})




