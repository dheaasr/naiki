from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406437262',
        'name': 'Dhea Anggrayningsih Syah Rony',
        'class': 'PBP C',
    }

    return render(request, "main.html", context)
