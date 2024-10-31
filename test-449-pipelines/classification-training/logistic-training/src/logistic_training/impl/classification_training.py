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
Implementation of this pipeline.

GENERATED STUB CODE - PLEASE ***DO*** MODIFY

Originally generated from: templates/general-mlflow/training.impl.py.vm 
"""

import json
from aissemble_security.pdp_client import AissembleSecurityException
from typing import List

from ..generated.classification_training_base import (
    ClassificationTrainingBase,
    DataFrame,
    DatasetSplits,
)

import mlflow


class ClassificationTraining(ClassificationTrainingBase):
    """
    Implementation of this pipeline.
    """

    def __init__(self):
        super().__init__("classification_training")
        # Set information about the ownership, documentation, and hardware details of the pipeline for tagging purposes.
        # Implement any additional initialization for the pipeline.

    def load_dataset(self) -> DataFrame:
        # Implement loading of the dataset for training,
        # and return the dataset as a DataFrame.

        # TODO: load dataset and convert to DataFrame, and set information about the origin of the dataset for tagging purposes.
        dataset = DataFrame()
        self.set_dataset_origin(None)

        return dataset

    def prep_dataset(self, dataset: DataFrame) -> DataFrame:
        # Implement last-mile data preparation on the loaded dataset that has been
        # passed through the dataset parameter, and return the prepped dataset.
        # If last-mile data preparation is not required, then just return the dataset.
        return dataset

    def select_features(self, dataset: DataFrame) -> List[str]:
        # Implement feature selection using the prepped dataset that has been passed
        # through the dataset parameter, and return the list of selected features.
        # If feature selection is not required, then return all features in the dataset.

        # TODO: select features from the dataset
        selected_features = dataset.columns.tolist()

        return selected_features

    def split_dataset(self, dataset: DataFrame) -> DatasetSplits:
        # Implement the creation of the training and testing splits using the dataset
        # with selected features that has been passed in through the dataset parameter,
        # and return a DatasetSplits object containing the splits.

        # TODO: create training/testing splits
        train_split = None
        test_split = None

        return DatasetSplits(train_split, test_split)

    # TODO: Update the return type of this to be match your expected model type such as LogisticRegression or Sequential.
    def train_model(self, train_dataset: any) -> any:
        # Implement the training of the model using the training split
        # that has been passed in through the train_dataset parameter,
        # and return the trained model.

        # TODO: create model based on what return type is needed and set model information for tagging purposes.
        self.set_model_information(None, None)
        model = None

        # TODO: train model using model.fit(...) on the training split

        return model

    # TODO: Update the model type to match what is returned in the train_model method
    def evaluate_model(self, model: any, test_dataset: any) -> float:
        # Implement the evaluation of the trained model using the testing split that has
        # been passed through the test_dataset parameter, and return the evaluation score.

        # TODO: evaluate model using model.predict(...) on the testing split
        # TODO: obtain the evaluation score using model.score(...) on the testing split
        score = 0

        # Log the score of the model
        mlflow.log_metric("score", score)

        return score

    # TODO: Update the model type to match what is returned in the train_model method
    def save_model(self, model: any) -> None:
        # Implement saving of the trained model.

        # TODO: save model using the correct mlflow module such as sklearn or keras. Below is an example using sklearn:
        # mlflow.sklearn.log_model(model, "model")
        pass

    # TODO: Update the model type to match what is returned in the train_model method
    def deploy_model(self, score: float, model: any) -> None:
        # Implement deploying of the trained model based on the evaluation score, if needed.
        pass
