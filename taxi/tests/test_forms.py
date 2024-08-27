from django.test import TestCase

from taxi.forms import (
    CarModelSearchForm,
    DriverUsernameSearchForm,
    ManufacturerNameSearchForm
)


class FormTest(TestCase):
    def test_driver_username_search_form_is_valid(self):
        form_data = {
            "username": "reichikku",
        }
        form = DriverUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_car_model_search_form_is_valid(self):
        form_data = {
            "model": "Subaru Forester",
        }
        form = CarModelSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_manufacturer_name_search_form_is_valid(self):
        form_data = {
            "name": "Subaru",
        }
        form = ManufacturerNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
