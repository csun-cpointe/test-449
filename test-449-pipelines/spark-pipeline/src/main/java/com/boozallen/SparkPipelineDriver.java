package com.boozallen;

/*-
 * #%L
 * Test pyspark lineage::Pipelines::Spark Pipeline
 * %%
 * Copyright (C) 2021 Booz Allen
 * %%
 * All Rights Reserved. You may not copy, reproduce, distribute, publish, display, 
 * execute, modify, create derivative works of, transmit, sell or offer for resale, 
 * or in any way exploit any part of this solution without Booz Allen Hamilton’s 
 * express written permission.
 * #L%
 */

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


import java.util.concurrent.CompletionStage;

import jakarta.enterprise.inject.Any;
import jakarta.enterprise.inject.spi.CDI;

import com.boozallen.pipeline.PipelineBase;

/**
 * Configures the steps needed to run a Spark-based implementation for SparkPipeline.
 *
 * This pipeline serves the following purpose: ${pipeline.description}.
 *
 * Please **DO** modify with your customizations, as appropriate.
 *
 * Originally generated from: templates/pipeline.driver.impl.java.vm 
 */
public class SparkPipelineDriver extends SparkPipelineBaseDriver {

  private static final Logger logger = LoggerFactory.getLogger(SparkPipelineDriver.class);
  
  public static void main(String[] args) {
    logger.info("STARTED: {} driver", "SparkPipeline");
    SparkPipelineBaseDriver.main(args);

    PipelineBase.getInstance().recordPipelineLineageStartEvent();


    final Step1 step1 = CDI.current().select(Step1.class, new Any.Literal()).get();
    step1.executeStep();

    final Step2 step2 = CDI.current().select(Step2.class, new Any.Literal()).get();
    CompletionStage<Void> step2Result = step2.executeStep();
    PipelineBase.getInstance().recordPipelineLineageCompleteEvent();
  }
}
