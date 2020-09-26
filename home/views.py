from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from home.models import Contact
# from home.models import AddPost
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import UserDetail
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.db.models import Q
# from .forms import UserUpdate, ProfileUpdate
from django.contrib.auth.decorators import login_required
# from .forms import  UserUpdate, ProfileUpdate


def home(request):
    allPosts = Post.objects.all().order_by('-views')[:3]
    context = {'allPosts':allPosts}
    return render(request,'home/home.html',context)
    # return render(request,"home/home.html")

def about(request):
    # return HttpResponse('About Page')
    return render(request, 'home/about.html')

def contact(request):
    # return HttpResponse('this is contact page')
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "your message has been send successfully") 
    return render(request,'home/contact.html')

def search(request):
    # allPosts = Post.objects.all()
    search = request.GET['search']  #search is name 
    # allPosts = Post.objects.filter(content__icontains = search)
    # allPosts = Post.objects.filter(title__icontains = search)
    allPosts = Post.objects.filter(Q(title__icontains = search) |
                                    Q(content__icontains = search) |
                                    Q(category__icontains = search) |
                                    Q(author__icontains = search)
                                    ).order_by('-sno')
    # if len(search)<1:
    #     messages.warning(request, 'Please enter any blog related words')
    params = {'allPosts': allPosts, 'search' : search}
    if len(search)<1: # if we dont put any word it gives error page so(search)<1
        # messages.warning(request, 'Please enter any blog related words')
        return render(request, 'home/search.html')
        # messages.warning(request, 'Please enter any blog related words')
    
    # if len(search)<1:
    #     messages.warning(request, 'Please enter any blog related words')
    #     return render(request, 'home/search.html')
    # elif allPosts.count() == 0:
    #     messages.warning(request, 'Please search  blog related words')
    #     return render(request, 'home/search.html')
    # params = {'allPosts': allPosts, 'search' : search} 
    return render(request, 'home/search.html', params)

def handleSignup(request):
    if request.method == 'POST':
        fname = request.POST['fname'] # ['fname'] = in html name = fname  & from django.contrib.auth.models import User
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        image = request.FILES.get('image')
        
        # check for error type input
        if len(username) > 20:
            messages.error(request, "Username must be less than 10 charecters or unique")
            return redirect('home')

        # if not username.isalnum():
        #     messages.error(request,"usernam must only charecter and numbers only")
        #     return redirect('home')

        if len(password1) < 8:
            messages.error(request, "Password must be  8 or more charecters")
            return redirect('home')

        if password1 != password2:
            messages.error(request,"Password not matched")
            return redirect('home')

        # fix password length | must be special char | must me a capital and small letter | minumum 8 char


        myuser = User.objects.create_user(username, email, password1)
        
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        if(image == None):
            myuserdetail = UserDetail(user=User.objects.filter(username=username).first(), mobile=mobile)
        else:
            myuserdetail = UserDetail(user=User.objects.filter(username=username).first(), mobile=mobile, image=image)
            
        myuserdetail.save()

        messages.success(request, "Your account has been created successfully")
        return redirect('home')

        
    else:
        return HttpResponse('404 - Not Foud')


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        # use authenticate model from jango(from django.contrib.auth.models import authenticate, login, logout)
        # create forget passowrd
        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request," You are successfully logged In")
            return redirect('home')
        else:
            messages.error(request,"Please enter valid information")
            return redirect('home')

    return HttpResponse("404- Not Found")
def handleLogout(request):
    # if request.method == 'POST':
    logout(request)
    messages.success(request,"you are successfully loggedout")
    return redirect('home')


@login_required(login_url='/')
def updateProfile(request):
    context = {}
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        # password1 = request.POST['password1']
        # password2 = request.POST['password2']
        # image = request.FILES.get('image')
        myuser = User.objects.get(username=username)
        userDetail = UserDetail.objects.get(user=myuser)

        myuser.first_name = fname
        myuser.last_name = lname
        myuser.email = email
        # usr.password1 = password1
        myuser.save()

        userDetail.mobile = mobile
        
        if 'image' in request.FILES:
            image = request.FILES['image']
            userDetail.image = image
        userDetail.save()
        context['status'] = "Changes save successfull"

    return render(request,'home/updateProfile.html',context)











# def addPost(request):
#     # return HttpResponse('this is contact page') remove all
#     if request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         author = request.POST['author']
#         # slug = request.POST['slug']
#         # addPost = Post(title='title', content=content, author='author', slug='slug' )
#         addPost = AddPost(title=title, content=content, author=author)
#         addPost.save()
#         messages.success(request, "your post has been send successfully") 
#     return render(request,'home/addPost.html')






