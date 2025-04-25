from rest_framework import generics
from app.models import LecturesBMS , LecturesBAF , LecturesBCA , LecturesBSC , LecturesBBI , Sports , Complaints
from app.serializer import LectureSerializerBMS , LectureSerializerBCA  ,LectureSerializerBBI , LectureSerializerBSC , LectureSerializerBAF , SportsSerializer , complaintSerializers

class LecCreateBCA(generics.CreateAPIView):
    queryset = LecturesBCA.objects.all()
    serializer_class = LectureSerializerBCA

class LecGetBCA(generics.ListAPIView):
    queryset = LecturesBCA.objects.all()
    serializer_class = LectureSerializerBCA



class LecCreateBMS(generics.CreateAPIView):
    queryset = LecturesBMS.objects.all()
    serializer_class = LectureSerializerBMS

class LecGetBMS(generics.ListAPIView):
    queryset = LecturesBMS.objects.all()
    serializer_class = LectureSerializerBMS




class LecCreateBAF(generics.CreateAPIView):
    queryset = LecturesBAF.objects.all()
    serializer_class = LectureSerializerBAF

class LecGetBAF(generics.ListAPIView):
    queryset = LecturesBAF.objects.all()
    serializer_class = LectureSerializerBAF




class LecCreateBBI(generics.CreateAPIView):
    queryset = LecturesBBI.objects.all()
    serializer_class = LectureSerializerBBI

class LecGetBBI(generics.ListAPIView):
    queryset = LecturesBBI.objects.all()
    serializer_class = LectureSerializerBBI




class LecCreateBSC(generics.CreateAPIView):
    queryset = LecturesBSC.objects.all()
    serializer_class = LectureSerializerBSC

class LecGetBSC(generics.ListAPIView):
    queryset = LecturesBSC.objects.all()
    serializer_class = LectureSerializerBSC


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

