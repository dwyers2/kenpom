import kenpompy.summary as kp
from kenpompy.utils import login
import re

browser = login("test@test.com", "test")

eff_stats = kp.get_efficiency(browser)

# for statrow in eff_stats:
#     print(statrow[1])

output = str(eff_stats.apply(lambda row: row["Conference"], axis = 1))

print(re.sub("[0-9]", "", output))

# eff_stats

# print(eff_stats)