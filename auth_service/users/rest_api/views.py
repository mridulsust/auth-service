from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from auth_service.common.api_views import BaseListCreateAPIView, BaseRetrieveUpdateDeleteAPIView
from .serializers import UserInputSerializer, UserOutputSerializer


User = get_user_model()


class UserListCreateAPIView(BaseListCreateAPIView):
    http_method_names = ['post']
    permission_classes = [AllowAny]
    serializer_class = UserInputSerializer
    output_serializer_class = UserOutputSerializer

    def create(self, request, *args, **kwargs):
        """
        Override version of perform_create of DRF. We just used a different serializer for output
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # CUSTOM: We are returning and receiving user object here
        user_instance = self.perform_create(serializer)
        # CUSTOM: Use different serializer for output
        output_serializer = self.output_serializer_class(user_instance)
        headers = self.get_success_headers(output_serializer.data)
        return Response(
            output_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        """
        Override version of perform_create of DRF.

        Original implementation: serializer.save() but the recommended way to create user is create_user
        """
        user_instance = User.objects.create_user(**serializer.data)
        return user_instance


class UserRetrieveUpdateDeleteAPIView(BaseRetrieveUpdateDeleteAPIView):
    model = User
    lookup_field = "uuid"
    serializer_class = UserInputSerializer

    def get_object(self):
        """
        We are overriding it to block cross user access
        """
        user_obj = super().get_object()
        if user_obj != self.request.user:
            raise Http404
        return user_obj

    def perform_update(self, serializer):
        """
        Override version of perform_create of DRF.

        Original implementation: serializer.save() but that doesn't update password
        """
        serializer.save()
        if "password" in serializer.data:
            password = serializer.data["password"]
            serializer.instance.set_password(password)
            serializer.instance.save()
