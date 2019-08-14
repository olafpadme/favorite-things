from django.test import TestCase
from core import models


def sample_category(title='place'):
    """Create a sample category"""
    return models.Category.objects.create(title=title)


class ModelTests(TestCase):

    def test_category_str(self):
        """Test the category string representation"""
        category = models.Category.objects.create(
            title='Person'
        )

        self.assertEqual(str(category), category.title)

    def test_audit_log_str(self):
        """Test the audit-log string representation"""
        audit_log = models.AuditLog.objects.create(
            description='Changed some of the things in for the test purposes. '
        )

        self.assertEqual(str(audit_log), audit_log.description[:42])

    def test_favorite_thing_str(self):
        """Test the recipe string representation"""
        favorite_thing = models.FavoriteThing.objects.create(
            title='Test title',
            rank=1,
            category=sample_category()

        )

        self.assertEqual(str(favorite_thing), favorite_thing.title)
