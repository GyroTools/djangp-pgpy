import pytest

from auth import ModelUserWithIdentityBackend
from django_pgpy.models import Identity


@pytest.mark.django_db
class TestModelUserWithIdentityBackend:
    def test_authenticate(self, rf, user_test_data):
        test_data = user_test_data
        request = rf.get('/login')

        backend = ModelUserWithIdentityBackend()

        assert Identity.objects.exists_for_user(test_data.user_1) is False
        backend.authenticate(request, username=test_data.user_1.username, password=test_data.pwd_user_1)

        assert Identity.objects.exists_for_user(test_data.user_1)

        uid: Identity = test_data.user_1.pgp_identity
        assert uid.private_key.is_protected

        with uid.unlock(test_data.pwd_user_1):
            assert uid.private_key.is_unlocked

    def test_authenticate__have_already_an_identity(self, rf, user_identity_test_data):
        test_data = user_identity_test_data
        request = rf.get('/login')

        backend = ModelUserWithIdentityBackend()

        assert Identity.objects.exists_for_user(test_data.user_1)
        assert Identity.objects.filter(user=test_data.user_1).count() == 1
        backend.authenticate(request, username=test_data.user_1.username, password=test_data.pwd_user_1)

        assert Identity.objects.exists_for_user(test_data.user_1)
        assert Identity.objects.filter(user=test_data.user_1).count() == 1

        uid: Identity = test_data.user_1.pgp_identity
        assert uid.private_key.is_protected

        with uid.unlock(test_data.pwd_user_1):
            assert uid.private_key.is_unlocked
