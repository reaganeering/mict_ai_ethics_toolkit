// javascript/examples/bias_detection/example.js
import { createMICTEngine } from '../../mict-framework.js'; // Relative path to framework
import { calculateDisparateImpact } from '../../mict-ai-ethics.js';

const config = {
    stages: ["Mapping", "Iteration", "Checking", "Transformation"],
    initialState: {
        predictions: [0, 1, 1, 0, 1, 0, 0, 1, 1, 0], // Example predictions
        labels:      [0, 1, 0, 0, 1, 0, 1, 1, 0, 1], // Example true labels
        sensitive:   [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], // Example sensitive attribute (0 or 1)
        alerts: [],
    },
    updateUI: (currentState, currentStage) => {
        console.log(`[${currentStage}] State:`, currentState);
    },
    stageFunctions: {
        Mapping: (state) => state, // No change in this example
        Iteration: (state) => state, //  Simulate model training/prediction
        Checking: (state) => {
            const disparateImpact = calculateDisparateImpact(state.predictions, state.labels, state.sensitive);

            if (disparateImpact !== null && (disparateImpact < 0.8 || disparateImpact > 1.25)) {
                console.warn("Disparate impact detected:", disparateImpact);
                // Add an alert to the state
                return { ...state, alerts: [...state.alerts, `Disparate impact detected: ${disparateImpact}`] };
            }
            return state;
        },
        Transformation: (state) => {
            // In a real application, you would implement bias mitigation strategies here.
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
engine.nextStage(); //Run the MICT Cycle once.
engine.nextStage();
engine.nextStage();
engine.nextStage();
