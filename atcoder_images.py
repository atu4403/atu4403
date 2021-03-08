import os
import pathlib
from selenium import webdriver

USERNAME = os.environ.get("ATCODER_USERNAME")
assert USERNAME, "Is required env.ATCODER_USERNAME"
PATH1 = os.environ.get("ATCODER_STATUS_PATH") or "images/ratingStatus.png"
PATH2 = os.environ.get("ATCODER_GRAPH_PATH") or "images/ratingGraph.png"
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=options.to_capabilities(),
    options=options,
)
driver.get(f"https://atcoder.jp/users/{USERNAME}")
driver.implicitly_wait(30)
png1 = driver.find_element_by_id("ratingStatus").screenshot_as_png
png2 = driver.find_element_by_id("ratingGraph").screenshot_as_png
pathlib.Path(PATH1).write_bytes(png1)
pathlib.Path(PATH2).write_bytes(png2)
driver.quit()
