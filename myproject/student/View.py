from django.shortcuts import render

def home(request):


    data={
        'name':'Anjali',
        'course':'WDP',
        'college':'JG-University'
    }

    subject=['paython','Agile','BigData']
    
    return render(request, 'index.html',{'data':data,'subject_List':subject})



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')