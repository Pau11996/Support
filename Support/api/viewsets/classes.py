from rest_framework import mixins, viewsets


class MixedPermission:
    """Mixin for simplified configuration of permissions depending on action in view."""
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CreateListRetrieveUpdateDestroyS(mixins.CreateModelMixin,
                                       mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.ListModelMixin,
                                       mixins.DestroyModelMixin,
                                       MixedPermission,
                                       viewsets.GenericViewSet):
    """Viewset with all action and custom MixedPermission."""
    pass


class CreateListS(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """Viewset to view a list of messages and create a single message."""
    pass


class UpdateDestroyS(mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """Viewset to update and destroy messages only superuser."""
    pass
