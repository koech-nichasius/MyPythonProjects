import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")

# wait until table rows are present
rows = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//table/tbody/tr")
    )
)

for row_index, row in enumerate(rows, start=1):
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text for cell in cells]
    print(f"Row {row_index}: {row_data}")

    if "Cierra" in row.text:
        row.find_element(
            By.XPATH, ".//a[contains(@class,'edit-wrap')]"
        ).click()

    time.sleep(30)

# wait.until(EC.element_to_be_clickable(edit_btns[2])).click()
