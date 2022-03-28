from django.shortcuts import redirect, render
from time import gmtime, strftime

def index(request):
    #declare session
    if 'count' in request.session:
        if request.method=='GET':
            request.session['count']+=2
            return render(request,'index.html')

        else:
            if 'addtwovisits' in request.POST:
                request.session['count']+=2
                return render(request,'index.html')
            elif 'reset' in request.POST:
                request.session['count']=-2
            return redirect('/destroy_session')
    else :
        request.session['count']=-2
        return render(request,'index.html')
def mypost(request):
    return redirect('/')










    
# def index(request):
    
#     if 'count' in request.session:
#         if request.method=='GET':
#             request.session['count']+=1
#             return render(request,'index.html')
            
            
#         else:
#             if 'addtwovisits' in request.POST:
#                 request.session['count']+=1

#             elif 'reset' in request.POST:
#                 request.session['count']=-1
#             return redirect('/post')
            
            

        
#     else:
#         request.session['count']=-1
#         return render(request,'index.html')
# def mypost(request):
#     return redirect('/')
