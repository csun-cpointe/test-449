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
Configurations for this pipeline, read from the pipeline properties file.

GENERATED STUB CODE - PLEASE ***DO*** MODIFY

Originally generated from: templates/general-mlflow/training.config.py.vm 
"""

from krausening.properties import PropertyManager


class PipelineConfig:
    """
    Configurations for this pipeline, read from the pipeline properties file.
    """

    def __init__(self):
        self.properties = PropertyManager.get_instance().get_properties(
            "pipeline.properties"
        )

    def mlflow_tracking_uri(self):
        """
        Returns the directory for tracking MLflow training runs.
        """
        return self.properties["mlflow_tracking_uri"]

    def kafka_server(self):
        """
        Returns the Kafka server host:port value.
        """
        return self.properties["kafka_server"]
