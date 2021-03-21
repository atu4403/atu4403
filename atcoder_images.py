import os
import pathlib
from selenium import webdriver
import base64


def to_bytes(elid):
    sc = "return arguments[0].toDataURL('image/png').substring(21);"
    el = driver.find_element_by_id(elid)
    b64 = driver.execute_script(sc, el)
    return base64.b64decode(b64)


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
pathlib.Path(PATH1).write_bytes(to_bytes("ratingStatus"))
pathlib.Path(PATH2).write_bytes(to_bytes("ratingGraph"))
driver.quit()
