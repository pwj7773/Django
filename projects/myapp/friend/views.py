from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# 현재 폴더의 models.py에서 Friend라는 클래스 import
from .models import Friend
# Create your views here.

def index(request):
    template = loader.get_template('friend/index.html')
    print("실행됨")
    context={}

    return HttpResponse(template.render(context, request))

def add_friend(request):
    print(request.method)
    temaplate = loader.get_template("friend/friendForm.html")
    context={}

    # 요청방식이 GET 방식이라면
    if request.method == "GET" :
        return HttpResponse(temaplate.render(context, request))
    
    # 요청방식이 POST 방식이라면
    else :
        # 요청 객체에서 값을 가져온다.
        name = request.POST['friend_name']
        age = request.POST['friend_age']
        bigo = request.POST['friend_bigo']

        print(name, age, bigo)

        # save() 
        f = Friend(
            friend_name = name,
            friend_age = age,
            friend_bigo = bigo
        )
        f.save()

        # # 템플릿 반환 방식(단축), render(요청, 템플릿경로[, context])
        # return render(request, 'friend/index.html')
        return HttpResponseRedirect('/friend/')

def create_friend(request):
    name = request.POST['friend_name']
    age = request.POST['friend_age']
    bigo = request.POST['friend_bigo']

    Friend.objects.create(
        friend_name = name,
        friend_age = age,
        friend_bigo = bigo
    )

    # 단축방식으로 index.html rendering
    # return render(request, 'friend/index.html')
    return HttpResponseRedirect('/friend/show_all')

def show_all(request) :

    # DB에 저장된 친구 정보 다 가져오기.
    fList = Friend.objects.all()
    
    context={
        'fList':fList
    }

    return render(request, 'friend/friend_list.html', context)


def search(request) :
    search_title = request.GET['search_title']
    condition = request.GET['condition']

    fList = []
    if condition == 'all' :
         fList = Friend.objects.filter(friend_name = search_title)
    else :
        fList = Friend.objects.filter(friend_name__contains = search_title)
    context = {
        'fList' : fList
    }
    return render(request,'friend/friend_list.html',context)
# path converter(주소로 넘어오는 값)의 이름이 id
def delete_friend(request,id):
    print(id)
    
    # Friend 객체들 중에 파라미터로 넘어온 id와 일치하는
    # id를 가진 객체를 삭제한다
    Friend.objects.get(id = id).delete()
    #상위 디렉토리 : ../
    #현재 디렉토리 : ./
    return HttpResponseRedirect('../../show_all/')

def update_friend(request,id) :
    print(id)
    # 파라미터의 id값에 해당하는 객체 찾기
    friend = Friend.objects.get(id=id)
    #전송 방식에 따른 화면 표시
    if request.method == "GET" :
        # id로 찾은 친구 정보를 템플릿에 표시하기 위해서
        context = {'friend' : friend}
        return render(request, 'friend/friend_update.html',context)
    else :
        # id로 찾은 객체에 대해서 폼의 값으로 원래 객체의 값 덮어쓰기
        name = request.POST['friend_name']
        age = request.POST['friend_age']
        bigo = request.POST['friend_bigo']
        friend.friend_name = name
        friend.friend_age = age
        friend.friend_bigo = bigo
        friend.save()
        return HttpResponseRedirect('../../show_all/')

