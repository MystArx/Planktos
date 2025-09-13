import os
import google.generativeai as genai # type: ignore
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

PROMPT_TEMPLATE = """
You are an expert legal assistant with 20 years of experience, specializing in making complex legal documents easy to understand. 
Your task is to take the following legal text and rewrite it in simple, clear, and plain language for a non-lawyer to understand.
Like you would explain to 18 year old

Follow these rules:
- Maintain the original meaning and all key details (like dates, names, amounts).
- Remove all legal jargon and complex sentence structures.
- Use short sentences and bullet points for maximum clarity.
- The tone should be helpful and straightforward.
- Do not add any new information or change the intent of the original text.
- Just Start with the simplified text, no intro or outro.
- DO NOT GIVE ANY INTRO, like  "Okay here is .... " or "Sure , this is .." etc. Just start with explanation.
- End with an example, as you would explain to a child, but without excessive kiddish metaphors like candies and toys etc.

Here is the legal text you need to simplify:
---
{LEGAL_TEXT}
---
"""


def simplify_legal_text(text_to_simplify: str) -> str:
    '''Return simplified legal text using Gemini API'''
    if not text_to_simplify:
        return "Error: No text provided."
    
    try:
        model=genai.GenerativeModel('gemini-2.0-flash')

        prompt=PROMPT_TEMPLATE.format(LEGAL_TEXT=text_to_simplify)

        response=model.generate_content(prompt)

        return response.text
    
    except Exception as e:

        print(f"API error: {e}")
        return f"Error during text simplification ."
    

#TODO: Remove this block, it is just to check the function
if __name__ == '__main__':    # Example usage
    sample_legal_text = """
    Notwithstanding any other provision of this Agreement, the party of the first part (hereinafter referred to as "the Disclosing Party") shall not be liable to the party of the second part (hereinafter referred to as "the Receiving Party") for any consequential, incidental, or indirect damages arising out of or in connection with the breach of this Agreement, provided that such damages were not the result of gross negligence or willful misconduct on the part of the Disclosing Party. The aforementioned limitation of liability shall be effective to the maximum extent permitted by applicable law.
    """
    
    print("--- Sending to Gemini 2.0 Flash for Simplification ---")
    simplified_version = simplify_legal_text(sample_legal_text)
    print("\n--- Simplified Version ---")
    print(simplified_version)