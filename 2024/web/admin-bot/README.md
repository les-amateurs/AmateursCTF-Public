# [redpwn/admin-bot](https://hub.docker.com/r/redpwn/admin-bot)

A scalable service for client-side web CTF challenges

## Quick Start

### GCP

In [`examples/gcp`](https://github.com/redpwn/admin-bot/tree/master/examples/gcp), run:

```sh
gcloud auth application-default login
terraform init
terraform apply --var "project=$(gcloud config get-value project)"
```

### AWS

In [`examples/aws`](https://github.com/redpwn/admin-bot/tree/master/examples/aws), run:

```sh
aws configure
repo=$(aws ecr create-repository --repository-name admin-bot --region us-east-1 --query repository.repositoryUri --output text)
docker pull redpwn/admin-bot-example
docker tag redpwn/admin-bot-example "$repo"
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin "$repo"
docker push "$repo"
terraform init
terraform apply --var "image=$(docker image inspect "$repo" -f '{{ index .RepoDigests 0 }}')"
```

After applying, Terraform outputs a `submit_url`. To submit a URL to the admin bot, visit `<submit_url>/one`.

## Deployment

1. Create a [`config.js` file](#challenge-configuration) and a [`Dockerfile`](https://github.com/redpwn/admin-bot/blob/master/examples/image/Dockerfile).

### GCP

2. Build and push the image to [`gcr.io`](https://cloud.google.com/container-registry) or [`pkg.dev`](https://cloud.google.com/artifact-registry).
1. Use the [Terraform module](https://registry.terraform.io/modules/redpwn/admin-bot/google/latest) to deploy to Cloud Run.

### AWS

2. Build and push the image to [ECR](https://aws.amazon.com/ecr/).
1. Use the [Terraform module](https://registry.terraform.io/modules/redpwn/admin-bot/aws/latest) to deploy to Fargate and Lambda.

## Challenge Configuration

The [`config.js` file](https://github.com/redpwn/admin-bot/blob/master/examples/image/config.js) must export a `Map` named `challenges`.

The key of each entry is its challenge ID. To submit a URL to the admin bot, visit `/<challenge id>`.

The value of each entry is an object with properties:

* `name`: the display name of the challenge
* `timeout`: the timeout in milliseconds for each admin bot visit
* `handler`: a function which returns a `Promise` and accepts the submitted URL and a [Puppeteer `BrowserContext`](https://pptr.dev/#?show=api-class-browsercontext)
* `urlRegex` (optional): a regex to check the URL against (default: `/^https?:\/\//`)

To mitigate possible Chrome vulnerabilities, JIT/WebAssembly is disabled.

## Terraform Configuration

### GCP

Terraform module: [`redpwn/admin-bot/google`](https://registry.terraform.io/modules/redpwn/admin-bot/google/latest).

Example configuration: [`examples/gcp/main.tf`](https://github.com/redpwn/admin-bot/blob/master/examples/gcp/main.tf).

### AWS

Terraform module: [`redpwn/admin-bot/aws`](https://registry.terraform.io/modules/redpwn/admin-bot/aws/latest).

Example configuration: [`examples/aws/main.tf`](https://github.com/redpwn/admin-bot/blob/master/examples/aws/main.tf).
