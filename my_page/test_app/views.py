from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'test_app/test_index.html')