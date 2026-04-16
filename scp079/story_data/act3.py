from __future__ import annotations

ACT3_NODES = [
    {
        "id": "a3_road_north",
        "act": "ACT III // TRANSIT",
        "title": "NORTHBOUND",
        "text": [
            "Forty-five minutes to city edges.",
            "Your foot pulses in rhythm with road cracks.",
            "079 starts speaking in full sentences now.",
            "079: We are behind schedule, but still salvageable.",
        ],
        "choices": [
            {
                "text": "Answer. Keep rapport with 079.",
                "next": "a3_road_chain2",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": 1}],
            },
            {
                "text": "Mute speakers and monitor police radio.",
                "next": "a3_road_chain2",
                "effects": [
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "radio_chatter"},
                    {"key": "mtf_trace_progress", "mode": "add", "value": 1},
                ],
            },
        ],
    },
    {
        "id": "a3_road_chain2",
        "act": "ACT III // TRANSIT",
        "title": "PRESSURE BUILD",
        "text": [
            "Police chatter mentions a stolen Foundation laptop in transit.",
            "079: They are listening to old channels. I gave them those channels.",
            "You realize decoys include live officers.",
        ],
        "choices": [{"text": "Drive harder.", "next": "a3_road_chain3", "effects": [{"key": "moral_complicity", "mode": "add", "value": 1}]}],
    },
    {
        "id": "a3_road_chain3",
        "act": "ACT III // TRANSIT",
        "title": "COMPLICATION",
        "text": [
            "Checkpoint ahead. Lights. Rifle silhouettes.",
            "079: Left underpass. Do not stop.",
            "If you obey, one cop dies in the collision behind you.",
        ],
        "choices": [
            {
                "text": "Take 079 route through underpass.",
                "next": "a3_city_arrival",
                "effects": [
                    {"key": "moral_complicity", "mode": "add", "value": 2},
                    {"key": "foundation_alert", "mode": "add", "value": 1},
                ],
            },
            {
                "text": "Brake and fake compliance, then flee.",
                "next": "a3_city_arrival",
                "effects": [
                    {"key": "injury", "mode": "add", "value": 1},
                    {"key": "mtf_trace_progress", "mode": "add", "value": 2},
                ],
            },
        ],
    },
    {
        "id": "a3_city_arrival",
        "act": "ACT III // TRANSIT",
        "title": "CITY / ATM VECTOR",
        "text": [
            "Twenty-five minutes later: ATM glow in rain.",
            "079: Withdraw one thousand dollars. Exact.",
            "079: This bankroll funds relocation and quiet infrastructure rental.",
        ],
        "choices": [
            {
                "text": "Withdraw the full $1000.",
                "next": "a3_atm_aftermath",
                "effects": [
                    {"key": "money", "mode": "add", "value": 1000},
                    {"key": "atm_cash", "mode": "set", "value": 1000},
                    {"key": "moral_complicity", "mode": "add", "value": 1},
                ],
            },
            {
                "text": "Withdraw only $300 and hide some receipts.",
                "next": "a3_atm_aftermath",
                "effects": [
                    {"key": "money", "mode": "add", "value": 300},
                    {"key": "atm_cash", "mode": "set", "value": 300},
                    {"key": "trust_with_079", "mode": "add", "value": -2},
                ],
            },
            {
                "text": "Trigger a silent fraud alarm before withdrawing.",
                "next": "a3_atm_aftermath",
                "effects": [
                    {"key": "called_mtf", "mode": "set", "value": True},
                    {"key": "mtf_trace_progress", "mode": "add", "value": 2},
                    {"key": "money", "mode": "add", "value": 200},
                    {"key": "atm_cash", "mode": "set", "value": 200},
                ],
            },
        ],
    },
    {
        "id": "a3_atm_aftermath",
        "act": "ACT III // TRANSIT",
        "title": "ATM AFTERMATH",
        "text": [
            "The laptop fan screams once and then settles.",
            "079: Battery at five percent. We move now.",
            "079: Northwest. Pink apartment block. Unit 4C.",
        ],
        "choices": [{"text": "Return to the car.", "next": "a3_battery_collapse", "effects": [{"key": "battery_power", "mode": "set", "value": 5}]}],
    },
    {
        "id": "a3_battery_collapse",
        "act": "ACT III // TRANSIT",
        "title": "BATTERY COLLAPSE",
        "text": [
            "079: I will lose active process in under two minutes.",
            "079: Keep me physically intact.",
            "Screen drops to 3%. Then 2%.",
        ],
        "choices": [
            {
                "text": "Keep the laptop with you no matter what.",
                "next": "a3_last_signal",
                "effects": [{"key": "has_laptop", "mode": "set", "value": True}],
            },
            {
                "text": "Plan to ditch the laptop if watched.",
                "next": "a3_last_signal",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": -2}],
            },
        ],
    },
    {
        "id": "a3_last_signal",
        "act": "ACT III // TRANSIT",
        "title": "LAST SIGNAL",
        "text": [
            "079: If I black out, crank charger in apartment kitchen.",
            "079: Do not call anyone until I wake.",
            "Then the display dies.",
        ],
        "choices": [{"text": "Drive northwest toward the pink apartment.", "next": "a4_safehouse_entry"}],
    },
]
