import pytest
from page_objects.base_page import BasePage


class TestProject1:

    @pytest.mark.debug
    def test1_confirm_vehicle_insurance_application_is_opened(self,driver):
        base_page=BasePage(driver)
        base_page.open()
        assert base_page.is_get_your_header_displayed()

   # def test2_random_date_shown_in_input_field(self, driver):
   # def test3_confirm_all_mandatory_fields_are_populated(self, driver):


