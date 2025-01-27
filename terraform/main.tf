provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      billing-use = var.billing_use
    }
  }
}

terraform {
  required_version = ">= 0.13.0"
  backend "s3" {}
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

data "aws_caller_idendity" "current" {}

data "aws_region" "current" {}


