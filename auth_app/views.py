from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import api_view
from .serializers import LoginSerializer
from rest_framework import status
from .models import Person

# Create your views here.

@api_view(['POST'])
def login(request):
	serializer = LoginSerializer(data=request.data, context={'request': request})
	serializer.is_valid(raise_exception=True)
	user = serializer.validated_data['user']
	# login(request, user)
	print(f"USER : {user}")
	token = AccessToken.for_user(user)
	return JsonResponse(
		{'id': user.id, 'username': user.username, 'first_name': user.first_name, 'token': str(token)},
		status=status.HTTP_200_OK)


@api_view(['POST'])
def create_person(request):
	persons = Person.objects.all()
	if request.user.is_authenticated:
		name = request.data.get('name')
		age = request.data.get('age')
		print(f"name : {name} age: {age}")
		print('hshs', list(Person.objects.values_list('id', flat=True)))
		if name not in list(Person.objects.values_list('name', flat=True)):
			p = Person.objects.create(name=name, age=age)
			p.save()
			return Response(
				{"created_person":f"New person added - {p.name}", 'Persons': [person.name for person in persons], "p":list(Person.objects.values_list('name', flat=True))},
				status=status.HTTP_200_OK)
		else:
			return Response(
				{"Not Possible Person": f"Person already exists with the same name", 'Persons': [person.name for person in persons]},
				status=status.HTTP_200_OK)

	return Response(
		{'details':"Authentication Needed to perform this action!"},
		status=status.HTTP_200_OK)

@api_view(['get'])
def hello(request):
	return Response({"details":"Hello function"}, status=status.HTTP_200_OK)


