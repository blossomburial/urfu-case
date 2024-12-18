from django.test import TestCase
from django.contrib.auth.models import User
from jobs.models import Jobs, Application, UserProfile
from jobs.forms import ApplicationForm
from django.urls import reverse

class JobsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="password123")
        self.job = Jobs.objects.create(
            title="тест",
            desc="тест",
            type_of_job="full_time",
            salary="100000",
            author=self.user,
        )

    def test_job_creation(self):
        self.assertEqual(self.job.title, "тест")
        self.assertEqual(self.job.author, self.user)
        self.assertEqual(str(self.job), "тест")

class JobsFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="password123")
        self.job = Jobs.objects.create(
            title="тест",
            desc="тест",
            type_of_job="full_time",
            salary="100000",
            author=self.user,
        )

    def test_invalid_form(self):
        form_data = {
            'desc': "", 
        }
        form = ApplicationForm(data=form_data)
        self.assertFalse(form.is_valid())

class ApplicationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'cover_letter': "сопр письмо",
        }
        form = ApplicationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'cover_letter': "", 
        }
        form = ApplicationForm(data=form_data)
        self.assertFalse(form.is_valid())

class ApplicationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="password123")
        self.job = Jobs.objects.create(
            title="тест",
            desc="тест",
            type_of_job="full_time",
            salary="100000",
            author=self.user,
        )
        self.application = Application.objects.create(
            user=self.user,
            job=self.job,
            cover_letter="сопр письмо",
        )

    def test_application_creation(self):
        self.assertEqual(self.application.user, self.user)
        self.assertEqual(self.application.job, self.job)
        self.assertEqual(self.application.cover_letter, "сопр письмо")

class JobsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="password123")
        self.job = Jobs.objects.create(
            title="тест",
            desc="тест",
            type_of_job="full_time",
            salary="100000",
            author=self.user,
        )

    def test_jobs_home_view(self):
        response = self.client.get(reverse('jobs-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/index.html')
        self.assertContains(response, "тест")

    def test_job_detail_view(self):
        response = self.client.get(reverse('job-detail', args=[self.job.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/job_detail.html')
        self.assertContains(response, "тест")

class ApplicationViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="password123")
        self.job = Jobs.objects.create(
            title="тест",
            desc="тест",
            type_of_job="full_time",
            salary="100000",
            author=self.user,
        )

    def test_apply_for_job_view(self):
        self.client.login(username="test", password="password123")
        response = self.client.post(reverse('job-apply', args=[self.job.id]), {
            'cover_letter': "сопр письмо",
        })
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Application.objects.filter(user=self.user, job=self.job).exists())

class ApplicationDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="password123")
        self.other_user = User.objects.create_user(username="test1", password="password123")
        self.job = Jobs.objects.create(
            title="тест",
            desc="тест",
            type_of_job="full_time",
            salary="100000",
            author=self.user,
        )
        self.application = Application.objects.create(
            user=self.user,
            job=self.job,
            cover_letter="сопр письмо",
        )

    def test_delete_own_application(self):
        self.client.login(username="test", password="password123")
        response = self.client.post(reverse('job-apply-delete', args=[self.application.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Application.objects.filter(id=self.application.id).exists())

    def test_delete_other_user_application(self):
        self.client.login(username="test1", password="password123")
        response = self.client.post(reverse('job-apply-delete', args=[self.application.id]))
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Application.objects.filter(id=self.application.id).exists())
