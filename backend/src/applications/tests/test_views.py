from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from applications.models import Application
from django.utils import timezone

class ApplicationViewTests(TestCase):
    def test_get_submit_application_page(self):
        response = self.client.get(reverse("submit_application"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "application_form.html")

    def test_post_submit_application(self):
        test_file = SimpleUploadedFile("test_file.txt", b"test_content")

        response = self.client.post(reverse("submit_application"), {
            "applicant_name": "test_name",
            "country_of_origin": "test_country",
            "supporting_document": test_file
        })

        test_application = Application.objects.get(applicant_name = "test_name")
        self.assertEqual(test_application.country_of_origin, "test_country")
        self.assertEqual(test_application.submission_date, timezone.now().date())
        self.assertEqual(test_application.status, "pending")

        self.assertRedirects(response, "/applications/success/")
    
    def test_get_application_success(self):
        response = self.client.get(reverse("application_success"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "application_success.html")

    def test_get_view_applications(self):
        applications = [
            Application(applicant_name="test_name_1", country_of_origin="test_country_1"), 
            Application(applicant_name="test_name_2", country_of_origin="test_country_2")
        ]
        Application.objects.bulk_create(applications)

        response = self.client.get(reverse("view_applications"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test_name_1")
        self.assertContains(response, "test_name_2")