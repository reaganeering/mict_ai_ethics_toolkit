# python/examples/bias_detection/data.py

# Example data for bias detection. This is SIMULATED data for demonstration purposes.
# In a real application, you would load data from a file or database.

example_data = {
    "predictions": [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1],  # Predicted labels (0 or 1)
    "labels": [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],  # True labels (0 or 1)
    "sensitive": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Sensitive attribute (0 or 1)
    # (e.g., 0 might represent one demographic group, and 1 another)
    "alerts": []
}
