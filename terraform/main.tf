resource "google_storage_bucket" "data_bucket" {
  name          = "ships-data-bucket-${random_id.bucket_suffix.hex}"
  location      = var.region
  force_destroy = true
}

resource "google_storage_bucket" "spark_staged_bs" {
  name          = "spark-staged-bs-${random_id.bucket_suffix.hex}"
  location      = var.region
  force_destroy = true
}

resource "random_id" "bucket_suffix" {
  byte_length = 2
}

resource "google_compute_instance" "vm_instance" {
  name         = "data-processing-vm"
  machine_type = "e2-standard-2"
  zone         = "${var.region}-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size  = 30  # Disk size in GB
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata = {
    "PROJECT_ID" = var.project_id
    "REGION" = var.region
    "DATA_BUCKET_NAME" = google_storage_bucket.data_bucket.name
    "SPARK_BUCKET_NAME" = google_storage_bucket.spark_staged_bs.name
    "BIGQUERY_DATASET_ID" = google_bigquery_dataset.ships_dataset.dataset_id
  }

  metadata_startup_script = <<EOF
#!/bin/bash
echo "export PROJECT_ID='${var.project_id}'" >> /etc/profile
echo "export REGION='${var.region}'" >> /etc/profile
echo "export DATA_BUCKET_NAME='${google_storage_bucket.data_bucket.name}'" >> /etc/profile
echo "export SPARK_BUCKET_NAME='${google_storage_bucket.spark_staged_bs.name}'" >> /etc/profile
echo "export BIGQUERY_DATASET_ID='${google_bigquery_dataset.ships_dataset.dataset_id}'" >> /etc/profile
EOF
}

resource "google_bigquery_dataset" "ships_dataset" {
  dataset_id                  = "ships_ds"
  location                    = var.region
  description                 = "Dataset for storing ships data"
  delete_contents_on_destroy  = true
}