from selenium import webdriver

driver = webdriver.Chrome('./drivers/chromedriver.exe')

# Switch windows:
#driver.switch_to.window('main')

# Test:
driver.get('https://github.com/Leandro-Cardoso')

# Save this data from every open window
# get_window_rect -> set_window_rect
print(driver.get_window_rect())

# Tabs ids
window_ids = driver.window_handles
window_id = driver.current_window_handle
print(window_id)
print(window_ids)
