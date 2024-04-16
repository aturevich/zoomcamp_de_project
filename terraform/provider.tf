provider "google" {
  credentials = file("../gcp_creds/gcp-key.json")
  project     = var.project_id
  region      = var.region
}

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 3.5"
    }
  }
}