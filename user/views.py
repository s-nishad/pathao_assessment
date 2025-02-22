from datetime import timedelta

from django.utils.timezone import now
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import User, UserTag
from .serializers import UserSerializer, UserDetailSerializer, UserTagSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter


class UserOperation(APIView):
    serializer_class = UserSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="tags",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Comma-separated list of tags",
                required=True
            )
        ],
        responses={200: "Success"},
    )
    def get(self, request):
        tags_param = request.query_params.get("tags", "")
        tags = [tag.strip() for tag in tags_param.split(",") if tag.strip()]

        if not tags:
            return Response({"error": "No valid tags provided"}, status=status.HTTP_400_BAD_REQUEST)

        users = User.objects.filter(tags__tag__in=tags).distinct()
        # users = User.objects.filter(tags__tag__in=tags, tags__expiry__gt=now()).distinct()

        data = [
            {
                "id": user.id,
                "name": f"{user.firstName} {user.lastName}",
                "tags": list(user.tags.all().values_list("tag", flat=True))
            }
            for user in users
        ]

        return Response({"users": data}, status=status.HTTP_200_OK)

    @extend_schema(request=UserSerializer, responses={201: "User created"})
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"id": user.id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreateUserView(APIView):
#     serializer_class = UserSerializer
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"id": user.id}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUserView(APIView):
    # lookup_field = 'id'

    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddUserTagsView(APIView):
    serializer_class = UserTagSerializer

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserTagSerializer(data=request.data)
        if serializer.is_valid():
            tags = serializer.validated_data["tags"]
            expiry_time = now() + timedelta(milliseconds=serializer.validated_data["expiry"])
            for tag in tags:
                UserTag.objects.update_or_create(
                    user=user,
                    tag=tag,
                    defaults={'expiry': expiry_time}
                )
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GetUsersByTagsView(APIView):
#     def get(self, request):
#         tags = request.query_params.get("tags", "").split(",")
#         users = User.objects.filter(tags__tag__in=tags).distinct()
#         # users = User.objects.filter(tags__tag__in=tags, tags__expiry__gt=now()).distinct()
#
#         data = [
#             {
#                 "id": user.id,
#                 "name": f"{user.firstName} {user.lastName}",
#                 "tags": list(user.tags.all().values_list("tag", flat=True))
#             }
#             for user in users
#         ]
#         return Response({"users": data}, status=status.HTTP_200_OK)
