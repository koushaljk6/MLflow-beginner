# MLflow-beginner





## For Dagshub:
###### first connect the github to dagshub and then copy the below code  from dagshub->remote->experiments section->code inside (using Mlflow tracking)
import dagshub
dagshub.init(repo_owner='koushaljk6', repo_name='MLflow-beginner', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/koushaljk6/MLflow-beginner.mlflow

set MLFLOW_TRACKING_USERNAME=koushaljk6

set MLFLOW_TRACKING_PASSWORD=095dd4bfe45e238a26ec97bcfa5fff2832921e35

```