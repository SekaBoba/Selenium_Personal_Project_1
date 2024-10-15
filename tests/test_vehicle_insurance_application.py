import pytest
from page_objects.base_page import BasePage
from page_objects.enter_vehicle_data_page import Enter_vehicle_data_page
import time
class TestProject1:

    @pytest.mark.debug
    def test1_confirm_vehicle_insurance_application_is_opened(self,driver):
        base_page=BasePage(driver)
        base_page.open()
        assert base_page.is_get_your_header_displayed()

    def test2_random_date_shown_in_input_field(self, driver):
        base_page = BasePage(driver)
        base_page.open()
        base_page.click_on_automobile_button()
        vehicle_data_page= Enter_vehicle_data_page(driver)
        vehicle_data_page.set_date_of_manufacute()
        time.sleep(10)

    """def test3_confirm_all_mandatory_fields_are_populated(self, driver):
        base_page = BasePage(driver)
        base_page.open()
        base_page.click_on_automobile_button()
        vehicle_data_page = Enter_vehicle_data_page(driver)  # kako se ovo zove, ozviljavanje klase pomocu???
        vehicle_data_page.execute_enter_vehicle_data(1000, "10/06/2023", 500, 100, 100)"""


