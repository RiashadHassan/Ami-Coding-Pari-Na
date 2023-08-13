from rest_framework import serializers
from base.models import InputItem

class InputItemSerializer(serializers.ModelSerializer):

    input_timestamp = serializers.SerializerMethodField()
    
    def get_input_timestamp(self, obj):
        
        return obj.input_timestamp.strftime("%Y-%m-%d %H:%M:%S")
        
    class Meta:
        model = InputItem
        fields = [field.name for field in model._meta.fields] + ['input_timestamp']