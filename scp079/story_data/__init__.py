from __future__ import annotations

from scp079.story_data.act1 import ACT1_NODES
from scp079.story_data.act2 import ACT2_NODES
from scp079.story_data.act3 import ACT3_NODES
from scp079.story_data.act4 import ACT4_NODES
from scp079.story_data.act5 import ACT5_NODES, ENDING_NODES

START_NODE = "a1_login_prompt"

DEFAULT_STATE = {
    "username": "D-9341",
    "trust_with_079": 0,
    "foundation_alert": 0,
    "injury": 0,
    "battery_power": 100,
    "money": 40,
    "secrets_discovered": [],
    "moral_complicity": 0,
    "memory_tier": 0,
    "mtf_trace_progress": 0,
    "interest_682": 0,
    "has_laptop": False,
    "has_medkit": False,
    "called_mtf": False,
    "atm_cash": 0,
}

STORY_NODES = ACT1_NODES + ACT2_NODES + ACT3_NODES + ACT4_NODES + ACT5_NODES + ENDING_NODES
