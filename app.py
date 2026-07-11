"""Starter entry point for the SentiScope feedback analyzer."""

from typing import List


def analyze_feedback(text: str) -> str:
    """Return a simple sentiment label for a feedback string."""
    lowered = text.lower()
    if any(word in lowered for word in ["love", "great", "excellent", "amazing", "happy"]):
        return "positive"
    if any(word in lowered for word in ["bad", "hate", "terrible", "angry", "frustrated"]):
        return "negative"
    return "neutral"


if __name__ == "__main__":
    sample_feedback = "The new dashboard is fast and easy to use."
    print(f"Sample feedback sentiment: {analyze_feedback(sample_feedback)}")
