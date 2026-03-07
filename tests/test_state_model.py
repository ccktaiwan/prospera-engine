"""
Prospera Engine Architecture Test
State Model Validation
"""

VALID_STATES = [
"INITIALIZED",
"IDLE",
"PROCESSING",
"COMMITTED",
"FAILED"
]

VALID_TRANSITIONS = {
"INITIALIZED": ["IDLE"],
"IDLE": ["PROCESSING"],
"PROCESSING": ["COMMITTED", "FAILED"],
"COMMITTED": ["IDLE"],
"FAILED": ["IDLE"]
}

def test_valid_states():
for state in VALID_STATES:
assert isinstance(state, str)

def test_transition_rules():
for state, next_states in VALID_TRANSITIONS.items():
assert state in VALID_STATES
for next_state in next_states:
assert next_state in VALID_STATES

def test_invalid_transition():
assert "INITIALIZED" not in VALID_TRANSITIONS.get("COMMITTED", [])
