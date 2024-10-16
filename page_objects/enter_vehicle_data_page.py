from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from datetime import date, timedelta
from page_objects.base_page import BasePage

class Enter_vehicle_data_page(BasePage):
    #Locators
    __make_select_field=(By.ID,"make")
    __make_select_option_audi=(By.XPATH,"//select[@id='make']/option[@value='Audi']")
    __engine_performance_kW_input_field=(By.XPATH,"//input[@id='engineperformance']")
    __date_of_manufacture_button=(By.XPATH,"//button[@id='opendateofmanufacturecalender']")

    __date_of_manufacture_input_field=(By.XPATH,"//input[@id='dateofmanufacture']")

    __date_of_manufacture_input_field_populated_icon=(By.XPATH,"//div[@class='field idealforms-field idealforms-field-text valid']/i[@class='icon']")

    __number_of_seats= (By.XPATH,"//select[@id='numberofseats']")
    __number_of_seats_option = (By.XPATH,"//select[@id='numberofseats']/option[@value='6']")
    __fuel_type_select=(By.XPATH,"//select[@id='fuel']")
    __fuel_type_select_option = (By.XPATH, "//select[@id='fuel']/option[@value='Diesel']")
    __list_rice_input_field=(By.XPATH,"//input[@id='listprice']")
    __license_plate_number_input_field=(By.XPATH,"//input[@id='licenseplatenumber']")
    __annual_mileage_input_field=(By.XPATH,"//input[@id='annualmileage']")
    __enter_vehicle_data_0=(By.XPATH,"//span[@class='counter zero']")
    __next_button=(By.XPATH,"//button[@id='nextenterinsurantdata']")



    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_enter_vehicle_data(self, engin_performance :int, date_of_manufacture:str, list_race:int, license_plate_number:int , annual_mileage:int):
        super()._click(self.__make_select_field)
        super()._click(self.__make_select_option_audi)
        super()._type(self.__engine_performance_kW_input_field, engin_performance)
        super()._type(self.__date_of_manufacture_input_field, date_of_manufacture)
        super()._click(self.__number_of_seats)
        super()._click(self.__number_of_seats_option)
        super()._click(self.__fuel_type_select)
        super()._click(self.__fuel_type_select_option)
        super()._type(self.__list_rice_input_field, list_race)
        super()._type(self.__license_plate_number_input_field, license_plate_number)
        super()._type(self.__annual_mileage_input_field,annual_mileage)
        assert super()._is_displayed(self.__enter_vehicle_data_0)



    @property
    def set_yesterday_date_of_manufacute(self)->str:
        return (date.today() - timedelta(days=1)).strftime("%m/%d/%Y")

    def set_date_of_manufacute(self)->str:
        super()._type(self.__date_of_manufacture_input_field, self.set_yesterday_date_of_manufacute)
        assert super()._is_displayed(self.__date_of_manufacture_input_field_populated_icon)

