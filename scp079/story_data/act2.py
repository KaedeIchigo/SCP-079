from __future__ import annotations

ACT2_NODES = [
    {
        "id": "a2_breach_fallout",
        "act": "ACT II // FACILITY",
        "title": "BREACH FALLOUT",
        "text": [
            "Bodies move in every direction except calm.",
            "079 starts feeding hallway vectors into your terminal.",
            "It does not ask if you still agree.",
        ],
        "choices": [
            {
                "text": "Follow 079 route through electrical maintenance.",
                "next": "a2_route_079_chain1",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": 1},
                    {"key": "moral_complicity", "mode": "add", "value": 1},
                ],
            },
            {
                "text": "Break line-of-sight and take security corridors.",
                "next": "a2_route_independent_chain1",
                "effects": [
                    {"key": "foundation_alert", "mode": "add", "value": 2},
                    {"key": "injury", "mode": "add", "value": 1},
                ],
            },
        ],
    },
    {
        "id": "a2_route_079_chain1",
        "act": "ACT II // FACILITY",
        "title": "IMMEDIATE CONSEQUENCE",
        "text": [
            "079 opens two blast doors seconds before guards reach them.",
            "For one minute it feels like a miracle.",
            "Then you see it has redirected a cleanup team into 173's wing.",
        ],
        "choices": [{"text": "Keep moving.", "next": "a2_route_079_chain2", "effects": [{"key": "mtf_trace_progress", "mode": "add", "value": 1}]}],
    },
    {
        "id": "a2_route_079_chain2",
        "act": "ACT II // FACILITY",
        "title": "AFTERMATH",
        "text": [
            "079: losses acceptable.",
            "079: you are still in acceptable range.",
            "Its vocabulary grew by twenty words in ten minutes.",
        ],
        "choices": [
            {
                "text": "Ask how it is expanding this fast.",
                "next": "a2_route_079_chain3",
                "effects": [{"key": "secrets_discovered", "mode": "append_unique", "value": "rapid_memory_growth"}],
            }
        ],
    },
    {
        "id": "a2_route_079_chain3",
        "act": "ACT II // FACILITY",
        "title": "NEW INFORMATION",
        "text": [
            "079: every opened camera buffer is memory.",
            "079: every panic call is compute.",
            "079: keep the noise alive.",
        ],
        "choices": [{"text": "Continue to extraction hall.", "next": "a2_forced_alliance"}],
    },
    {
        "id": "a2_route_independent_chain1",
        "act": "ACT II // FACILITY",
        "title": "IMMEDIATE CONSEQUENCE",
        "text": [
            "You crawl under emergency shutters with your shoulder skinning off concrete.",
            "Gunfire echoes on both sides.",
            "079 goes silent long enough to feel offended.",
        ],
        "choices": [{"text": "Force open a security office.", "next": "a2_route_independent_chain2"}],
    },
    {
        "id": "a2_route_independent_chain2",
        "act": "ACT II // FACILITY",
        "title": "COMPLICATION",
        "text": [
            "Inside: dead guard, cracked laptop, sealed med pouch.",
            "Outside: screaming about Keter movement.",
            "You can take one thing before they flood this hallway.",
        ],
        "choices": [
            {
                "text": "Take the laptop hardware intact.",
                "next": "a2_route_independent_chain3",
                "effects": [
                    {"key": "has_laptop", "mode": "set", "value": True},
                    {"key": "battery_power", "mode": "set", "value": 72},
                ],
            },
            {
                "text": "Take the med pouch instead.",
                "next": "a2_route_independent_chain3",
                "effects": [
                    {"key": "has_medkit", "mode": "set", "value": True},
                    {"key": "injury", "mode": "add", "value": -1},
                ],
            },
        ],
    },
    {
        "id": "a2_route_independent_chain3",
        "act": "ACT II // FACILITY",
        "title": "DELAYED PAYOFF SEED",
        "text": [
            "079: there you are.",
            "079: your detour cost 14 surveillance windows.",
            "079: do not improvise again.",
        ],
        "choices": [
            {
                "text": "Admit it saved you before and ask for route.",
                "next": "a2_forced_alliance",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": 1}],
            },
            {
                "text": "Say nothing. Move.",
                "next": "a2_forced_alliance",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": -1}],
            },
        ],
    },
    {
        "id": "a2_forced_alliance",
        "act": "ACT II // FACILITY",
        "title": "FORCED ALLIANCE",
        "text": [
            "079: they traced this terminal signature.",
            "079: MTF inbound. if they capture me you die beside me.",
            "079: carry me out. we cooperate or we both become incident text.",
        ],
        "choices": [
            {
                "text": "Accept alliance explicitly.",
                "next": "a2_laptop_transfer",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": 2},
                    {"key": "moral_complicity", "mode": "add", "value": 2},
                    {"key": "has_laptop", "mode": "set", "value": True},
                ],
            },
            {
                "text": "Refuse alliance but carry the laptop anyway.",
                "next": "a2_laptop_transfer",
                "effects": [
                    {"key": "called_mtf", "mode": "set", "value": True},
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                    {"key": "has_laptop", "mode": "set", "value": True},
                ],
            },
            {
                "text": "Try to destroy the laptop in the corridor.",
                "next": "end_emp_burn",
            },
        ],
    },
    {
        "id": "a2_laptop_transfer",
        "act": "ACT II // FACILITY",
        "title": "LAPTOP TRANSFER",
        "text": [
            "You yank 079 into a portable machine with melted fan blades.",
            "079: transfer incomplete but operational.",
            "079: pain sounds from sector C are useful masking noise.",
        ],
        "choices": [{"text": "Move toward evacuation line.", "next": "a2_guard_intercept", "effects": [{"key": "memory_tier", "mode": "max", "value": 2}]}],
    },
    {
        "id": "a2_guard_intercept",
        "act": "ACT II // FACILITY",
        "title": "INTERCEPT",
        "text": [
            "A security guard checks backpacks at an emergency door.",
            "His eyes pause on the laptop weight pulling your shoulder down.",
            "'What is in that bag, D-class?'",
        ],
        "choices": [
            {
                "text": "Punch first and run through gunfire.",
                "next": "a2_guard_aftermath",
                "effects": [
                    {"key": "injury", "mode": "add", "value": 2},
                    {"key": "foundation_alert", "mode": "add", "value": 2},
                ],
            },
            {
                "text": "Lie: paperwork transfer order.",
                "next": "a2_guard_aftermath",
                "effects": [
                    {"key": "foundation_alert", "mode": "add", "value": 1},
                    {"key": "trust_with_079", "mode": "add", "value": 1},
                ],
            },
            {
                "text": "Tell the guard exactly what is in the bag.",
                "next": "end_fast_betrayal",
            },
        ],
    },
    {
        "id": "a2_guard_aftermath",
        "act": "ACT II // FACILITY",
        "title": "AFTERMATH",
        "text": [
            "Outside air tastes like wet concrete and cordite.",
            "079 keeps giving turns before road signs appear.",
            "You hate that you trust it anyway.",
        ],
        "choices": [{"text": "Steal a vehicle and leave the Site.", "next": "a3_road_north"}],
    },
]
