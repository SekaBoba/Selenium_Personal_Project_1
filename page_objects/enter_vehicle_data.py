from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage

class Enter_vehicle_data_page(BasePage):
    #Locators
    __make_select_field=(By.ID,"make")
    __engine_performance_kW_input_field=(By.XPATH,"//input[@id='engineperformance']")
    __date_of_manufacture_button=(By.XPATH,"//button[@id='opendateofmanufacturecalender']")
    __number_of_seats= (By.XPATH,"//select[@id='numberofseats]")
    __number_of_seats_option = (By.XPATH,"//select[@id='numberofseats']/option[@value='6']")
    __fuel_type_select=(By.XPATH,"//select[@id='fuel']")
    __fuel_type_select_option = (By.XPATH, "//select[@id='fuel']/option[@value='Diesel']")
    __list_rice_input_field=(By.XPATH,"//input[@id='listprice']")
    __license_plate_number_input_field=(By.XPATH,"//input[@id='licenseplatenumber']")
    __annual_mileage_input_field=(By.XPATH,"//input[@id='annualmileage']")
    __next_button=(By.XPATH,"//button[@id='nextenterinsurantdata']")
