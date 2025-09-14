# llm_calls.py
import os
import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Prompt template
PROMPT_TEMPLATE = """
You are an expert legal assistant with 20 years of experience, specializing in making complex legal documents easy to understand. 
Your task is to take the following legal text and rewrite it in simple, clear, and plain language for a non-lawyer to understand,
like you would explain to an 18-year-old.

Follow these rules:
- Maintain the original meaning and all key details (like dates, names, amounts).
- Remove all legal jargon and complex sentence structures.
- Use short sentences and bullet points for maximum clarity.
- The tone should be helpful and straightforward.
- Do not add any new information or change the intent of the original text.
- Just start with the simplified text, no intros or outros.
- DO NOT write "Okay here is..." or "Sure, this is...".
- End with an example explanation that makes the meaning extra clear,
  but without excessive kiddish metaphors like candies or toys.

Here is the legal text you need to simplify:
---
{LEGAL_TEXT}
---
"""

def simplify_legal_text(text_to_simplify: str) -> str:
    """
    Calls Gemini API to simplify legal text.
    
    Args:
        text_to_simplify (str): Original legal text.
    
    Returns:
        str: Simplified plain-language version.
    """
    if not text_to_simplify:
        return "Error: No text provided."
    
    try:
        # Load Gemini model
        model = genai.GenerativeModel("gemini-2.0-flash")

        # Format prompt
        prompt = PROMPT_TEMPLATE.format(LEGAL_TEXT=text_to_simplify)

        # Send request
        response = model.generate_content(prompt)

        return response.text.strip() if response and response.text else "Error: No response text received."
    
    except Exception as e:
        print(f"[LLM Error] {e}")
        return "Error during text simplification."

# Local testing
if __name__ == "__main__":
    sample_legal_text = """
    Notwithstanding any other provision of this Agreement, the party of the first part 
    (hereinafter referred to as "the Disclosing Party") shall not be liable to the party 
    of the second part (hereinafter referred to as "the Receiving Party") for any 
    consequential, incidental, or indirect damages arising out of or in connection with 
    the breach of this Agreement, provided that such damages were not the result of gross 
    negligence or willful misconduct on the part of the Disclosing Party. The aforementioned 
    limitation of liability shall be effective to the maximum extent permitted by applicable law.
    """

    print("\n--- Sending to Gemini 2.0 Flash for Simplification ---\n")
    simplified = simplify_legal_text(sample_legal_text)
    print("\n--- Simplified Version ---\n")
    print(simplified)
