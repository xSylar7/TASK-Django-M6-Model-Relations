import pytest
from django.db.models import Model, OneToOneField

from classes import models


def test_many_to_many() -> None:
    is_in_tag = hasattr(models.Tag, "courses")
    is_in_course = hasattr(models.Course, "tags")
    assert (
        is_in_tag or is_in_course
    ), "No m2m relation found between Course-Tag, are you sure you named them `tags` and `courses`"

    if is_in_tag:
        m2m_field = models.Tag.courses
        other = models.Course
    else:
        m2m_field = models.Course.tags
        other = models.Tag

    assert m2m_field.field.many_to_many is True
    assert m2m_field.rel.model is other


def test_many_to_one() -> None:
    assert hasattr(models.Lecture, "course"), "Are you sure you named your FK `course`?"

    assert models.Lecture.course.field.many_to_one is True
    assert models.Lecture.course.field.related_model is models.Course


@pytest.mark.parametrize("model", [models.Slide, models.Assignment])
def test_one_to_one(model: type[Model]) -> None:
    assert hasattr(model, "lecture")

    field: OneToOneField = model.lecture.field
    assert field.one_to_one is True
    assert field.related_model is models.Lecture
    assert field.primary_key is True
