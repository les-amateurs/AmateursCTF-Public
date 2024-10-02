terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.58.0"
    }
  }
}

variable "project" {}
output "submit_url" {
  value = module.admin_bot.submit_url
}

provider "google" {
  project = var.project
  region  = "us-east1"
}

module "admin_bot" {
  source    = "redpwn/admin-bot/google"
  image     = "us-east1-docker.pkg.dev/redpwn/admin-bot/example"
  recaptcha = {
    site   = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
    secret = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
  }
}
