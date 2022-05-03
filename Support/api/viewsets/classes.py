from rest_framework import mixins, viewsets


class MixedPermission:
    """Permissions for actions"""
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
    pass


class CreateListS(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """"""
    pass


class UpdateDestroyS(mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    """"""
    pass
