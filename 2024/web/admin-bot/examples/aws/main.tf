terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.35.0"
    }
  }
}

variable "image" {}
output "submit_url" {
  value = module.admin_bot.submit_url
}

provider "aws" {
  region = "us-east-1"
}

module "admin_bot" {
  source = "redpwn/admin-bot/aws"
  image  = var.image
  recaptcha = {
    site   = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
    secret = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
  }
}
