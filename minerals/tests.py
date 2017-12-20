from django.test import TestCase
from django.urls import reverse
from django.db import IntegrityError
from .models import Mineral

# Create your tests here.

class MineralModelTests(TestCase):
    def setUp(self):
        self.mineral_one = Mineral.objects.create(
            name="MineratiTesti",
            image_filename='mineratitesti.jpg',
            image_caption='caption test',
            category='category test',
            formula='C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni',
            color='colortest',
            refractive_index='refractivetest'
        )

        self.mineral_two = Mineral.objects.create(
            name="MineratiTestiTwo",
            image_filename='mineratitesti.jpg',
            image_caption='caption test',
            category='category test',
            formula='C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni',
            color='colortest',
            refractive_index='refractivetest'
    )

    def test_mineral_creation(self):
        all_minerals = Mineral.objects.all()
        self.assertIn(self.mineral_one, all_minerals)
        self.assertIn(self.mineral_two, all_minerals)

        with self.assertRaises(IntegrityError):
            # to test unique name unqiuness
            self.mineral_three = Mineral.objects.create(
                name="MineratiTesti",
                image_filename='mineratitesti.jpg',
                image_caption='caption test',
                category='category test',
                formula='C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni',
                color='colortest',
                refractive_index='refractivetest')


class MineralsViews(TestCase):
    def setUp(self):
        self.mineral_one = Mineral.objects.create(
            name="MineratiTesti",
            image_filename='mineratitesti.jpg',
            image_caption='caption test',
            category='category test',
            formula='C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni',
            color='colortest',
            refractive_index='refractivetest')

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_one, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, self.mineral_one.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'pk':self.mineral_one.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral_one, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertContains(resp, self.mineral_one.name)

