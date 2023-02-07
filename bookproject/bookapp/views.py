from django.shortcuts import get_object_or_404, render, redirect
from .forms import BookModelForm, CommentForm
from .models import Book, Comment
from django.core.paginator import Paginator
import urllib.request
import json
client_id = "SpN27dzgiOqhZj1X48o7"
client_secret = "1_nctZ3vm_"

# Create your views here.
def home(request):
    books = Book.objects.filter().order_by('-date')
    paginator = Paginator(books, 4)
    pagnum = request.GET.get('page')
    books = paginator.get_page(pagnum)
    return render(request, 'index.html', {'books':books})

def mybook(request):
    allbook = Book.objects.filter().order_by('-date')
    books = allbook.filter(writer=request.user)
    return render(request, 'mybook.html', {'books':books})

def search(request):
    if (request.method == 'POST'):
        searchtext = request.POST['searchtext']
        encText = urllib.parse.quote(searchtext)
        url = "	https://openapi.naver.com/v1/search/book.json?query=" + encText
        req = urllib.request.Request(url, None)

        req.add_header("X-Naver-Client-Id",client_id)
        req.add_header("X-Naver-Client-Secret",client_secret)

        response = urllib.request.urlopen(req)

        rescode = response.getcode()

        if(rescode==200): #성공이면
            response_body = response.read()
        else: #실패면
            print("Error Code:" + rescode)
        resdata = response_body.decode('utf-8')

        pydata = json.loads(resdata)
        data = pydata['items']

        with open('book.json', 'w', encoding='UTF-8-sig') as file:
            file.write(json.dumps(data, ensure_ascii=False))
        return render(request, 'search.html', {'data' : data})
    else : 
        return render(request, 'search.html')

def bookform(request):
    if (request.method == 'POST' or request.method == 'FILES'):
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.writer = request.user
            unfinished.save()
            return redirect('home')
    else:
        form = BookModelForm()
    return render(request, 'form.html', {'form':form})

def bookedit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if (request.method == 'POST' or request.method == 'FILES'):
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if (form.is_valid()):
            form.save()
        return redirect('home')

    else:
        form = BookModelForm(instance=book)
        return render(request, 'update.html', {'form' : form, 'book_detail' : book})

def bookdelete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('home')

def detail(request, book_id):
    book_detail = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book_detail':book_detail})

def review(request, book_id):
    book_detail = get_object_or_404(Book, pk=book_id)
    comment_form = CommentForm()
    return render(request, 'review.html', {'book_detail':book_detail, 'comment_form':comment_form})

def create_comment(request, book_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) #아직은 저장하지 말고 대기하라는 뜻
        finished_form.book = get_object_or_404(Book, pk=book_id) #어떤 게시글에 달린 댓글인지 알리기 위해 pk를 통해 블로그 객체 불러와서 post에 넣어준다.
        finished_form.writer = request.user
        finished_form.save()
    return redirect('review', book_id)

def reviewedit(request, review_id):
    comment = get_object_or_404(Comment, pk=review_id)
    book = get_object_or_404(Book, pk=comment.book.id)
    if (request.method == 'POST'):
        form = CommentForm(request.POST, instance=comment)
        if (form.is_valid()):
            form.save()    
        return redirect('review', book.id)
    else:
        form = CommentForm(instance=comment)
        return render(request, 'update_review.html', {'book_detail' : book, 'comment_detail' : comment, 'form' : form})

def reviewdelete(request, review_id):
    comment = get_object_or_404(Comment, pk=review_id)
    book = get_object_or_404(Book, pk=comment.book.id)
    comment.delete()
    return redirect('review', book.id)