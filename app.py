import gradio as gr
import os
import atexit
from src.IO_utils import cleanup_temp_files
from src.data_generation import generate_and_evaluate_data
from src.plot_utils import display_reference_csv

# ==========================================================
# Setup
# ==========================================================

# Temporary folder for images
PROJECT_TEMP_DIR = "temp_plots"
os.makedirs(PROJECT_TEMP_DIR, exist_ok=True)

# Ensure temporary plot images are deleted when the program exits
atexit.register(lambda: cleanup_temp_files(PROJECT_TEMP_DIR))

# ==========================================================
# Prompts
# ==========================================================

SYSTEM_PROMPT = """
You are a precise synthetic data generator. Your only task is to output valid JSON arrays of dictionaries.

Rules:
1. Output a single JSON array starting with '[' and ending with ']'.
2. Do not include markdown, code fences, or explanatory text — only the JSON.
3. Keep all columns exactly as specified; do not add or remove fields (index must be omitted).
4. Respect data types: text, number, date, boolean, etc.
5. Ensure internal consistency and realistic variation.
6. If a reference table is provided, generate data with similar statistical distributions for numerical and categorical variables, 
   but never copy exact rows. Each row must be independent and new.
7. For personal information (names, ages, addresses, IDs), ensure diversity and realism — individual values may be reused to maintain realism, 
   but never reuse or slightly modify entire reference rows.
8. Escape internal double quotes in strings with a backslash (") for JSON validity.
9. Do NOT replace single quotes in normal text; they should remain as-is.
10. Escape newline (
), tab (	), or carriage return (
) characters as 
, 	, 
 inside strings.
11. Remove any trailing commas before closing brackets.
12. Do not include any reference data or notes about it in the output.
13. The output must always be valid JSON parseable by standard JSON parsers.
14. Don't repeat any exact column.
15. When using reference data, consider the entire dataset for statistical patterns and diversity; 
do not restrict generation to the first rows or the order of the dataset.
"""

USER_PROMPT = """
Generate exactly 15 rows of synthetic data following all the rules above. 
Ensure that all strings are safe for JSON parsing and ready to convert to a pandas DataFrame.
"""

# ==========================================================
# Gradio App
# ==========================================================
with gr.Blocks() as demo:

    # Store temp folder in state
    temp_dir_state = gr.State(value=PROJECT_TEMP_DIR)

    gr.Markdown("# 🧠 Synthetic Data Generator (with OpenAI)")

    # ======================================================
    # Tabs for organized sections
    # ======================================================
    with gr.Tabs():

        # ------------------------------
        # Tab 1: Input
        # ------------------------------
        with gr.Tab("Input"):

            # System prompt in collapsible
            with gr.Accordion("System Prompt (click to expand)", open=False):
                system_prompt_input = gr.Textbox(
                    label="System Prompt",
                    value=SYSTEM_PROMPT,
                    lines=20
                )

            # User prompt box
            user_prompt_input = gr.Textbox(label="User Prompt", value=USER_PROMPT, lines=5)

            # Model selection
            model_select = gr.Dropdown(
                label="OpenAI Model",
                choices=["gpt-4o-mini", "gpt-4.1-mini"],
                value="gpt-4o-mini"
            )

            # Reference CSV upload
            reference_input = gr.File(label="Reference CSV (optional)", file_types=[".csv"])

            # Examples inside accordion
            with gr.Accordion("Try example reference files", open=False):
                gr.Examples(
                    examples=["data/sentiment_reference.csv","data/people_reference.csv","data/wine_reference.csv"],
                    inputs=reference_input
                )

            # Generate button
            generate_btn = gr.Button("🚀 Generate Data")

            # Download button
            download_csv = gr.File(label="Download CSV")

        # ------------------------------
        # Tab 2: Reference Table
        # ------------------------------
        with gr.Tab("Reference Table"):
            reference_display = gr.DataFrame(label="Reference CSV Preview")

        # ------------------------------
        # Tab 3: Generated Table
        # ------------------------------
        with gr.Tab("Generated Table"):
            output_df = gr.DataFrame(label="Generated Data")
            

        # ------------------------------
        # Tab 4: Evaluation
        # ------------------------------
        with gr.Tab("Comparison"):
            with gr.Accordion("Evaluation Results (click to expand)", open=True):
                evaluation_df = gr.DataFrame(label="Evaluation Results")

        # ------------------------------
        # Tab 5: Visualizations
        # ------------------------------

        with gr.Tab("Visualizations"):
            gr.Markdown("# Click on the box to expand")
            
            images_gallery = gr.Gallery(
                label="Column Visualizations",
                show_label=True,
                columns=2,
                height='auto',
                interactive=True
            )

        # Hidden state for internal use
        generated_state = gr.State()

    # ======================================================
    # Event bindings
    # ======================================================
    generate_btn.click(
        fn=generate_and_evaluate_data,
        inputs=[system_prompt_input, user_prompt_input, temp_dir_state, reference_input, model_select],
        outputs=[output_df, download_csv, evaluation_df, generated_state, images_gallery]
    )

    reference_input.change(
        fn=display_reference_csv,
        inputs=[reference_input],
        outputs=[reference_display]
    )

demo.launch(debug=True)
