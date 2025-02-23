# python/examples/hallucination_detection/example.py

from mict_framework import MICT
from mict_ai_ethics import detect_hallucinations
from data import example_data  # Import the example data


def update_ui(state, stage):
    print(f"[{stage}] Current State: {state}")

def mapping(state):
    print("Mapping stage - No state change")
    return state

def iteration(state):
    print("Iteration stage - No state change")  # In a real application, you'd generate text here
    return state

def checking(state):
    print("Checking stage - Detecting hallucinations...")
    hallucinations = detect_hallucinations(state['generated_text'], state['knowledge_base'])

    if hallucinations:
        print("Potential hallucinations detected:", hallucinations)
        new_state = state.copy() # Create mutable copy
        new_state['alerts'] = state.get('alerts', []) + [f"Potential hallucination: {h}" for h in hallucinations]
        return new_state
    return state

def transformation(state):
    print("Transformation stage - No action taken in this example")
    # In a real application, you might regenerate the text or flag it for review
    return state

config = {
    "stages": ["Mapping", "Iteration", "Checking", "Transformation"],
    "initialState": example_data, # Use imported data.
    "updateUI": update_ui,
    "stageFunctions": {
        "Mapping": mapping,
        "Iteration": iteration,
        "Checking": checking,
        "Transformation": transformation
    },
}

mict_cycle = MICT(config)
mict_cycle.next_stage() # Run all stages
mict_cycle.next_stage()
mict_cycle.next_stage()
mict_cycle.next_stage()
