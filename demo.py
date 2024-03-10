from visa_approval.constants import DATABASE_NAME
from visa_approval.pipeline.training_pipeline import TrainPipeline


pipline  = TrainPipeline()
pipline.run_pipeline()