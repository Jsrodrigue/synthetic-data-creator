# Synthetic Data Generator

An intelligent synthetic data generator that uses OpenAI models to create realistic tabular datasets based on reference data. This project includes an intuitive web interface built with Gradio.

> **🎓 Educational Project**: This project was created as part of the comprehensive LLM Engineering course on Udemy: [LLM Engineering: Master AI and Large Language Models](https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/learn/lecture/52941433#questions/23828099). It demonstrates practical applications of LLM engineering principles, prompt engineering, and synthetic data generation techniques.

## 📋 Features

- **Intelligent Generation**: Uses OpenAI models (GPT-4o-mini, GPT-4.1-mini) to generate synthetic data
- **Web Interface**: Easy-to-use Gradio application with data preview
- **Reference Data**: Ability to load CSV files as reference to maintain statistical distributions
- **JSON Validation**: Automatic output cleaning to ensure valid JSON
- **Export**: Direct download of generated data in CSV format
- **Included Examples**: Sample datasets for people and sentiment analysis

## 🎓 LLM Engineering Concepts Demonstrated

This project showcases several key concepts from LLM Engineering:

- **Prompt Engineering**: Sophisticated system and user prompts for consistent data generation
- **Output Parsing**: Robust JSON cleaning and validation techniques
- **Data Validation**: Ensuring generated data meets quality and format requirements
- **Reference-based Generation**: Using existing data to maintain statistical properties
- **Web Interface Integration**: Building user-friendly applications with Gradio

## 🚀 Installation

### Prerequisites
- Python 3.12+
- OpenAI account with API key

### Installation with pip
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Installation with uv
```bash
# Clone the repository
git clone <your-repository>
cd synthetic_data

# Install dependencies
uv sync

# Activate virtual environment
uv shell
```

### Configuration
1. Copy the environment variables example file:
```bash
cp .env_example .env
```

2. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## 📸 Screenshots & Demo

### Application Interface
![Main Interface](docs/screenshots/main_interface.png)
*Main interface showing the synthetic data generator with all controls*

### Reference Data Preview
![Reference Data](docs/screenshots/reference_data.png)
*Reference CSV preview with example people data*

### Generated Results
![Generated Data](docs/screenshots/generated_data.png)
*Example of generated synthetic data with download option*

### Video Demo
[![Video Demo](docs/screenshots/video_thumbnail.png)](https://youtube.com/watch?v=your-demo-video)
*Click to watch a complete walkthrough of the application*


## 🎯 Usage

### Start the application
```bash
python app.py
```

The script will print a local URL (e.g., http://localhost:7860) or a shareable Gradio link — open that link in your browser.

### How to use the interface

1. **Configure Prompts**:
   - **System Prompt**: You can use the default rules or edit the system prompt for data generation.
   - **User Prompt**: Specifies what type of data to generate (default: 15 rows)

2. **Select Model**:
   - `gpt-4o-mini`: Faster and more economical
   - `gpt-4.1-mini`: Higher reasoning capacity

3. **Load Reference Data** (optional):
   - Upload a CSV file with similar data
   - Use included examples: `people_reference.csv`, `sentiment_reference.csv` or `wine_reference.csv`

4. **Generate Data**:
   - Click "🚀 Generate Data"
   - Review results in the gradio UI
   - Download the generated CSV



## 📊 Quality Evaluation

### Simple Evaluation System

The project includes a simple evaluation system focused on basic metrics and visualizations:

#### Features
- **Simple Metrics**: Basic statistical comparisons and quality checks
- **Integrated Visualizations**: Automatic generation of comparison plots in the app
- **Easy to Understand**: Clear scores and simple reports
- **Scale Invariant**: Works with datasets of different sizes
- **Temporary Files**: Visualizations are generated in temp files and cleaned up automatically




## 🛠️ Improvements and Next Steps

### Immediate Improvements

1. **Advanced Validation**:
   - Implement specific validators by data type
   - Create evaluation reports

2. **Advanced Quality Metrics**
   - Include more advanced metrics to compare multivariate similarity (for future work), e.g.:
      - C2ST (Classifier Two‑Sample Test): train a classifier to distinguish real vs synthetic — report AUROC (ideal ≈ 0.5).
      - MMD (Maximum Mean Discrepancy): kernel-based multivariate distance.
      - Multivariate Wasserstein / Optimal Transport: joint-distribution distance (use POT).
     
3. **More Models**:
   - Integrate Hugging Face models
   - Support for local models (Ollama)
   - Comparison between different models

4. **Enhanced Interface**:
   - Generation history
   - Predefined prompt templates
   - Data visualizations

### Advanced Features

1. **Conditional Generation**:
   - Data based on specific conditions
   - Controlled outlier generation
   - Maintaining complex relationships

2. **Privacy Analysis**:
   - Differential privacy metrics
   - Sensitive data detection
   - Automatic anonymization

3. **Database Integration**:
   - Direct database connection
   - Massive data generation
   - Automatic synchronization

### Scalable Architecture

1. **REST API**:
   - Endpoints for integration
   - Authentication and rate limiting
   - OpenAPI documentation

2. **Asynchronous Processing**:
   - Work queues for long generations
   - Progress notifications
   - Robust error handling

3. **Monitoring and Logging**:
   - Usage and performance metrics
   - Detailed generation logs
   - Quality alerts

## 📁 Project Structure

```
synthetic_data/
├── app.py                 # Main Gradio application
├── utils.py               # Data generation functions
├── evaluation.py          # Data evaluation system
├── demo_evaluation.py     # Evaluation demonstration script
├── notebook.ipynb        # Experiments and development
├── pyproject.toml        # Project configuration
├── requirements.txt      # Dependencies
├── data/                 # Example data
│   ├── people_reference.csv
│   └── sentiment_reference.csv
├── screenshots/          # Screenshots of the app
├── .env_example          # Environment variables template
└── README.md            # This file
```


## 📄 License

This project is under the MIT License. See the `LICENSE` file for more details.

## 🆘 Support

If you have problems or questions:

1. Check the documentation
2. Search existing issues
3. Create a new issue with problem details

## 🔗 Useful Links

- [OpenAI Documentation](https://platform.openai.com/docs)
- [Gradio Documentation](https://gradio.app/docs/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

## 🎓 Course Context & Learning Outcomes

This project was developed as part of the [LLM Engineering: Master AI and Large Language Models](https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/learn/lecture/52941433#questions/23828099) course on Udemy. It demonstrates practical implementation of:

### Key Learning Objectives:
- **Prompt Engineering Mastery**: Creating effective system and user prompts for consistent outputs
- **API Integration**: Working with OpenAI's API for production applications
- **Data Processing**: Handling JSON parsing, validation, and error management
- **Web Application Development**: Building user interfaces with Gradio

### Course Insights Applied:
- **Why OpenAI over Open Source**: This project was developed as an alternative to open-source models due to consistency issues in prompt following with models like Llama 3.2. OpenAI provides more reliable and faster results for this specific task.
- **Production Considerations**: Focus on error handling, output validation, and user experience
- **Scalability Planning**: Architecture designed for future enhancements and integrations

### Related Course Topics:
- Prompt engineering techniques
- LLM API integration and optimization
- Synthetic data generation strategies
- Production deployment considerations

---

**📚 Course Link**: [LLM Engineering: Master AI and Large Language Models](https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/learn/lecture/52941433#questions/23828099)