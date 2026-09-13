import sys
import argparse
import json
from .evaluator import TokenEvaluator

def main():
    parser = argparse.ArgumentParser(description="Traum Tokenizer Evaluation CLI")
    parser.add_argument("text", nargs="?", default="", help="Text to evaluate token metrics for")
    parser.add_argument("--json", action="store_true", help="Output metrics in JSON format")
    args = parser.parse_args()

    input_text = args.text
    if not input_text:
        if not sys.stdin.isatty():
            input_text = sys.stdin.read().strip()
        else:
            input_text = "الذكاء الاصطناعي وتطبيقات معالجة اللغة الطبيعية في العالم العربي"

    res = TokenEvaluator.evaluate_text(input_text)

    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print("\n📊 Traum Tokenizer Efficiency Report:")
        print(f"  • Words: {res['word_count']}")
        print(f"  • Characters: {res['character_count']}")
        print(f"  • Generic Tokenizer Tokens: {res['generic_tokenizer_estimated_tokens']}")
        print(f"  • Traum Tokenizer Tokens:   {res['traum_tokenizer_estimated_tokens']}")
        print(f"  • Token Savings:            {res['estimated_token_savings_percent']}%")
        print(f"  • Fertility Ratio:          {res['traum_fertility_ratio']} tokens/word\n")

if __name__ == "__main__":
    main()
