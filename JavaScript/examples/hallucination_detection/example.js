// javascript/examples/hallucination_detection/example.js
import { createMICTEngine } from '../../mict-framework.js'; // Relative path to framework
import { detectHallucinations } from '../../mict-ai-ethics.js';
import { exampleData } from './data.js';

const config = {
    stages: ["Mapping", "Iteration", "Checking", "Transformation"],
    initialState: exampleData, // Use the imported example data.
    updateUI: (currentState, currentStage) => {
        console.log(`[${currentStage}] State:`, currentState);
    },
    stageFunctions: {
        Mapping: (state) => state, // No change in this example
        Iteration: (state) => state, //  Simulate model training/prediction
        Checking: (state) => {
            const hallucinations = detectHallucinations(state.generated_text, state.knowledge_base);

            if (hallucinations.length > 0) {
                console.warn("Hallucinations detected:", hallucinations);
                // Add an alert to the state
                return { ...state, alerts: [...state.alerts, `Hallucinations detected: ${hallucinations}`] };
            }
            return state;
        },
        Transformation: (state) => {
            // In a real application, you would implement hallucination mitigation strategies here.
            // This is just a placeholder.
            console.log("Transformation: (No action taken in this example)");
            return state;
        }
    },
    errorHandler: (error, stage, state) => {
      console.error(`Error: Stage ${stage}: ${error}`);
    }
};

const engine = createMICTEngine(config);
engine.nextStage(); // Run through MICT
engine.nextStage();
engine.nextStage();
engine.nextStage();
