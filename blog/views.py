from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment, Category
from django.contrib import messages
from blog.templatetags  import extras
from django.contrib.auth.decorators import login_required
# from blog.models import Post
import math
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blogHome(request):
    no_of_posts = 4
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    # return HttpResponse("This is blog home with all blogs")
    allPosts = Post.objects.all().order_by("-sno")
    length = len(allPosts) 
    allPosts =allPosts[(page - 1) * no_of_posts: page * no_of_posts]  #[0:4] no. of post==len=4 in one page
    if page>1:
        prev = page - 1
    else:
        prev = None
    if page < math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    context = {'allPosts' : allPosts, 'prev':prev, 'nxt':nxt}   # context is a dictionary which has {key:values}
    return render(request, 'blog/blogHome.html', context)



# send post in db-POST==========
@login_required(login_url='/')
def userPost(request):
        # return HttpResponse('this is contact page') remove all
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        slug = request.POST['slug']
        # categoryName = request.POST.get('category')
        category = request.POST.get('category')
        slug = request.POST['slug']
        user = request.user

        # category = Category.objects.get(name=categoryName)
        # if(categoryName == None):
        #     id = Category(name=categoryName)
        #     category = Category.objects.get(id=id)

        userPost = Post(title=title, content=content, author=author, slug=slug, category=category, user=user)
       
        userPost.save()
        messages.success(request, "your post has been send successfully") 

        #  category = Category.objects.get(name=name)

    
    choices = Category.objects.all()
    return render(request,'blog/userPost.html', {'choices':choices})


# @login_required(login_url='/')
# def categoryName(request):
#     choices = Category.objects.all()
#     # choices = Category.objects.all().value_list('name','name')
#     # choices_list = []
#     # for item in choices:
#     #     choices_list.append(item)
#     # return render(request,'blog/userPost.html',{'choices_list':choices_list})
#     return render(request,'blog/userPost.html',{'choices':choices})


#render post From db-POST=======
def blogPost(request, slug):
    # return HttpResponse(f'sandals blogPost: {slug}')
    post = Post.objects.filter(slug = slug).first()  # for post-views
    cookie = request.COOKIES.get(slug)
    if(cookie != '1'):
        post.views = post.views + 1
    # request.session['post.views_%s' % post.sno] = True
        post.save()
    # request.session[session_key] = True

    comments = BlogComment.objects.filter(post = post, parent=None) #it gives comment regarding that post so post=post/
    replies = BlogComment.objects.filter(post = post).exclude(parent=None) #it gives reply/exclude(parent=None)==means when it no reply
    
    replyDict = {}  #when it not
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context = {'post': post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}    # user = user == if user-login-then comment sections shows
    response = render(request, 'blog/blogPost.html', context)
    response.set_cookie(slug, '1')
    return response

def postComment(request):
    # return redirect("/blog/{post.slug}")
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":  
            comment = BlogComment(comment=comment, user=user, post=post) 
            comment.save()
            messages.success(request,"your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno = parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)

            comment.save()
            messages.success(request,"your reply has been posted successfully")


    return redirect(f"/blog/{post.slug}")
    # return redirect("/blog/{post.slug}") there must be 'f'




