from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Cat',
        'amount': '1',
        'description': 'Something',
        'category': 'Something else'
    }

    return render(request, "main.html", context)
