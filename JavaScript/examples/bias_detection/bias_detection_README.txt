# Bias Detection Example

This example demonstrates how to use the `calculateDisparateImpact` function from the `mict-ai-ethics` toolkit to detect bias in a binary classification model's predictions.

## Concepts Demonstrated

*   **Disparate Impact:**  A metric for measuring bias in machine learning models.  A disparate impact ratio less than 0.8 or greater than 1.25 is often considered to indicate potential bias (the "80% rule").
*   **MICT Framework Integration:**  The example shows how to use the `calculateDisparateImpact` function within the `Checking` stage of a MICT cycle.

## How to Run

1.  Make sure you have Node.js installed.
2.  Navigate to this directory in your terminal: `cd javascript/examples/bias_detection`
3.  Run the example: `node example.js`

## Expected Output

The example will print the current MICT stage and the state to the console.  If a disparate impact is detected, it will also print a warning message.

## Data

The example data is in `data.js`. It consists of:

*   `predictions`: An array of predicted labels (0 or 1).
*   `labels`: An array of true labels (0 or 1).
*   `sensitive`: An array indicating group membership (0 or 1).

You can modify the data in `data.js` to experiment with different scenarios.

## Limitations

This is a simplified example for demonstration purposes.  In a real-world application, you would use a much larger dataset and more sophisticated bias detection techniques.
