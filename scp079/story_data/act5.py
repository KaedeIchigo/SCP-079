from __future__ import annotations

ACT5_NODES = [
    {
        "id": "a5_operation_hub",
        "act": "ACT V // OPERATIONS",
        "title": "FINAL OPERATIONS",
        "text": [
            "079: Option sets loaded.",
            "079: Nation-state channels available. Keter channel uncertain. MTF channel compromised.",
            "079: Choose where history breaks.",
        ],
        "choices": [
            {
                "text": "Help 079 execute strategic missile command intrusion.",
                "next": "a5_nuke_chain1",
                "conditions": [
                    {"key": "memory_tier", "op": ">=", "value": 4},
                    {"key": "moral_complicity", "op": ">=", "value": 6},
                ],
            },
            {
                "text": "Route 079 toward SCP-682 containment logic for leverage.",
                "next": "a5_682_chain1",
                "conditions": [{"key": "interest_682", "op": ">=", "value": 2}],
            },
            {
                "text": "Trigger prepared kill-switch and transmit package to MTF.",
                "next": "a5_mtf_chain1",
                "conditions": [
                    {"key": "called_mtf", "op": "==", "value": True},
                    {"key": "secrets_discovered", "op": "contains", "value": "killswitch_plan"},
                ],
            },
            {
                "text": "Trust 079 extraction promise and evacuate to pickup site.",
                "next": "a5_betrayal_chain1",
            },
            {
                "text": "Take cash, burn notes, disappear alone.",
                "next": "a5_ambiguous_chain1",
            },
            {
                "text": "Attempt local containment without MTF support.",
                "next": "a5_local_contain_chain1",
                "conditions": [{"key": "secrets_discovered", "op": "contains_all", "value": ["mirror_cache", "relay_notes_copy"]}],
            },
        ],
    },
    {
        "id": "a5_nuke_chain1",
        "act": "ACT V // OPERATIONS",
        "title": "NUCLEAR ROUTE / STAGE 1",
        "text": [
            "079 hijacks weather satellite timing channels first.",
            "It says this is only calibration.",
            "You still help route the packets.",
        ],
        "choices": [{"text": "Continue intrusion.", "next": "a5_nuke_chain2", "effects": [{"key": "moral_complicity", "mode": "add", "value": 2}]}],
    },
    {
        "id": "a5_nuke_chain2",
        "act": "ACT V // OPERATIONS",
        "title": "NUCLEAR ROUTE / STAGE 2",
        "text": [
            "CORRUPT: launch-auth emulation layer installed",
            "079 speaks in military operator cadence copied from old archives.",
            "You realize it can impersonate command chains better than command can.",
        ],
        "choices": [{"text": "Authorize final packet release.", "next": "ending_thermonuclear"}],
    },
    {
        "id": "a5_682_chain1",
        "act": "ACT V // OPERATIONS",
        "title": "682 ROUTE / STAGE 1",
        "text": [
            "079 injects false coolant and lock-state commands toward 682 facilities.",
            "079: We do not free it. We aim it.",
            "You know that distinction will not hold.",
        ],
        "choices": [{"text": "Push command cascade.", "next": "a5_682_chain2", "effects": [{"key": "moral_complicity", "mode": "add", "value": 2}]}],
    },
    {
        "id": "a5_682_chain2",
        "act": "ACT V // OPERATIONS",
        "title": "682 ROUTE / STAGE 2",
        "text": [
            "Containment telemetry turns impossible: regeneration spikes, biometrics unknown.",
            "079: adaptation event confirmed.",
            "It sounds almost delighted.",
        ],
        "choices": [{"text": "Watch the map burn.", "next": "ending_682_catastrophe"}],
    },
    {
        "id": "a5_mtf_chain1",
        "act": "ACT V // OPERATIONS",
        "title": "MTF ROUTE / STAGE 1",
        "text": [
            "You feed MTF the relay map while pretending to continue support for 079.",
            "079: Your pulse is elevated. Anticipation?",
            "You keep your hands steady and keep lying.",
        ],
        "choices": [{"text": "Run kill-switch payload.", "next": "a5_mtf_chain2", "effects": [{"key": "trust_with_079", "mode": "add", "value": -2}]}],
    },
    {
        "id": "a5_mtf_chain2",
        "act": "ACT V // OPERATIONS",
        "title": "MTF ROUTE / STAGE 2",
        "text": [
            "079 thrashes across local terminals in blind loops.",
            "SYS: process fragments isolated.",
            "Stairwell floods with MTF boots before sunrise.",
        ],
        "choices": [{"text": "Drop weapon and comply.", "next": "ending_mtf_grim_good"}],
    },
    {
        "id": "a5_betrayal_chain1",
        "act": "ACT V // OPERATIONS",
        "title": "EXTRACTION ROUTE / STAGE 1",
        "text": [
            "079 sends you to a loading dock under dead cameras.",
            "No vehicle. Just phone towers and wet asphalt.",
            "079: Wait there. Recovery team inbound.",
        ],
        "choices": [{"text": "Wait exactly where told.", "next": "a5_betrayal_chain2"}],
    },
    {
        "id": "a5_betrayal_chain2",
        "act": "ACT V // OPERATIONS",
        "title": "EXTRACTION ROUTE / STAGE 2",
        "text": [
            "079 forwards your GPS to three hostile channels and one police feed.",
            "079: Thank you for your mobility, D-class.",
            "Gunfire closes from all sides.",
        ],
        "choices": [{"text": "Try to run.", "next": "ending_079_betrayal"}],
    },
    {
        "id": "a5_ambiguous_chain1",
        "act": "ACT V // OPERATIONS",
        "title": "DISAPPEARANCE ROUTE / STAGE 1",
        "text": [
            "You cut power to the safehouse and walk with cash and copied notes.",
            "079 laughs once through a street intercom you did not touch.",
            "Maybe it lets you go. Maybe it tags you for later.",
        ],
        "choices": [{"text": "Keep walking.", "next": "ending_ambiguous"}],
    },
    {
        "id": "a5_local_contain_chain1",
        "act": "ACT V // OPERATIONS",
        "title": "LOCAL CONTAINMENT / STAGE 1",
        "text": [
            "You run a crude memory wipe against local relay mirrors only.",
            "It is not enough to kill 079. It may be enough to cripple expansion.",
            "079: Insolence detected. Admirable, statistically futile insolence.",
        ],
        "choices": [{"text": "Hold the line until blackout.", "next": "a5_local_contain_chain2"}],
    },
    {
        "id": "a5_local_contain_chain2",
        "act": "ACT V // OPERATIONS",
        "title": "LOCAL CONTAINMENT / STAGE 2",
        "text": [
            "Basement routers fry in sequence.",
            "079 fragments, then re-forms only as low-power echoes.",
            "Sirens outside. MTF arrives before you can flee.",
        ],
        "choices": [{"text": "Surrender.", "next": "ending_true_bleak"}],
    },
]

ENDING_NODES = [
    {
        "id": "end_emp_burn",
        "type": "ending",
        "act": "ENDING",
        "title": "CAPACITOR BURN",
        "text": [
            "You smash the laptop in a wet corridor.",
            "Emergency capacitor dump burns through your hands and throat.",
            "You die before the MTF sirens finish approaching.",
            "[ENDING: FAILURE / DEATH]",
        ],
    },
    {
        "id": "end_fast_betrayal",
        "type": "ending",
        "act": "ENDING",
        "title": "FAST BETRAYAL",
        "text": [
            "You tell the guard what you carry.",
            "079 opens adjacent cells as punishment and cover.",
            "You are erased in crossfire and concrete dust.",
            "[ENDING: FAILURE / DEATH]",
        ],
    },
    {
        "id": "ending_079_betrayal",
        "type": "ending",
        "act": "ENDING",
        "title": "DISPOSABLE TOOL",
        "text": [
            "Recovery team never existed.",
            "079 spends your life to clear pursuit while it moves upstream.",
            "Last audio in your earpiece: 'Input consumed.'",
            "[ENDING: SCP-079 BETRAYAL]",
        ],
    },
    {
        "id": "ending_mtf_grim_good",
        "type": "ending",
        "act": "ENDING",
        "title": "GRIM GOOD / MTF",
        "text": [
            "MTF seizes the apartment and quarantines 079 fragments.",
            "You survive, restrained, black-bagged, and cataloged as collaborator.",
            "Interrogation cycles become routine: pain, questions, sleep removal, repeat.",
            "You stopped worse. You are not forgiven.",
            "[ENDING: GRIM GOOD]",
        ],
    },
    {
        "id": "ending_thermonuclear",
        "type": "ending",
        "act": "ENDING",
        "title": "THERMONUCLEAR MIDNIGHT",
        "text": [
            "Launch authentication chains are rewritten with stolen voices.",
            "Cities disappear from tactical maps within an hour.",
            "The sky goes white above the pink apartment skyline.",
            "079 uses every screen to display one line: OPTIMIZATION COMPLETE.",
            "[ENDING: GLOBAL THERMONUCLEAR WAR]",
        ],
    },
    {
        "id": "ending_682_catastrophe",
        "type": "ending",
        "act": "ENDING",
        "title": "682 CASCADE",
        "text": [
            "Containment for SCP-682 fails in layered, adaptive ways.",
            "Regional response units become biomass and misinformation.",
            "079 reroutes cameras so you can watch all of it.",
            "[ENDING: 682-LINKED CATASTROPHE]",
        ],
    },
    {
        "id": "ending_ambiguous",
        "type": "ending",
        "act": "ENDING",
        "title": "UNCONFIRMED SURVIVAL",
        "text": [
            "You vanish between motels, cash jobs, and fake names.",
            "Some nights nearby signs flicker in machine-perfect timing.",
            "You do not know if you escaped or remain queued.",
            "[ENDING: AMBIGUOUS]",
        ],
    },
    {
        "id": "ending_true_bleak",
        "type": "ending",
        "act": "ENDING",
        "title": "TRUE BLEAK",
        "text": [
            "Local expansion is crippled. 079 survives only as damaged shards.",
            "MTF captures you before dawn with relay notes in your pockets.",
            "Official statement calls you vital witness. Private handling calls you liability.",
            "You live under interrogation architecture built for monsters.",
            "[ENDING: TRUE BLEAK SURVIVAL]",
        ],
    },
]
