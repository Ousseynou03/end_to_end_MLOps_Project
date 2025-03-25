import mlflow
import pandas as pd

# Configurer MLflow pour pointer vers DAGsHub
MLFLOW_TRACKING_URI = "https://dagshub.com/dioneousseynou03/end_to_end_MLOps_Project.mlflow"

# set MLflow Username
# set MLflow Password
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

experiment_name = "Default"
experiment = mlflow.get_experiment_by_name(experiment_name)

if experiment is None:
    raise ValueError(f"L'expérience {experiment_name} n'existe pas sur MLflow.")

# Récupérer tous les runs de l'expérience
runs = mlflow.search_runs(experiment_ids=[experiment.experiment_id])

if runs.empty:
    raise ValueError("Aucun run trouvé dans l'expérience.")

# Trier les runs par accuracy (du plus grand au plus petit)
best_run = runs.sort_values(by="metrics.precision", ascending=False).iloc[0]

# Récupérer l'ID du run et l'URI du modèle
best_run_id = best_run["run_id"]
best_model_uri = f"runs:/{best_run_id}/model"

print(f"Le meilleur modèle a une precision de : {best_run['metrics.precision']}")
print(f"ID du run : {best_run_id}")
print(f"URI du modèle : {best_model_uri}")

import mlflow.artifacts

# Définir le dossier où télécharger les artefacts
model_dir = "final_model"

# Télécharger tous les artefacts du meilleur modèle
mlflow.artifacts.download_artifacts(run_id=best_run_id, dst_path=model_dir)

print(f"Tous les artefacts du modèle ont été téléchargés dans : {model_dir}")