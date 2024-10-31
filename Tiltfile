allow_k8s_contexts('local')
docker_prune_settings(num_builds=1, keep_recent=1)

aissemble_version = '1.10.0-SNAPSHOT'

build_args = { 'DOCKER_BASELINE_REPO_ID': 'ghcr.io/',
               'VERSION_AISSEMBLE': aissemble_version}

# Kafka
yaml = helm(
    'test-449-deploy/src/main/resources/apps/kafka-cluster',
    values=['test-449-deploy/src/main/resources/apps/kafka-cluster/values.yaml',
        'test-449-deploy/src/main/resources/apps/kafka-cluster/values-dev.yaml']
)
k8s_yaml(yaml)

# logistic-training-compiler
local_resource(
    name='compile-logistic-training',
    cmd='cd test-449-pipelines/classification-training/logistic-training && poetry run behave tests/features && poetry build && cd - && \
    cp -r test-449-pipelines/classification-training/logistic-training/dist test-449-docker/test-449-logistic-training-docker/target/logistic-training',
    deps=['test-449-pipelines/classification-training/logistic-training'],
    auto_init=False,
    ignore=['**/dist/']
)

k8s_kind('SparkApplication', image_json_path='{.spec.image}')


yaml = local('helm template oci://ghcr.io/boozallen/aissemble-spark-application-chart --version %s --values test-449-pipelines/spark-pipeline/src/main/resources/apps/spark-pipeline-base-values.yaml,test-449-pipelines/spark-pipeline/src/main/resources/apps/spark-pipeline-dev-values.yaml' % aissemble_version)
k8s_yaml(yaml)
k8s_resource('spark-pipeline', port_forwards=[port_forward(4747, 4747, 'debug')], auto_init=False, trigger_mode=TRIGGER_MODE_MANUAL)
# test-449-logistic-training-docker
docker_build(
    ref='test-449-logistic-training-docker',
    context='test-449-docker/test-449-logistic-training-docker',
    build_args=build_args,
    extra_tag='test-449-logistic-training-docker:latest',
    dockerfile='test-449-docker/test-449-logistic-training-docker/src/main/resources/docker/Dockerfile'
)


# policy-decision-point
docker_build(
    ref='test-449-policy-decision-point-docker',
    context='test-449-docker/test-449-policy-decision-point-docker',
    build_args=build_args,
    dockerfile='test-449-docker/test-449-policy-decision-point-docker/src/main/resources/docker/Dockerfile'
)


# spark-worker-image
docker_build(
    ref='test-449-spark-worker-docker',
    context='test-449-docker/test-449-spark-worker-docker',
    build_args=build_args,
    extra_tag='test-449-spark-worker-docker:latest',
    dockerfile='test-449-docker/test-449-spark-worker-docker/src/main/resources/docker/Dockerfile'
)

# python-pipeline-compiler
local_resource(
    name='compile-python-pipeline',
    cmd='cd test-449-pipelines/python-pipeline && poetry run behave tests/features && poetry build && cd - && \
    cp -r test-449-pipelines/python-pipeline/dist/* test-449-docker/test-449-spark-worker-docker/target/dockerbuild/python-pipeline && \
    cp test-449-pipelines/python-pipeline/dist/requirements.txt test-449-docker/test-449-spark-worker-docker/target/dockerbuild/requirements/python-pipeline',
    deps=['test-449-pipelines/python-pipeline'],
    auto_init=False,
    ignore=['**/dist/']
)


k8s_yaml('test-449-deploy/src/main/resources/apps/logistic-training-image/logistic-training-image.yaml')


k8s_yaml('test-449-deploy/src/main/resources/apps/spark-worker-image/spark-worker-image.yaml')


yaml = helm(
   'test-449-deploy/src/main/resources/apps/spark-infrastructure',
   name='spark-infrastructure',
   values=['test-449-deploy/src/main/resources/apps/spark-infrastructure/values.yaml',
       'test-449-deploy/src/main/resources/apps/spark-infrastructure/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'test-449-deploy/src/main/resources/apps/s3-local',
   name='s3-local',
   values=['test-449-deploy/src/main/resources/apps/s3-local/values.yaml',
       'test-449-deploy/src/main/resources/apps/s3-local/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'test-449-deploy/src/main/resources/apps/postgres',
   name='postgres',
   values=['test-449-deploy/src/main/resources/apps/postgres/values.yaml',
       'test-449-deploy/src/main/resources/apps/postgres/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'test-449-deploy/src/main/resources/apps/metadata',
   name='metadata',
   values=['test-449-deploy/src/main/resources/apps/metadata/values.yaml',
       'test-449-deploy/src/main/resources/apps/metadata/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'test-449-deploy/src/main/resources/apps/spark-operator',
   name='spark-operator',
   values=['test-449-deploy/src/main/resources/apps/spark-operator/values.yaml',
       'test-449-deploy/src/main/resources/apps/spark-operator/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'test-449-deploy/src/main/resources/apps/shared-infrastructure',
   name='shared-infrastructure',
   values=['test-449-deploy/src/main/resources/apps/shared-infrastructure/values.yaml',
       'test-449-deploy/src/main/resources/apps/shared-infrastructure/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'test-449-deploy/src/main/resources/apps/model-training-api',
   name='model-training-api',
   values=['test-449-deploy/src/main/resources/apps/model-training-api/values.yaml',
       'test-449-deploy/src/main/resources/apps/model-training-api/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'test-449-deploy/src/main/resources/apps/mlflow-ui',
   name='mlflow-ui',
   values=['test-449-deploy/src/main/resources/apps/mlflow-ui/values.yaml',
       'test-449-deploy/src/main/resources/apps/mlflow-ui/values-dev.yaml']
)
k8s_yaml(yaml)
yaml = helm(
   'test-449-deploy/src/main/resources/apps/policy-decision-point',
   name='policy-decision-point',
   values=['test-449-deploy/src/main/resources/apps/policy-decision-point/values.yaml',
       'test-449-deploy/src/main/resources/apps/policy-decision-point/values-dev.yaml']
)
k8s_yaml(yaml)

yaml = local('helm template oci://ghcr.io/boozallen/aissemble-spark-application-chart --version %s --values test-449-pipelines/python-pipeline/src/python_pipeline/resources/apps/python-pipeline-base-values.yaml,test-449-pipelines/python-pipeline/src/python_pipeline/resources/apps/python-pipeline-dev-values.yaml' % aissemble_version)
k8s_yaml(yaml)
k8s_resource('python-pipeline', port_forwards=[port_forward(4747, 4747, 'debug')], auto_init=False, trigger_mode=TRIGGER_MODE_MANUAL)

yaml = helm(
   'test-449-deploy/src/main/resources/apps/pipeline-invocation-service',
   name='pipeline-invocation-service',
   values=['test-449-deploy/src/main/resources/apps/pipeline-invocation-service/values.yaml',
       'test-449-deploy/src/main/resources/apps/pipeline-invocation-service/values-dev.yaml']
)
k8s_yaml(yaml)
# Add deployment resources here