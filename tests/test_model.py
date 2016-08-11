# -*- coding: utf-8 -*-
from unittest import TestCase

from django_antimat.models import Mat
from .models import TestAntimat


class ModelTestCase(TestCase):
    def setUp(self):
        self.test_text = u'Гуляла корова по полю'
        self.replaced_text = u'Гуляла ****** по полю'
        self.stop_word = Mat(word='коровы')
        self.stop_word.save()

    def test_replace_field_body(self):
        m = TestAntimat(text=self.test_text)
        self.assertEqual(m.text, self.replaced_text)
        m.text = self.test_text
        self.assertEqual(m.text, self.replaced_text)

    def test_create(self):
        m = TestAntimat.objects.create(text=self.test_text)
        self.assertEqual(m.text, self.replaced_text)
        m.text = self.test_text
        self.assertEqual(m.text, self.replaced_text)