import json

import pytest
from rest_framework.test import APIRequestFactory

from .models import PerevalAdd
from .views import PerevalAddViewSet


@pytest.fixture
def factory():
    return APIRequestFactory()


def test_create_pereval(factory):
    data = {
        "title": "Test Pereval",
        "beautyTitle": "Beautiful Pereval",
        "other_titles": "Other Titles",
        "connect": "Connection Information",
        "level_winter": "Winter Level",
        "level_summer": "Summer Level",
        "level_autumn": "Autumn Level",
        "level_spring": "Spring Level",
        "coords": {
            "latitude": 12.345,
            "longitude": 67.890,
            "height": 1000
        }
    }

    request = factory.post('/api/perevals/', data=json.dumps(data), content_type='application/json')
    view = PerevalAddViewSet.as_view({'post': 'create'})
    response = view(request)

    assert response.status_code == 200
    assert PerevalAdd.objects.count() == 1
    assert response.data['status'] == 200
    assert response.data['message'] == 'Отправлено успешно'
    assert 'id' in response.data


def test_create_pereval_invalid_data(factory):
    data = {
        # Invalid data with missing required fields
    }

    request = factory.post('/api/perevals/', data=json.dumps(data), content_type='application/json')
    view = PerevalAddViewSet.as_view({'post': 'create'})
    response = view(request)

    assert response.status_code == 400
    assert PerevalAdd.objects.count() == 0
    assert response.data['status'] == 400
    assert 'message' in response.data


def test_edit_pereval(factory):
    pereval = PerevalAdd.objects.create(
        title="Test Pereval",
        beautyTitle="Beautiful Pereval",
        other_titles="Other Titles",
        connect="Connection Information",
        level_winter="Winter Level",
        level_summer="Summer Level",
        level_autumn="Autumn Level",
        level_spring="Spring Level",
        status="new"
    )

    data = {
        "title": "Updated Pereval",
        "level_winter": "Updated Winter Level",
        # Other fields for update
    }

    request = factory.put(f'/api/perevals/{pereval.pk}/', data=json.dumps(data), content_type='application/json')
    view = PerevalAddViewSet.as_view({'put': 'edit_pereval'})
    response = view(request, pk=pereval.pk)

    assert response.status_code == 200
    assert PerevalAdd.objects.get(pk=pereval.pk).title == "Updated Pereval"


def test_edit_pereval_invalid_status(factory):
    pereval = PerevalAdd.objects.create(
        title="Test Pereval",
        beautyTitle="Beautiful Pereval",
        other_titles="Other Titles",
        connect="Connection Information",
        level_winter="Winter Level",
        level_summer="Summer Level",
        level_autumn="Autumn Level",
        level_spring="Spring Level",
        status="accepted"  # Set status to a non-'new' value
    )

    data = {
        "title": "Updated Pereval",
        "level_winter": "Updated Winter Level",
        # Other fields for update
    }

    request = factory.put(f'/api/perevals/{pereval.pk}/', data=json.dumps(data), content_type='application/json')
    view = PerevalAddViewSet.as_view({'put': 'edit_pereval'})
    response = view(request, pk=pereval.pk)

    assert response.status_code == 400
    assert PerevalAdd.objects.get(pk=pereval.pk).title == "Test Pereval"
