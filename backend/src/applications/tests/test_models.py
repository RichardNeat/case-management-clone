# Create your tests here.

from django.test import TestCase
from applications.models import Application
from django.utils import timezone

class ApplicationTestCase(TestCase):
    def setUp(self):
        Application.objects.create(
            applicant_name = "test_name",
            country_of_origin = "test_country",
        )

    def test_application_content(self):
        test_application = Application.objects.get(applicant_name = "test_name")
        self.assertEqual(test_application.country_of_origin, "test_country")
        self.assertEqual(test_application.submission_date, timezone.now().date())
        self.assertEqual(test_application.status, "pending")