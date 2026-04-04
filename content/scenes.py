# ============================================================
#  content/scenes.py
#  Aggregates all act scene dictionaries into one SCENES dict.
#  Add new acts here as they are implemented.
# ============================================================

from content.act1 import SCENES as _ACT1
from content.act2 import SCENES as _ACT2
from content.act3 import SCENES as _ACT3

SCENES = {**_ACT1, **_ACT2, **_ACT3}
