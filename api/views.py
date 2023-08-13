from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import InputItem
from .serializer import InputItemSerializer
from django.contrib.auth.models import User
from datetime import datetime

class InputItemAPI(APIView):
    def get(self, request):
        
        
        
        ''''''
        
        start_datetime = request.query_params.get('start_datetime')
        end_datetime = request.query_params.get('end_datetime')
        user_id = request.query_params.get('user_id')
        
        try: 
            #checking if a user with the given user_id even exists or not
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            context = {'status': 'error', 'error_response': 'User does not exist'}
            return Response(context, status=404)
        
        try: 
            start_datetime = datetime.strptime(start_datetime, "%Y-%m-%d %H:%M:%S")
            end_datetime = datetime.strptime(end_datetime, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            context = {'status': 'error', 'error_response': 'date format is not valid'}
            return Response(context, status=400)
        
        #retieving input items within the time range & ordering them by the newest ones first
        input_items = InputItem.objects.filter(user=user, input_timestamp__range=(start_datetime, end_datetime)).order_by('-input_timestamp')   
        input_items_count= input_items.count()
        serialized_input_items = InputItemSerializer(input_items, many= True) 
                
        if input_items_count==0:
            #no inputs in this time range
            response_data= { 'status': 'success',
                            'user_id': user_id,
                            'payload': 'No payloads created during the inserted time range :)'
                           } 
        else:
            response_data= { 'status': 'success',
                            'user_id': user_id,
                            'payload': serialized_input_items.data
                           } 
                
        return Response(response_data)   