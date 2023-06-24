from django. http import HttpResponse
from django.shortcuts import render



def about(request):
    # return HttpResponse('hey im the big ')
    if request.method == 'POST':
        num1 = int(request.POST.get('name1'))
        num2 = int(request.POST.get('name2'))
        operator = request.POST.get('opr')
        print(num1)
        print(num2)
        print(operator)

        if operator == '+':
            sum = num1 + num2

            context = {'key':sum}
            return render(request,'result.html',context) 


        if operator == '-':
            diff = num1-num2
            context = { 'key' : diff}

            return render(request,'result.html',context)


        if operator == '*':
            mul = num1*num2
            context = { 'key': mul}

            return render(request,'result.html', context)



        if operator == '-':
            div = num1/num2
            context = { 'key' : div}

            return render(request,'result.html',context)


        else:
            return HttpResponse('error')





  

def index(request ):
    return render(request,'base.html')

    



