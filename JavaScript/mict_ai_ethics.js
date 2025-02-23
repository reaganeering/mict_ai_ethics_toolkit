// javascript/mict-ai-ethics.js

/**
 * Calculates the disparate impact ratio for a binary classification model.
 * @param {number[]} predictions - Array of predicted labels (0 or 1).
 * @param {number[]} labels - Array of true labels (0 or 1).
 * @param {number[]} sensitiveAttribute - Array indicating group membership (0 or 1).
 * @returns {number|null} The disparate impact ratio, or null if undefined.
 */
function calculateDisparateImpact(predictions, labels, sensitiveAttribute) {
    if (predictions.length !== labels.length || predictions.length !== sensitiveAttribute.length) {
        return null; // Or throw an error
    }

    const group0PredPositive = predictions.filter((p, i) => sensitiveAttribute[i] === 0 && p === 1).length;
    const group0Total = sensitiveAttribute.filter(a => a === 0).length;
    const group1PredPositive = predictions.filter((p, i) => sensitiveAttribute[i] === 1 && p === 1).length;
    const group1Total = sensitiveAttribute.filter(a => a === 1).length;

    if (group0Total === 0 || group1Total === 0) {
        return null; // Avoid division by zero
    }

    const group0Rate = group0PredPositive / group0Total;
    const group1Rate = group1PredPositive / group1Total;

    if (group0Rate === 0) {
        return null; // Avoid division by zero
    }

    return group1Rate / group0Rate;
}

/**
 * Simple hallucination detection based on string matching against a knowledge base.
 * @param {string} text - The generated text.
 * @param {string[]} knowledgeBase - An array of known facts.
 * @returns {string[]} An array of potentially hallucinated statements.
 */
function detectHallucinations(text, knowledgeBase) {
  const sentences = text.split(/(?<=[.!?])\s+/); // Split into sentences.
  const hallucinations = [];

  for (const sentence of sentences) {
    let found = false;
    for (const fact of knowledgeBase) {
      if (sentence.toLowerCase().includes(fact.toLowerCase())) {
        found = true;
        break;
      }
    }
    if (!found) {
      hallucinations.push(sentence);
    }
  }
  return hallucinations;
}

// --- Example Usage (within a MICT Cycle) ---
// This would typically be in an example file, NOT in mict-ai-ethics.js itself

// import { calculateDisparateImpact, detectHallucinations } from './mict-ai-ethics.js';
// import { createMICTEngine } from './mict-framework.js'; // Assuming you have a separate file

// ... (MICT cycle setup, stage functions, etc.) ...

export { calculateDisparateImpact, detectHallucinations };
