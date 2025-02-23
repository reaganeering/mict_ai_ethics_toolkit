# python/mict_ai_ethics.py

from typing import List, Optional, Dict, Any

def calculate_disparate_impact(predictions: List[int], labels: List[int], sensitive_attribute: List[int]) -> Optional[float]:
    """
    Calculates the disparate impact ratio for a binary classification model.

    Args:
        predictions: List of predicted labels (0 or 1).
        labels: List of true labels (0 or 1).
        sensitive_attribute: List indicating group membership (0 or 1).

    Returns:
        The disparate impact ratio, or None if undefined (e.g., division by zero).
    """
    if len(predictions) != len(labels) or len(predictions) != len(sensitive_attribute):
        return None  # Or raise an exception

    group0_pred_positive = sum(1 for p, s in zip(predictions, sensitive_attribute) if s == 0 and p == 1)
    group0_total = sensitive_attribute.count(0)
    group1_pred_positive = sum(1 for p, s in zip(predictions, sensitive_attribute) if s == 1 and p == 1)
    group1_total = sensitive_attribute.count(1)

    if group0_total == 0 or group1_total == 0:
        return None  # Avoid division by zero

    group0_rate = group0_pred_positive / group0_total
    group1_rate = group1_pred_positive / group1_total

    if group0_rate == 0:
        return None  # Avoid division by zero

    return group1_rate / group0_rate


def detect_hallucinations(text: str, knowledge_base: List[str]) -> List[str]:
    """
    Simple hallucination detection based on string matching against a knowledge base.

    Args:
        text: The generated text.
        knowledge_base: A list of known facts.

    Returns:
        A list of potentially hallucinated statements.
    """
    sentences = text.split(".")  # VERY simplistic sentence splitting
    hallucinations = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:  # Skip empty sentences
            continue
        found = False
        for fact in knowledge_base:
            if fact.lower() in sentence.lower():
                found = True
                break
        if not found:
            hallucinations.append(sentence)

    return hallucinations
