from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from user.models import Userdata
from django.views import View


class createUpdate(View):
    
    def get(self, request, pk=None, *args, **kwargs):
        import pdb;pdb.set_trace
        
        if pk:
            result = Userdata.objects.get(id=pk)
            context = {'result': result}
            return render(request, 'user/edit.html', context)
        else:
            return render(request, 'user/create.html')
    
    #create and update both requires POST HTTP method(becouse we need request body) , only diffrence is upodate reqired pk , and create dont required it
    def post(self, request, pk=None, *args, **kwargs):
        import pdb;pdb.set_trace()
        if pk:
            instance = Userdata.objects.get(id=pk)
            instance.title = request.POST.get('title')
            instance.description = request.POST.get('description')
            instance.save()
            return redirect('/user/get')
        else:
            Userdata.objects.create(title= request.POST.get('title'),description = request.POST.get('description'))
            return redirect('/user/get')

class getDelete(View):
    #rename read=  get
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            result = Userdata.objects.get(id=pk)
            result.delete()
            return redirect('/user/get')  
        result = Userdata.objects.all()
        data = {'result': result}
        return render(request, 'user/read.html', data)

    def post(self, request, pk=None, *args, **kwargs):
        pass    
        


