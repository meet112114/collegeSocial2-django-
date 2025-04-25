from rest_framework import generics
from app.models import BCA , BMS , BSC , BBI , BAF
from app.serializer import BCASerializer ,BAFSerializer ,BSCSerializer , BBISerializer , BMSSerializer
from rest_framework.response import Response

class BCACreateAPIView(generics.CreateAPIView):
    queryset = BCA.objects.all()
    serializer_class = BCASerializer

class BSCCreateAPIView(generics.CreateAPIView):
    queryset = BSC.objects.all()
    serializer_class = BSCSerializer

class BAFCreateAPIView(generics.CreateAPIView):
    queryset = BAF.objects.all()
    serializer_class = BAFSerializer

class BMSCreateAPIView(generics.CreateAPIView):
    queryset = BMS.objects.all()
    serializer_class = BMSSerializer

class BBICreateAPIView(generics.CreateAPIView):
    queryset = BBI.objects.all()
    serializer_class = BBISerializer



class BCAListAPIView(generics.ListAPIView):
    queryset = BCA.objects.all()
    serializer_class = BCASerializer

class BSCListAPIView(generics.ListAPIView):
    queryset = BSC.objects.all()
    serializer_class = BSCSerializer

class BAFListAPIView(generics.ListAPIView):
    queryset = BAF.objects.all()
    serializer_class = BAFSerializer

class BBIListAPIView(generics.ListAPIView):
    queryset = BBI.objects.all()
    serializer_class = BBISerializer

class BMSListAPIView(generics.ListAPIView):
    queryset = BMS.objects.all()
    serializer_class = BMSSerializer