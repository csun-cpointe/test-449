###
# #%L
# Test pyspark lineage::Pipelines::Classification Training::Logistic Training
# %%
# Copyright (C) 2021 Booz Allen
# %%
# All Rights Reserved. You may not copy, reproduce, distribute, publish, display,
# execute, modify, create derivative works of, transmit, sell or offer for resale,
# or in any way exploit any part of this solution without Booz Allen Hamilton’s
# express written permission.
# #L%
###
"""
Driver to run this pipeline.

GENERATED STUB CODE - PLEASE ***DO*** MODIFY

Originally generated from: templates/general-mlflow/training.driver.py.vm
"""
import os
import sys

from logistic_training.impl.classification_training import ClassificationTraining
from logistic_training.generated.pipeline.pipeline_base import PipelineBase

if __name__ == "__main__":
    if os.getenv("MODE") == "no-op":
        print("Training job successfully registered.")
        sys.exit()

    PipelineBase().record_pipeline_lineage_start_event()

    ClassificationTraining().run()

    PipelineBase().record_pipeline_lineage_complete_event()
