from rest_framework import generics
from app.models import CO , EJ ,EE , IF , ME
from app.serializer import COSerializer ,EJSerializer ,EESerializer , MESerializer , IFSerializer
from rest_framework.response import Response

class COCreateAPIView(generics.CreateAPIView):
    queryset = CO.objects.all()
    serializer_class = COSerializer

class EECreateAPIView(generics.CreateAPIView):
    queryset = EE.objects.all()
    serializer_class = EESerializer

class EJCreateAPIView(generics.CreateAPIView):
    queryset = EJ.objects.all()
    serializer_class = EJSerializer

class IFCreateAPIView(generics.CreateAPIView):
    queryset = IF.objects.all()
    serializer_class = IFSerializer

class MECreateAPIView(generics.CreateAPIView):
    queryset = ME.objects.all()
    serializer_class = MESerializer

class COListAPIView(generics.ListAPIView):
    queryset = CO.objects.all()
    serializer_class = COSerializer

class EEListAPIView(generics.ListAPIView):
    queryset = EE.objects.all()
    serializer_class = EESerializer

class EJListAPIView(generics.ListAPIView):
    queryset = EJ.objects.all()
    serializer_class = EJSerializer

class MEListAPIView(generics.ListAPIView):
    queryset = ME.objects.all()
    serializer_class = MESerializer

class IFListAPIView(generics.ListAPIView):
    queryset = IF.objects.all()
    serializer_class = IFSerializer