# pythonFlask

## install python 3
    brew install python 
for other OS check the official  instalation guide

## install flask
Guide: [Flask Guide](https://flask.palletsprojects.com/en/stable/installation/)

##### Create a project folder and a .venv folder within: 
    python3 -m venv .venv

##### Before you work on your project, activate the corresponding environment:
    . .venv/bin/activate
##### Install Flask
    pip install flask

## Deploying to AWS EKS

This Helm chart has been configured to facilitate deployment to AWS Elastic Kubernetes Service (EKS). Key considerations:

### 1. Image Repository (AWS ECR)

Before deploying, you **must** update the `image.repository` value in `chart/values.yaml`. It is currently set to a placeholder:
`YOUR_AWS_ACCOUNT_ID.dkr.ecr.YOUR_AWS_REGION.amazonaws.com/YOUR_APP_NAME`

You need to replace this with the URI of your Docker image hosted in AWS Elastic Container Registry (ECR).

**To find your ECR image URI:**
1. Push your Docker image to ECR.
2. In the AWS Management Console, navigate to the Amazon ECR service.
3. Select your repository.
4. The URI is displayed next to your image tag(s).

### 2. Service Type (LoadBalancer)

The `service.type` in `chart/values.yaml` is set to `LoadBalancer` by default for AWS deployments. This will automatically provision an AWS Elastic LoadBalancer (ELB) to expose your application externally.

**To find the external IP/hostname of your service:**
After deploying the Helm chart, you can get the LoadBalancer's address by running:
`kubectl get service <your-release-name>-flask-app -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'`
(Replace `<your-release-name>` with the name of your Helm release). It might take a few minutes for the LoadBalancer to be provisioned and the external IP/hostname to become available.

### 3. Resource Configuration

The `chart/values.yaml` file includes commented-out placeholders for CPU and memory `resources` (requests and limits). It is highly recommended to uncomment and configure these based on your application's needs for production deployments on EKS to ensure stable performance and efficient resource utilization.