from rest_framework import generics


class BaseGenericAPIView:
    """
    Common properties and logic shared by all API
    """
    pass


class BaseListCreateAPIView(BaseGenericAPIView, generics.ListCreateAPIView):
    """
    Base list and create API
    """
    pass


class BaseRetrieveUpdateDeleteAPIView(BaseGenericAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    Base retrieve, update and delete API
    """
    model = None

    def get_queryset(self):
        """
        Override version of get_queryset from Base
        """
        if self.model is not None:
            return self.model.objects.all()

        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )
