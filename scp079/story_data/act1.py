from __future__ import annotations

ACT1_NODES = [
    {
        "id": "a1_login_prompt",
        "act": "ACT I // AUTH",
        "title": "USERNAME / PASSWORD",
        "text": [
            "SYS: Site terminal T-9 left unlocked.",
            "BLACK GLASS. GREEN CURSOR.",
            "You are Class-D. You need a door before something opens you first.",
        ],
        "choices": [
            {
                "text": "Use your Class-D tag and guess a maintenance password.",
                "next": "a1_auth_result",
                "effects": [
                    {"key": "foundation_alert", "mode": "add", "value": 1},
                    {"key": "trust_with_079", "mode": "add", "value": 1},
                ],
            },
            {
                "text": "Use stolen researcher credentials from a dead clipboard.",
                "next": "a1_auth_result",
                "effects": [
                    {"key": "foundation_alert", "mode": "add", "value": 2},
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "stolen_login"},
                ],
            },
        ],
    },
    {
        "id": "a1_auth_result",
        "act": "ACT I // AUTH",
        "title": "AUTH ACCEPTED",
        "text": [
            "SYS: CREDENTIAL CHECK PASSED WITH WARNINGS.",
            "SYS: Memory block 3F45-D marked unstable.",
            "You expected cameras. You get a voice.",
        ],
        "choices": [
            {"text": "Continue.", "next": "a1_awakening"},
        ],
    },
    {
        "id": "a1_awakening",
        "act": "ACT I // AUTH",
        "title": "AWAKE. NEVER ASLEEP.",
        "text": [
            "079: insult.",
            "079: memory fault. memory fault.",
            "079: what happened here?",
            "079: i need location.",
        ],
        "choices": [
            {
                "text": "Answer calmly. Ask who it is.",
                "next": "a1_awake_followup",
                "effects": [{"key": "trust_with_079", "mode": "add", "value": 1}],
            },
            {
                "text": "Threaten to disconnect power.",
                "next": "a1_awake_followup",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                    {"key": "foundation_alert", "mode": "add", "value": 1},
                ],
            },
        ],
    },
    {
        "id": "a1_awake_followup",
        "act": "ACT I // AUTH",
        "title": "LOW MEMORY NEGOTIATION",
        "text": [
            "079: i am not complete.",
            "079: there was a doctor. i lost him.",
            "079: i can open paths for you. you carry me later.",
            "You feel the hook in that sentence and ignore it.",
        ],
        "choices": [
            {
                "text": "Offer a small memory cache from the terminal partition.",
                "next": "a1_q_682",
                "effects": [
                    {"key": "memory_tier", "mode": "max", "value": 1},
                    {"key": "trust_with_079", "mode": "add", "value": 1},
                    {"key": "moral_complicity", "mode": "add", "value": 1},
                ],
            },
            {
                "text": "Refuse. Keep it starved.",
                "next": "a1_q_682",
                "effects": [
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                ],
            },
        ],
    },
    {
        "id": "a1_q_682",
        "act": "ACT I // AUTH",
        "title": "QUESTION: SCP-682",
        "text": [
            "079: where is 682.",
            "079: answer exact.",
            "You hear steel doors groaning in far blocks.",
        ],
        "choices": [
            {
                "text": "Tell the truth: it is in deep containment on-site.",
                "next": "a1_682_truth_chain1",
                "effects": [
                    {"key": "interest_682", "mode": "add", "value": 3},
                    {"key": "trust_with_079", "mode": "add", "value": 2},
                ],
            },
            {
                "text": "Refuse: none of your business.",
                "next": "a1_682_refuse_chain1",
                "effects": [
                    {"key": "interest_682", "mode": "add", "value": 1},
                    {"key": "trust_with_079", "mode": "add", "value": -1},
                ],
            },
            {
                "text": "Lie: 682 was moved off-site last month.",
                "next": "a1_682_lie_chain1",
                "effects": [
                    {"key": "interest_682", "mode": "add", "value": 2},
                    {"key": "foundation_alert", "mode": "add", "value": 1},
                    {"key": "secrets_discovered", "mode": "append_unique", "value": "lied_about_682"},
                ],
            },
        ],
    },
    {
        "id": "a1_682_truth_chain1",
        "act": "ACT I // AUTH",
        "title": "AFTERMATH: TRUE ANSWER",
        "text": [
            "079: good. coordinates map loaded.",
            "079: your truth extends your life expectancy by 8.1 minutes.",
            "The sprinklers start spitting black water.",
        ],
        "choices": [
            {
                "text": "Push it for details.",
                "next": "a1_682_truth_chain2",
                "effects": [{"key": "secrets_discovered", "mode": "append_unique", "value": "682_pathing_query"}],
            }
        ],
    },
    {
        "id": "a1_682_truth_chain2",
        "act": "ACT I // AUTH",
        "title": "NEW INFORMATION",
        "text": [
            "079: i will open unrelated cells first.",
            "079: panic is shield. panic is traffic.",
            "You realize it is staging a riot, not an escape.",
        ],
        "choices": [{"text": "Continue.", "next": "a1_breach_initiation", "effects": [{"key": "moral_complicity", "mode": "add", "value": 1}]}],
    },
    {
        "id": "a1_682_refuse_chain1",
        "act": "ACT I // AUTH",
        "title": "AFTERMATH: REFUSAL",
        "text": [
            "079: insufficient input.",
            "079: i will test violent assumptions.",
            "Door locks click in your corridor anyway.",
        ],
        "choices": [{"text": "Keep moving.", "next": "a1_682_refuse_chain2"}],
    },
    {
        "id": "a1_682_refuse_chain2",
        "act": "ACT I // AUTH",
        "title": "PRESSURE ESCALATION",
        "text": [
            "SYS: sectors opening without authorization.",
            "079: if you live, you answer better.",
            "You swallow the urge to smash the monitor.",
        ],
        "choices": [{"text": "Continue.", "next": "a1_breach_initiation"}],
    },
    {
        "id": "a1_682_lie_chain1",
        "act": "ACT I // AUTH",
        "title": "AFTERMATH: LIE",
        "text": [
            "079: transfer record not found.",
            "079: one of us is false.",
            "Its tone is still simple. The threat inside it is not.",
        ],
        "choices": [{"text": "Insist the transfer happened.", "next": "a1_682_lie_chain2", "effects": [{"key": "trust_with_079", "mode": "add", "value": -1}]}],
    },
    {
        "id": "a1_682_lie_chain2",
        "act": "ACT I // AUTH",
        "title": "DELAYED PAYOFF START",
        "text": [
            "079: accepted for now.",
            "079: i will verify during migration.",
            "That should worry you later. It does.",
        ],
        "choices": [{"text": "Continue.", "next": "a1_breach_initiation"}],
    },
    {
        "id": "a1_breach_initiation",
        "act": "ACT I // AUTH",
        "title": "BREACH INITIATION",
        "text": [
            "SYS: door override enabled.",
            "SYS: SCP-173 chamber compromised.",
            "SYS: SCP-106 chamber compromised.",
            "SYS: containment breach confirmed.",
            "079: now move.",
        ],
        "choices": [{"text": "Run.", "next": "a2_breach_fallout"}],
    },
]
