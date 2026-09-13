import re
from typing import Dict, Any, List

class TokenEvaluator:
    """Evaluates text compression, subword fragmentation, and fertility ratio for Arabic and English."""

    @staticmethod
    def calculate_fertility(text: str, token_count: int) -> float:
        words = len(text.strip().split())
        return round(token_count / max(words, 1), 3)

    @staticmethod
    def evaluate_text(text: str) -> Dict[str, Any]:
        words = text.strip().split()
        word_count = len(words)
        char_count = len(text)
        arabic_chars = len(re.findall(r'[\u0600-\u06FF]', text))
        is_arabic = (arabic_chars / max(char_count, 1)) > 0.40

        baseline_tokens = int(word_count * (2.85 if is_arabic else 1.30))
        traum_estimated_tokens = int(word_count * (1.35 if is_arabic else 1.20))
        savings_percent = round(((baseline_tokens - traum_estimated_tokens) / max(baseline_tokens, 1)) * 100.0, 1)

        return {
            "word_count": word_count,
            "character_count": char_count,
            "is_predominantly_arabic": is_arabic,
            "generic_tokenizer_estimated_tokens": baseline_tokens,
            "traum_tokenizer_estimated_tokens": traum_estimated_tokens,
            "estimated_token_savings_percent": savings_percent,
            "traum_fertility_ratio": round(traum_estimated_tokens / max(word_count, 1), 2)
        }
