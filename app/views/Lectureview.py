from rest_framework import generics
from app.models import LecturesIF , LecturesEJ  , LecturesCO , LecturesEE , LecturesME , Sports , Complaints
from app.serializer import LectureSerializerIF , LectureSerializerCO  ,LectureSerializerEE , LectureSerializerEJ , LectureSerializerME , SportsSerializer , complaintSerializers

class LecCreateIF(generics.CreateAPIView):
    queryset = LecturesIF.objects.all()
    serializer_class = LectureSerializerIF

class LecGetIF(generics.ListAPIView):
    queryset = LecturesIF.objects.all()
    serializer_class = LectureSerializerIF



class LecCreateCO(generics.CreateAPIView):
    queryset = LecturesCO.objects.all()
    serializer_class = LectureSerializerCO

class LecGetCO(generics.ListAPIView):
    queryset = LecturesCO.objects.all()
    serializer_class = LectureSerializerCO




class LecCreateME(generics.CreateAPIView):
    queryset = LecturesME.objects.all()
    serializer_class = LectureSerializerME

class LecGetME(generics.ListAPIView):
    queryset = LecturesME.objects.all()
    serializer_class = LectureSerializerME




class LecCreateEE(generics.CreateAPIView):
    queryset = LecturesEE.objects.all()
    serializer_class = LectureSerializerEE

class LecGetEE(generics.ListAPIView):
    queryset = LecturesEE.objects.all()
    serializer_class = LectureSerializerEE




class LecCreateEJ(generics.CreateAPIView):
    queryset = LecturesEJ.objects.all()
    serializer_class = LectureSerializerEJ

class LecGetEJ(generics.ListAPIView):
    queryset = LecturesEJ.objects.all()
    serializer_class = LectureSerializerEJ


class SportsApplication(generics.CreateAPIView):
    queryset = Sports.objects.all()
    serializer_class = SportsSerializer

class GetSportsApplication(generics.ListAPIView):
    queryset = Sports.objects.all()
    serializer_class = SportsSerializer

class CreateComplaint(generics.CreateAPIView):
    queryset = Complaints.objects.all()
    serializer_class = complaintSerializers

class GetComplaint(generics.ListAPIView):
    queryset = Complaints.objects.all()
    serializer_class = complaintSerializers
