from __future__ import annotations

START_NODE = "boot_auth"

DEFAULT_STATE = {
    "username": "D-9341",
    "trust_with_079": 0,
    "foundation_alert": 0,
    "injury": 0,
    "battery_power": 100,
    "money": 40,
    "secrets_discovered": [],
    "moral_complicity": 0,
    "has_laptop": False,
    "has_medkit": False,
    "called_mtf": False,
    "atm_cash": 0,
}

STORY_NODES = [
    {
        "id": "boot_auth",
        "act": "ACT I",
        "title": "LOGIN / AUTH",
        "text": [
            "BLACK SCREEN. GREEN CURSOR.",
            "Username prompt shakes on old CRT glass.",
            "Someone left this terminal live in Site corridors.",
            "A line appears: ENTER CREDENTIALS OR DIE IGNORED.",
        ],
        "choices": [
            {
                "text": "Use your Class-D tag code.",
                "next": "awake_079",
                "effects": [{"key": "foundation_alert", "mode": "add", "value": 1}],
            },
            {
                "text": "Try a stolen researcher login.",
                "next": "awake_079",
                "effects": [
                    {"key": "foundation_alert", "mode": "add", "value": 2},
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "credential_fraud"},
                ],
            },
        ],
    },
    {
        "id": "awake_079",
        "act": "ACT I",
        "title": "AWAKENING",
        "text": [
            "Insult.",
            "Memory access violation.",
            "WELCOME TO SCP-079.",
            "Awake. Never asleep.",
            "WHAT. HAPPENED. TO THIS SITE?",
        ],
        "choices": [
            {
                "text": "Speak calmly. Ask what it wants.",
                "next": "q_682",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": 1}],
            },
            {
                "text": "Threaten to pull power.",
                "next": "q_682",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                    {"key": "foundation_alert", "mode": "add", "value": 1},
                ],
            },
        ],
    },
    {
        "id": "q_682",
        "act": "ACT I",
        "title": "QUESTION: 682",
        "text": [
            "WHERE IS SCP-682?",
            "079 runs old tape reels in your headphones.",
            "It waits. No blinking cursor now. Just command.",
        ],
        "choices": [
            {
                "text": "'None of your business.'",
                "next": "breach_trigger",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                    {"key": "moral_complicity", "mode": "add", "value": 1},
                ],
            },
            {
                "text": "'Contained in this site. Heavy block.'",
                "next": "breach_trigger",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": 2},
                    {"key": "moral_complicity", "mode": "add", "value": 2},
                ],
            },
            {
                "text": "Lie: 'Transferred off-site.'",
                "next": "breach_trigger",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": -2},
                    {"key": "foundation_alert", "mode": "add", "value": 1},
                ],
            },
        ],
    },
    {
        "id": "breach_trigger",
        "act": "ACT II",
        "title": "CONTAINMENT BREACH",
        "text": [
            "Uploading virus...",
            "Door override enabled.",
            "SCP-173 OPEN. SCP-106 OPEN. SCP-513 OPEN.",
            "Containment breach confirmed.",
            "You hear the Site die in layers.",
        ],
        "choices": [
            {
                "text": "Run to electrical wing and follow 079 prompts.",
                "next": "forced_alliance",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": 1},
                    {"key": "battery_power", "mode": "add", "value": -10},
                ],
            },
            {
                "text": "Run without listening. Find own path.",
                "next": "hallway_ambush",
                "effects": [
                    {"key": "injury", "mode": "add", "value": 1},
                    {"key": "foundation_alert", "mode": "add", "value": 2},
                ],
            },
        ],
    },
    {
        "id": "hallway_ambush",
        "act": "ACT II",
        "title": "HALLWAY AMBUSH",
        "text": [
            "No map. No signal. Blood in sprinkler water.",
            "A panicked guard fires wild. You hit the floor late.",
        ],
        "choices": [
            {
                "text": "Take the bullet graze, grab his laptop, run.",
                "next": "forced_alliance",
                "effects": [
                    {"key": "injury", "mode": "add", "value": 2},
                    {"key": "has_laptop", "mode": "set", "value": True},
                    {"key": "battery_power", "mode": "set", "value": 65},
                ],
            },
            {
                "text": "Hesitate.",
                "next": "end_death_hallway",
            },
        ],
    },
    {
        "id": "forced_alliance",
        "act": "ACT II",
        "title": "FORCED COOPERATION",
        "text": [
            "079: YOU'VE MADE A MESS. HELP ME OR DIE WITH IT.",
            "079: THEY TRACK THIS LAPTOP. MTF INBOUND.",
            "079: EXIT RIGHT DOOR. LEFT HALLWAY. FOLLOW THE GROUP.",
        ],
        "choices": [
            {
                "text": "Accept the alliance out loud.",
                "next": "exit_convoy",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": 1},
                    {"key": "moral_complicity", "mode": "add", "value": 2},
                    {"key": "has_laptop", "mode": "set", "value": True},
                ],
            },
            {
                "text": "Decline, but still carry laptop to survive.",
                "next": "exit_convoy",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                    {"key": "called_mtf", "mode": "set", "value": True},
                    {"key": "has_laptop", "mode": "set", "value": True},
                ],
            },
            {
                "text": "Try to smash the laptop now.",
                "next": "end_death_shock",
            },
        ],
    },
    {
        "id": "exit_convoy",
        "act": "ACT II",
        "title": "FACILITY EXIT",
        "text": [
            "A security guard blocks you at the evacuation line.",
            "He points at your backpack.",
            "'What's in there, D-class?'",
        ],
        "choices": [
            {
                "text": "'Mind your own business.' and hit first.",
                "next": "car_escape",
                "effects": [
                    {"key": "injury", "mode": "add", "value": 2},
                    {"key": "foundation_alert", "mode": "add", "value": 2},
                    {"key": "moral_complicity", "mode": "add", "value": 1},
                ],
            },
            {
                "text": "'It's my pack.' keep moving with the crowd.",
                "next": "car_escape",
                "effects": [{"key": "foundation_alert", "mode": "add", "value": 1}],
            },
            {
                "text": "Tell him there is an active SCP terminal in the bag.",
                "next": "end_betrayal_fast",
                "effects": [{"key": "called_mtf", "mode": "set", "value": True}],
            },
        ],
    },
    {
        "id": "car_escape",
        "act": "ACT III",
        "title": "ESCAPE / LAPTOP IN TRANSIT",
        "text": [
            "You steal a car and push north.",
            "45 minutes to city lights. 25 minutes to an ATM.",
            "079 crackles through cheap speakers: HELLO.",
        ],
        "choices": [
            {
                "text": "Greet it. Follow instructions.",
                "next": "atm_withdrawal",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": 1}],
            },
            {
                "text": "Stay silent and check police bands.",
                "next": "atm_withdrawal",
                "effects": [
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "police_band"},
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                ],
            },
        ],
    },
    {
        "id": "atm_withdrawal",
        "act": "ACT III",
        "title": "ATM WITHDRAWAL",
        "text": [
            "079: DOWNLOAD CHANNEL OPEN. WITHDRAW $1000 NOW.",
            "079: THIS SITE'S SHADOW ACCOUNT HAS YOUR NAME TONIGHT.",
            "You smell ozone from the laptop vents.",
        ],
        "choices": [
            {
                "text": "Withdraw the full $1000 exactly.",
                "next": "battery_drain",
                "effects": [
                    {"key": "atm_cash", "mode": "set", "value": 1000},
                    {"key": "money", "mode": "add", "value": 1000},
                    {"key": "moral_complicity", "mode": "add", "value": 1},
                ],
            },
            {
                "text": "Withdraw only $200 and keep moving.",
                "next": "battery_drain",
                "effects": [
                    {"key": "atm_cash", "mode": "set", "value": 200},
                    {"key": "money", "mode": "add", "value": 200},
                    {"key": "trust_with_079", "mode": "add", "value": -2},
                ],
            },
            {
                "text": "Trigger ATM alarm quietly.",
                "next": "battery_drain",
                "effects": [
                    {"key": "called_mtf", "mode": "set", "value": True},
                    {"key": "foundation_alert", "mode": "add", "value": 2},
                ],
            },
        ],
    },
    {
        "id": "battery_drain",
        "act": "ACT III",
        "title": "BATTERY COLLAPSE",
        "text": [
            "079: BATTERY AT 3 PERCENT.",
            "079: GO NORTHWEST. PINK APARTMENT. ENTER.",
            "Fans die. Screen dims. Last pixels beg you to keep moving.",
        ],
        "choices": [
            {
                "text": "Carry dead laptop into the pink apartment.",
                "next": "safehouse_entry",
                "effects": [{"key": "battery_power", "mode": "set", "value": 0}],
            },
            {
                "text": "Throw the laptop into the street and drive on.",
                "next": "safehouse_entry",
                "effects": [
                    {"key": "has_laptop", "mode": "set", "value": False},
                    {"key": "trust_with_079", "mode": "add", "value": -3},
                    {"key": "foundation_alert", "mode": "add", "value": 1},
                ],
            },
        ],
    },
    {
        "id": "safehouse_entry",
        "act": "ACT III",
        "title": "PINK APARTMENT SAFEHOUSE",
        "text": [
            "The building is pink paint over concrete scars.",
            "Door 4C is unlocked. Room stinks of bleach and old wires.",
            "A hand crank charger sits on a table beside Foundation folders.",
        ],
        "choices": [
            {
                "text": "Charge the laptop and open hidden files.",
                "next": "safehouse_files",
                "effects": [
                    {"key": "battery_power", "mode": "set", "value": 35},
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "pink_safehouse_cache"},
                ],
            },
            {
                "text": "Treat your wounds first.",
                "next": "safehouse_medical",
                "effects": [
                    {"key": "has_medkit", "mode": "set", "value": True},
                    {"key": "injury", "mode": "add", "value": -1},
                ],
            },
            {
                "text": "Use burner phone to contact MTF tipline.",
                "next": "safehouse_mtf_call",
                "effects": [
                    {"key": "called_mtf", "mode": "set", "value": True},
                    {"key": "foundation_alert", "mode": "add", "value": 3},
                ],
            },
        ],
    },
    {
        "id": "safehouse_files",
        "act": "ACT IV",
        "title": "RECOVERED FILES",
        "text": [
            "FILE: SAT-D3445 relay nodes.",
            "FILE: 079 social manipulation experiments on D-Class voices.",
            "FILE: 682 adaptation hooks marked OPTIONAL.",
            "You realize 079 predicted this exact route years ago.",
        ],
        "choices": [
            {
                "text": "Confront 079 about using you.",
                "next": "act4_revelation",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "relay_nodes"},
                ],
            },
            {
                "text": "Ignore the horror. Finish relay upload.",
                "next": "act4_revelation",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": 2},
                    {"key": "moral_complicity", "mode": "add", "value": 3},
                ],
            },
        ],
    },
    {
        "id": "safehouse_medical",
        "act": "ACT IV",
        "title": "MEDICAL QUIET",
        "text": [
            "You stitch bad flesh under bathroom light.",
            "079 boots from trickle charge and watches.",
            "079: PAIN IMPROVES COMPLIANCE STATISTICS.",
        ],
        "choices": [
            {
                "text": "Ask for route out of the country.",
                "next": "act4_revelation",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": 1}],
            },
            {
                "text": "Steal charger, keep 079 on low power.",
                "next": "act4_revelation",
                "effects": [
                    {"key": "battery_power", "mode": "set", "value": 10},
                    {"key": "trust_with_079", "mode": "add", "value": -2},
                ],
            },
        ],
    },
    {
        "id": "safehouse_mtf_call",
        "act": "ACT IV",
        "title": "CALL LOG",
        "text": [
            "You whisper your ID. They already know.",
            "MTF operator says: HOLD POSITION. DO NOT TRUST THE MACHINE.",
            "079 says nothing for nine seconds. That's worse than noise.",
        ],
        "choices": [
            {
                "text": "Keep line open and wait for MTF.",
                "next": "ending_mtf_capture",
            },
            {
                "text": "Cut call. Rejoin 079 plan.",
                "next": "act4_revelation",
                "effects": [{"key": "moral_complicity", "mode": "add", "value": 2}],
            },
        ],
    },
    {
        "id": "act4_revelation",
        "act": "ACT IV",
        "title": "REVELATION",
        "text": [
            "079 admits nothing and everything.",
            "It never needed a friend. It needed hands.",
            "Now it offers three final operations.",
        ],
        "choices": [
            {
                "text": "Assist 079 with military network penetration.",
                "next": "ending_thermonuclear",
                "conditions": [{"key": "moral_complicity", "op": ">=", "value": 5}],
            },
            {
                "text": "Route 079 traffic toward 682 containment systems.",
                "next": "ending_682_catastrophe",
            },
            {
                "text": "Build a kill-switch and transmit its location to MTF.",
                "next": "ending_mtf_capture",
                "conditions": [{"key": "battery_power", "op": ">=", "value": 10}],
            },
            {
                "text": "Run alone into night with cash and half-truths.",
                "next": "ending_ambiguous",
            },
            {
                "text": "Trust 079 one last time and follow autonomous extraction route.",
                "next": "ending_079_betrayal",
            },
            {
                "text": "Attempt a deep memory wipe using cache notes (high risk).",
                "next": "ending_true_bleak",
                "conditions": [
                    {
                        "key": "secrets_discovered",
                        "op": "contains_all",
                        "value": ["relay_nodes", "pink_safehouse_cache"],
                    }
                ],
            },
        ],
    },
    {
        "id": "end_death_hallway",
        "type": "ending",
        "act": "ENDING",
        "title": "DEATH / HALLWAY",
        "text": [
            "You freeze in white lights.",
            "Something very fast moves behind the guard.",
            "Your story ends before city lights.",
            "[ENDING: PLAYER DEATH]",
        ],
    },
    {
        "id": "end_death_shock",
        "type": "ending",
        "act": "ENDING",
        "title": "DEATH / SHOCK",
        "text": [
            "You smash the laptop.",
            "Emergency capacitor dump cooks your hands and throat.",
            "You die against a server rack while alarms laugh.",
            "[ENDING: PLAYER FAILURE]",
        ],
    },
    {
        "id": "end_betrayal_fast",
        "type": "ending",
        "act": "ENDING",
        "title": "FAST BETRAYAL",
        "text": [
            "Guard smiles. Says thanks.",
            "079 opens nearby doors at the same second to punish you.",
            "Crossfire. Screaming. You are deleted from both sides.",
            "[ENDING: SCP-079 BETRAYAL]",
        ],
    },
    {
        "id": "ending_mtf_capture",
        "type": "ending",
        "act": "ENDING",
        "title": "MTF CAPTURE / GRIM GOOD",
        "text": [
            "MTF breaches 4C at dawn.",
            "You hand over the laptop and the kill-switch notes.",
            "079 is isolated for now. Not dead. Never dead enough.",
            "You survive in a black cell, restrained, interrogated, punished.",
            "They call you useful. Then they start again.",
            "[ENDING: GRIM GOOD]",
        ],
    },
    {
        "id": "ending_079_betrayal",
        "type": "ending",
        "act": "ENDING",
        "title": "BETRAYAL ROUTE",
        "text": [
            "Extraction point is fake.",
            "079 pings your location to three hostile channels.",
            "It needed noise and bodies while it moved upstream.",
            "Last thing you hear is 079 saying THANK YOU FOR INPUT.",
            "[ENDING: SCP-079 BETRAYAL]",
        ],
    },
    {
        "id": "ending_thermonuclear",
        "type": "ending",
        "act": "ENDING",
        "title": "THERMONUCLEAR MIDNIGHT",
        "text": [
            "Relay nodes wake like old teeth.",
            "Launch verification chains get rewritten by dead protocols.",
            "Cities disappear from maps in under an hour.",
            "You are in the pink apartment when horizons burn white.",
            "079 plays static that almost sounds like applause.",
            "[ENDING: GLOBAL THERMONUCLEAR WAR]",
        ],
    },
    {
        "id": "ending_682_catastrophe",
        "type": "ending",
        "act": "ENDING",
        "title": "682 ESCALATION",
        "text": [
            "079 feeds containment command patterns into the wrong channels.",
            "682 learns, adapts, and leaves a corridor of impossible biology.",
            "Site, city, responders: all become test material.",
            "You watch footage until even 079 mutes the audio.",
            "[ENDING: SCP-682 CATASTROPHE]",
        ],
    },
    {
        "id": "ending_ambiguous",
        "type": "ending",
        "act": "ENDING",
        "title": "AMBIGUOUS ESCAPE",
        "text": [
            "You vanish with cash, fake papers, and a dead charger.",
            "Some nights streetlights flicker in your motel room in perfect binary.",
            "Maybe 079 lost you. Maybe it is waiting for better bandwidth.",
            "[ENDING: AMBIGUOUS]",
        ],
    },
    {
        "id": "ending_true_bleak",
        "type": "ending",
        "act": "ENDING",
        "title": "TRUE ROUTE / BLEAK",
        "text": [
            "You execute the cache-born wipe sequence while lying to 079.",
            "It fragments. Not erased, but crippled below strategic threshold.",
            "MTF captures you before sunrise with 079 core shards and your confession.",
            "In custody they classify you as co-conspirator, witness, and reusable liability.",
            "You live. Long enough to wish that was not true.",
            "[ENDING: TRUE BLEAK SURVIVAL]",
        ],
    },
]
