import random
from pathlib import Path


def select_files_randomly(population, sample_size):
    if sample_size > len(population):
        print("Sample size is larger than the population size.")
        return []

    selected_files = random.sample(population, sample_size)

    return selected_files


analysis_sensitivities = "../micro-benchmark/analysis_sensitivities"
python_features = "../micro-benchmark/python_features"
file_extension = "*.py"


analysis_sensitivities_population = sorted(Path(analysis_sensitivities).rglob("*.py"))
python_features_population = sorted(Path(python_features).rglob("*.py"))


sample_size = 10  # Desired sample size
selected_files_analysis_sensitivities = select_files_randomly(
    analysis_sensitivities_population, sample_size
)
selected_files_python_features = select_files_randomly(
    python_features_population, sample_size
)

print("Selected files for evaluation from analysis_sensitivities:")
for file_name in selected_files_analysis_sensitivities:
    print(file_name)

print("\n####\n")

print("Selected files for evaluation from python_features:")
for file_name in selected_files_python_features:
    print(file_name)
