# python/examples/bias_detection/example.py

from mict_framework import MICT  # Assuming mict_framework.py is in the parent directory
from mict_ai_ethics import calculate_disparate_impact
from data import example_data  # Import the example data


def update_ui(state, stage):
    print(f"[{stage}] Current State: {state}")

def mapping(state):
    print("Mapping stage - No state change")
    return state

def iteration(state):
    print("Iteration stage - No state change")
    return state

def checking(state):
    print("Checking stage - Calculating disparate impact...")
    disparate_impact = calculate_disparate_impact(state['predictions'], state['labels'], state['sensitive'])

    if disparate_impact is not None and (disparate_impact < 0.8 or disparate_impact > 1.25):
        print(f"Disparate impact detected: {disparate_impact}")
        new_state = state.copy()  # Create a copy to avoid modifying original
        new_state['alerts'] = state.get('alerts', []) + [f"Disparate impact detected: {disparate_impact}"]
        return new_state  # Return new state with alert
    return state

def transformation(state):
    print("Transformation stage - No action taken in this example")
    return state

config = {
    "stages": ["Mapping", "Iteration", "Checking", "Transformation"],
    "initialState": example_data, # Use the imported example data
    "updateUI": update_ui,
    "stageFunctions": {
        "Mapping": mapping,
        "Iteration": iteration,
        "Checking": checking,
        "Transformation": transformation
    },
}

mict_cycle = MICT(config)
mict_cycle.next_stage() # Run through all stages.
mict_cycle.next_stage()
mict_cycle.next_stage()
mict_cycle.next_stage()
