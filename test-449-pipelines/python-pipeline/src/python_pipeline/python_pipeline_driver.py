###
# #%L
# Test pyspark lineage::Pipelines::Python Pipeline
# %%
# Copyright (C) 2021 Booz Allen
# %%
# All Rights Reserved. You may not copy, reproduce, distribute, publish, display,
# execute, modify, create derivative works of, transmit, sell or offer for resale,
# or in any way exploit any part of this solution without Booz Allen Hamilton’s
# express written permission.
# #L%
###
from python_pipeline.step.step1 import Step1
from python_pipeline.step.step2 import Step2
import asyncio
from krausening.logging import LogManager
from python_pipeline.generated.pipeline.pipeline_base import PipelineBase

"""
Driver to run the PythonPipeline.

GENERATED STUB CODE - PLEASE ***DO*** MODIFY

Originally generated from: templates/data-delivery-pyspark/pipeline.driver.py.vm 
"""

logger = LogManager.get_instance().get_logger("PythonPipeline")


if __name__ == "__main__":
    logger.info("STARTED: PythonPipeline driver")
    PipelineBase().record_pipeline_lineage_start_event()

    # TODO: Execute steps in desired order and handle any inbound and outbound types
    Step1().execute_step()
    asyncio.run(Step2().execute_step())
    PipelineBase().record_pipeline_lineage_complete_event()
