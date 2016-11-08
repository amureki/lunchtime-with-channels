import pytest

from votes.models import Vote


@pytest.mark.django_db
class TestVote:
    def test_update(self, place, username):
        from django.utils import translation
        from django.conf import settings
        print(settings.LANGUAGE_CODE)
        print(translation.get_language())
        assert not Vote.objects.exists()
        Vote.update(place.id, username)
        assert Vote.objects.exists()
