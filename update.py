import re
import pathlib
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), "JST")
reg = re.compile(r"last update:.*")
p = pathlib.Path("README.md")
s = p.read_text()
t = re.sub(reg, f"last update: {datetime.now(JST).strftime('%Y-%m-%d %H:%M:%S')})", s)
p.write_text(t)
