from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', )


'''  The below can be used but since django-auth is good for handling Authentications via API it was used in this project'''




# class UserDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'first_name',
#             'last_name',
#         ]




# class UserCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(label='Password', write_only=True, required=True,
#                                         style={'input_type': 'password', 'placeholder': 'Password'})
#     password2 = serializers.CharField(label='Confirm Password', write_only=True, required=True,
#                                         style={'input_type': 'password', 'placeholder': 'Password'})

#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password',
#             'password2',
            
#         ]

#     def validate_password(self, value):
#         data = self.get_initial()
#         pass1 = data.get("password")
#         pass2 = data.get("password2")
#         if pass1 != pass2:
#             raise serializers.ValidationError("Passwords must match.")
#         return value


#     def create(self, validated_data):
#         username = validated_data['username']
#         email = validated_data['email']
#         password = validated_data['password']
#         user_obj = User(
#                 username = username,
#                 email = email
#             )
#         user_obj.set_password(password)
#         user_obj.save()
#         return validated_data



# class UserLoginSerializer(serializers.ModelSerializer):
#     username = serializers.CharField()
#     password = serializers.CharField(label='Password', write_only=True, required=True,
#                                         style={'input_type': 'password', 'placeholder': 'Password'})
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password',
#         ]
#         extra_kwargs = {"password":
#                             {"write_only": True}
#                             }
#     def validate(self, data):
#         print("serializers ValidationError",data)
#         username = data['username']
#         password = data['password']
#         print(username , password)
#         user_qs = authenticate(username=username , password=password)
#         print
#         if not user_qs:
#             raise serializers.ValidationError("Please enter valid username and password.")
#         return data


