import re
import pathlib
import datetime as dt

reg = re.compile(r"last update:.*")
p = pathlib.Path("README.md")
s = p.read_text()
t = re.sub(reg, f"last update: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})", s)
p.write_text(t)
