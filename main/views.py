from django.shortcuts import render

# Create your views here.
def acceuil(request):

   if request.session ['c']==1 :
            
      return render(request,'main/index.html')
    
          
   else:
      
        return render (request,'login')
     
     
      
    


def App(request) :
  return render(request,'main/app.html')
def auth(request) :
  return render(request,'main/auth.html')

