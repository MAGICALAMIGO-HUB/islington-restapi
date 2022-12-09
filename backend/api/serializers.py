from rest_framework import serializers
from.models import Artical
class AritcalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artical
        # fields = ['id','title','body']
        fields = '__all__'