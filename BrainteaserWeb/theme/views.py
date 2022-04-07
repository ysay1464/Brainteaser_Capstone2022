from django.shortcuts import render, redirect
from .models import Board,BoardContents

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list(request):
    # IT 게시판
    boards = Board.objects.filter(Category='Category1')
    # 다른 게시판2
    # boards = Board.objects.filter(Category='Category2')
    # 다른 게시판3
    # boards = Board.objects.filter(Category='Category3')
    return render(request, 'list.html',{"boards":boards})

def write(request):
    return render(request, 'write.html')

def view(request):
    # TeaserID가 자동적으로 수정되면서 다수의 URL을 사용할 수 있도록 해야함.
    boardContents = BoardContents.objects.filter(TeaserID = 1)
    return render(request, 'view.html', {"boardContents":boardContents})

def logout(request):
    print(request.session.get('username'), "로그아웃")
    request.session.flush()
    return redirect('/')

