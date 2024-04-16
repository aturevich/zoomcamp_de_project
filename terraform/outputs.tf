output "instance_external_ip" {
  value = google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip
  description = "The external IP address of the VM instance."
}

output "data_bucket_url" {
  value = "gs://${google_storage_bucket.data_bucket.name}"
  description = "The URL of the primary data storage bucket."
}

output "spark_staged_bucket_url" {
  value = "gs://${google_storage_bucket.spark_staged_bs.name}"
  description = "The URL of the Spark staged storage bucket."
}

output "bigquery_dataset_id" {
  value = google_bigquery_dataset.ships_dataset.dataset_id
  description = "The ID of the BigQuery dataset."
}