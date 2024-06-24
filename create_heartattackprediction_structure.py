import os
import subprocess

project_root = r"D:\Heartattackprediction"

structure = [
    ".github/workflows/ci-cd-pipeline.yml",
    "data/raw/",
    "data/processed/",
    "notebooks/research.ipynb",
    "src/components/data_ingestion.py",
    "src/components/data_preprocessing.py",
    "src/components/model_training.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
]

# Create project structure
for path in structure:
    full_path = os.path.join(project_root, path)
    if path.endswith("/"):
        os.makedirs(full_path, exist_ok=True)
    else:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            pass

# Specify the path to the Python 3.9 executable
python_39_path = r"C:\Users\Admin\AppData\Local\Programs\Python\Python39\python.exe"  # Update with the correct path

# Create virtual environment with the name "Heartattackpredictionnew" using Python 3.9
venv_path = os.path.join(project_root, 'Heartattackpredictionnew')
subprocess.run([python_39_path, '-m', 'venv', venv_path])

# Install required packages
requirements = [
    "numpy",
    "pandas",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "jupyter"
]

with open(os.path.join(project_root, 'requirements.txt'), 'w') as f:
    f.write('\n'.join(requirements))

# Activate the virtual environment and install the requirements
pip_executable = os.path.join(venv_path, 'Scripts', 'pip.exe')

subprocess.run([pip_executable, 'install', '-r', os.path.join(project_root, 'requirements.txt')])

print("Project structure and virtual environment 'Heartattackpredictionnew' setup successfully.")
