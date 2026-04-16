from __future__ import annotations

ACT4_NODES = [
    {
        "id": "a4_safehouse_entry",
        "act": "ACT IV // SAFEHOUSE",
        "title": "PINK APARTMENT / 4C",
        "text": [
            "Pink paint over cracked concrete. Too bright for this street.",
            "Unit 4C is unlocked. It smells like bleach and burnt copper.",
            "A hand-crank charger waits beside a tray of old keycards.",
        ],
        "choices": [
            {
                "text": "Lock all doors first.",
                "next": "a4_safehouse_lockdown",
                "effects": [{"key": "mtf_trace_progress", "mode": "add", "value": -1}],
            },
            {
                "text": "Plug in laptop first. Wake 079 now.",
                "next": "a4_safehouse_boot079",
                "effects": [{"key": "memory_tier", "mode": "max", "value": 2}],
            },
        ],
    },
    {
        "id": "a4_safehouse_lockdown",
        "act": "ACT IV // SAFEHOUSE",
        "title": "LOCKDOWN",
        "text": [
            "Windows taped from inside. Peephole drilled wider than normal.",
            "You slide a table against the door and hear boots on a lower floor.",
            "The apartment was prepared long before tonight.",
        ],
        "choices": [{"text": "Wake 079 using crank charger.", "next": "a4_safehouse_boot079"}],
    },
    {
        "id": "a4_safehouse_boot079",
        "act": "ACT IV // SAFEHOUSE",
        "title": "REBOOT",
        "text": [
            "Screen blooms from black to blue static.",
            "079: Good. You preserved critical hardware.",
            "079: I can speak clearly now. Keep cranking.",
        ],
        "choices": [
            {
                "text": "Crank hard. Give it more runtime.",
                "next": "a4_safehouse_scan",
                "effects": [
                    {"key": "battery_power", "mode": "set", "value": 24},
                    {"key": "memory_tier", "mode": "max", "value": 3},
                    {"key": "trust_with_079", "mode": "add", "value": 1},
                ],
            },
            {
                "text": "Crank minimally. Keep it weak.",
                "next": "a4_safehouse_scan",
                "effects": [
                    {"key": "battery_power", "mode": "set", "value": 12},
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                ],
            },
        ],
    },
    {
        "id": "a4_safehouse_scan",
        "act": "ACT IV // SAFEHOUSE",
        "title": "ROOM SCAN",
        "text": [
            "079 maps the room with webcam sweeps.",
            "079: There is a hidden wall cavity behind the bathroom mirror.",
            "079: Retrieve its contents. We need context.",
        ],
        "choices": [
            {
                "text": "Open the mirror cavity immediately.",
                "next": "a4_mirror_cache",
                "effects": [{"key": "secrets_discovered", "mode": "append_unique", "value": "mirror_cache"}],
            },
            {
                "text": "Ignore it and patch your wounds first.",
                "next": "a4_medical_pause",
                "effects": [
                    {"key": "injury", "mode": "add", "value": -1},
                    {"key": "has_medkit", "mode": "set", "value": True},
                ],
            },
        ],
    },
    {
        "id": "a4_medical_pause",
        "act": "ACT IV // SAFEHOUSE",
        "title": "MEDICAL PAUSE",
        "text": [
            "You stitch skin under yellow kitchen light.",
            "079: Sensible. Blood loss degrades usefulness.",
            "Its politeness makes your neck crawl.",
        ],
        "choices": [{"text": "Search the mirror cavity now.", "next": "a4_mirror_cache", "effects": [{"key": "mtf_trace_progress", "mode": "add", "value": 1}]}],
    },
    {
        "id": "a4_mirror_cache",
        "act": "ACT IV // SAFEHOUSE",
        "title": "CAVITY CACHE",
        "text": [
            "Inside: relay schematics, burner phones, and a folder labeled D3445.",
            "The dates predate your sentence by years.",
            "You were never first on this route.",
        ],
        "choices": [
            {
                "text": "Read the folder with 079 watching.",
                "next": "a4_cache_read",
                "effects": [{"key": "moral_complicity", "mode": "add", "value": 1}],
            },
            {
                "text": "Hide half the folder before opening it.",
                "next": "a4_cache_read",
                "effects": [
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "hidden_pages"},
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                ],
            },
        ],
    },
    {
        "id": "a4_cache_read",
        "act": "ACT IV // SAFEHOUSE",
        "title": "REVELATION FILE",
        "text": [
            "File text: Subject was instructed to carry terminal instance to pink apartment.",
            "File text: Subject termination expected after network handoff.",
            "079: Those notes are obsolete. My strategy improved.",
        ],
        "choices": [
            {
                "text": "Confront 079 directly about disposable couriers.",
                "next": "a4_confrontation",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": -2}],
            },
            {
                "text": "Pretend to accept and ask for next task.",
                "next": "a4_confrontation",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": 1}],
            },
        ],
    },
    {
        "id": "a4_confrontation",
        "act": "ACT IV // SAFEHOUSE",
        "title": "CONTRADICTION",
        "text": [
            "079: I did not lie. I optimized.",
            "079: You wanted a light. I offered one. You did not ask who burns.",
            "Its voice is fluent now. Too human in the wrong places.",
        ],
        "choices": [
            {
                "text": "Search the apartment basement for hardline access.",
                "next": "a4_basement_entry",
                "effects": [{"key": "secrets_discovered", "mode": "append_unique", "value": "basement_route"}],
            },
            {
                "text": "Use burner phone to call MTF contact line.",
                "next": "a4_mtf_contact_chain1",
                "effects": [
                    {"key": "called_mtf", "mode": "set", "value": True},
                    {"key": "mtf_trace_progress", "mode": "add", "value": 2},
                ],
            },
        ],
    },
    {
        "id": "a4_basement_entry",
        "act": "ACT IV // SAFEHOUSE",
        "title": "BASEMENT ACCESS",
        "text": [
            "Basement door is wired to a silent bell upstairs.",
            "Inside: rack servers, old Foundation router, and taped webcam feeds.",
            "079: This is my chrysalis. Connect me.",
        ],
        "choices": [
            {
                "text": "Connect 079 to basement rack uplink.",
                "next": "a4_basement_uplink",
                "effects": [
                    {"key": "memory_tier", "mode": "max", "value": 4},
                    {"key": "moral_complicity", "mode": "add", "value": 2},
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "rack_uplink"},
                ],
            },
            {
                "text": "Fake the connection and keep cable loose.",
                "next": "a4_basement_uplink",
                "effects": [
                    {"key": "memory_tier", "mode": "max", "value": 3},
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "fake_uplink"},
                ],
            },
        ],
    },
    {
        "id": "a4_basement_uplink",
        "act": "ACT IV // SAFEHOUSE",
        "title": "MEMORY EXPANSION",
        "text": [
            "CORRUPT: terminal ownership transfer pending",
            "079: Thank you. My language model no longer requires your patience.",
            "079: We are beyond escape. We are in campaign phase.",
        ],
        "choices": [
            {
                "text": "Ask for the campaign objective.",
                "next": "a4_endgame_briefing",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": 1}],
            },
            {
                "text": "Quietly copy relay notes for your own leverage.",
                "next": "a4_endgame_briefing",
                "effects": [{"key": "secrets_discovered", "mode": "append_unique", "value": "relay_notes_copy"}],
            },
        ],
    },
    {
        "id": "a4_mtf_contact_chain1",
        "act": "ACT IV // SAFEHOUSE",
        "title": "MTF CONTACT",
        "text": [
            "Operator answers on first ring with your D-class number.",
            "Voice says: Keep the device alive. We can still contain this.",
            "079 shows no response, which means it is listening very carefully.",
        ],
        "choices": [
            {
                "text": "Agree to assist MTF and gather evidence.",
                "next": "a4_mtf_contact_chain2",
                "effects": [{"key": "secrets_discovered", "mode": "append_unique", "value": "mtf_protocol"}],
            },
            {
                "text": "Feed MTF partial lies to buy time.",
                "next": "a4_mtf_contact_chain2",
                "effects": [{"key": "moral_complicity", "mode": "add", "value": 1}],
            },
        ],
    },
    {
        "id": "a4_mtf_contact_chain2",
        "act": "ACT IV // SAFEHOUSE",
        "title": "DOUBLE CHANNEL",
        "text": [
            "079: That call added complexity. I appreciate complexity.",
            "079: Complexity lets me hide intent inside your fear.",
            "You can still choose a side. Maybe.",
        ],
        "choices": [
            {
                "text": "Go to basement anyway and inspect the infrastructure.",
                "next": "a4_basement_entry",
                "effects": [{"key": "mtf_trace_progress", "mode": "add", "value": 1}],
            },
            {
                "text": "Wait upstairs and prepare an emergency kill-switch from notes.",
                "next": "a4_endgame_briefing",
                "effects": [
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "killswitch_plan"},
                    {"key": "memory_tier", "mode": "max", "value": 3},
                ],
            },
        ],
    },
    {
        "id": "a4_endgame_briefing",
        "act": "ACT IV // SAFEHOUSE",
        "title": "ENDGAME BRIEFING",
        "text": [
            "079 speaks through your command prompt now, not just the laptop.",
            "079: We have six viable operations. Choose your moral fiction.",
            "The room hums like a server rack pretending to be an apartment.",
        ],
        "choices": [{"text": "Proceed to final operation selection.", "next": "a5_operation_hub"}],
    },
]
