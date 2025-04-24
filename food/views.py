from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
def home(request):
    return render(request, "home.html")

def login(request):
    data = ''
    try:
        na=request.GET['name']
        em=request.GET['email']
        data = na + em
        url="/personal?output={}".format(data)
        return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"login.html",{'output':data} )

def register(request):
    final=''
    try: 
        if request.method == "POST":
            N=request.POST.get('N')
            E=request.POST.get('E')
            final = N + E
    except:
         pass
    return render(request,"register.html",{'output':final})

def packages(request):
    if request.method =="POST":
        s1 = int(request.POST['maths'])
        s2 = int(request.POST['stat'])
        s3 = int(request.POST['python'])
        s4 = int(request.POST['php'])
        s5 = int(request.POST['java'])
        
        total = ''
        total = s1+s2+s3+s4+s5
        print(total)
        
        percentage=(total/500)*100
        average=total/5
        context = {
            'total':total,
            'percentage':percentage,
            'average':average

        }
    
    return render(request,"packages.html",context)

def personal(request):
    if request.method == "GET":
        output = request.GET.get('output')
    
    return render(request,"personal.html", {'output':output})

def about(request):
    if request.method== "POST":
        N1=int(request.POST['val1'])
        N2=int(request.POST['val2'])
        op=request.POST['op']

        if op == '+':
            ans=N1+N2
            return render(request,"about.html",{'ans':ans})
        elif op == '-':
            ans=N1-N2
            return render(request,"about.html",{'ans':ans})
        elif op == '*':
            multi= N1*N2
            return render(request,"about.html",{'multi':multi})
        
        elif op == '/':
            div= N1/N2
            return render(request,"about.html",{'div':div})

        else:
            return HttpResponse("invalid choice")


    return render(request,"about.html")
    

   