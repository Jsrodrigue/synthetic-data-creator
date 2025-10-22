import json
import os
import re
import tempfile

import openai
import pandas as pd
from dotenv import load_dotenv


def _clean_json_output(raw_text: str) -> str:
    """
    Cleans raw OpenAI output to produce valid JSON.
    Only escapes double quotes and control characters; single quotes remain unchanged.
    """
    text = raw_text.strip()
    # Remove code fences or HTML
    text = re.sub(r"```(?:json)?", "", text)
    text = re.sub(r"</?[^>]+>", "", text)

    # Escape double quotes inside string values
    def escape_quotes(match):
        value = match.group(1)
        value = value.replace('"', r"\"")  # escape only double quotes
        value = value.replace("\n", r"\n").replace("\r", r"\r").replace("\t", r"\t")
        return f'"{value}"'

    text = re.sub(r'"(.*?)"', escape_quotes, text)

    # Ensure JSON array brackets
    if not text.startswith("["):
        text = "[" + text
    if not text.endswith("]"):
        text += "]"

    # Remove trailing commas before closing brackets
    text = re.sub(r",\s*]", "]", text)
    return text

def generate_synthetic_data_openai(
    system_prompt: str,
    user_prompt: str,
    reference_file=None,
    openai_model: str = "gpt-4o-mini",
    max_tokens: int = 2048,
    temperature=0.0,
):
    """
    Generates synthetic tabular data using OpenAI and returns a pandas DataFrame and CSV path.
    """
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Prepare full prompt
    if reference_file:
        df_ref = pd.read_csv(reference_file)
        reference_data = df_ref.to_dict(orient="records")
        user_prompt_full = (
            f"{user_prompt}\nFollow the structure and distribution of the reference data, "
            f"but do NOT copy any exact values:\n{reference_data}"
        )
    else:
        user_prompt_full = user_prompt

    response = openai.chat.completions.create(
        model=openai_model,  # "gpt-4o-mini" or "gpt-4.1-mini"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt_full},
        ],
        max_completion_tokens=max_tokens,
        temperature=temperature,  # e.g., 0.7
    )

    raw_text = response.choices[0].message.content
    cleaned_json = _clean_json_output(raw_text)

    try:
        data = json.loads(cleaned_json)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON generated. Error: {e}\nTruncated output: {cleaned_json[:500]}"
        )

    df = pd.DataFrame(data)

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(tmp_file.name, index=False)
    tmp_file.close()

    return df, tmp_file.name
