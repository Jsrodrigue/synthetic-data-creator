from src.openai_utils import generate_synthetic_data_openai
from src.evaluator import SimpleEvaluator
import pandas as pd

def generate_and_evaluate_data(system_prompt, user_prompt, temp_dir, reference_file=None, openai_model="gpt-4o-mini"):
    """
    Generate synthetic data using an OpenAI model and evaluate it against a reference dataset.

    This function generates synthetic data based on the provided prompts, optionally compares it
    with a reference CSV dataset using the SimpleEvaluator, and creates visualizations (histograms
    and boxplots) for each column.

    Args:
        system_prompt (str): The system-level prompt guiding the OpenAI model.
        user_prompt (str): The user-level prompt specifying the data generation request.
        temp_dir (str): Path to the temporary directory where visualization images will be saved.
        reference_file (Optional[Union[str, file-like]]): Path or file object of a reference CSV dataset.
        openai_model (str, optional): Name of the OpenAI model to use. Defaults to "gpt-4o-mini".

    Returns:
        Tuple[
            pd.DataFrame,           # Generated synthetic data
            str,                    # Path to the generated CSV file
            pd.DataFrame,           # Evaluation results as a DataFrame
            Dict[str, List[Optional[Image.Image]]],  # Dictionary of visualizations per column
            List[Image.Image]       # Flattened list of all generated images (histograms + boxplots)
        ]
    """
    df, csv_path = generate_synthetic_data_openai(system_prompt, user_prompt, reference_file, openai_model)

    reference_df = None
    if reference_file:
        reference_df = pd.read_csv(reference_file.name if hasattr(reference_file, "name") else reference_file)

    if reference_df is not None:
        evaluator = SimpleEvaluator(temp_dir=temp_dir)
        evaluator.evaluate(reference_df, df)
        report_df = evaluator.results_as_dataframe()
        vis_dict = evaluator.create_visualizations_temp_dict(reference_df, df)
    else:
        report_df = pd.DataFrame()
        vis_dict = {}

    # Collect all images (histograms and boxplots) into a single list
    all_images = []
    for imgs in vis_dict.values():
        all_images.extend([img for img in imgs if img is not None])

    return df, csv_path, report_df, vis_dict, all_images
