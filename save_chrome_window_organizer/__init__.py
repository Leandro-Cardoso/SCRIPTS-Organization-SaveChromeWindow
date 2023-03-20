from selenium import webdriver

driver = webdriver.Chrome()

# Save this data from every open window
print(driver.get_window_position())
print(driver.get_window_size())
print(driver.get_window_rect())
