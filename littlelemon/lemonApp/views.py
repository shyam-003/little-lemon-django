from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def about(request):
    return render(request, 'about.html')

from .models import *
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .forms import BookingForm


# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message" : "this is a secret message"})

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})


def book(request):
    form = BookingForm()
    submitted_data = None
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form  = BookingForm()
    context = {'form':form}
    return render(request, 'book.html', context)


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer