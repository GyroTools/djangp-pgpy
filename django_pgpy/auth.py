from django.contrib.auth.backends import ModelBackend


class ModelUserWithIdentityBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        from django_pgpy.models import Identity

        user = super().authenticate(request, username, password, **kwargs)
        if user and user.is_authenticated and not Identity.objects.exists_for_user(user):
            Identity.objects.create(user, password)
        return user
