# Variables
PROJECT_ID="speedy-surface-463712-g3"
REGION_FUNCS="us-central1"
REGION_SQL="us-central1"
ZONE_VM="us-central1-a"
BUCKET="pusc-gce-bucket-$(date +%Y%m%d)-$RANDOM"
INSTANCE_SQL="pusc-gce-sql"
DB_NAME="db_puscgce"
VM_NAME="pusc-gce-vm-apache"

# Habilitar APIs
gcloud services enable compute.googleapis.com storage.googleapis.com sqladmin.googleapis.com cloudfunctions.googleapis.com run.googleapis.com

# Bucket público
gcloud storage buckets create gs://$BUCKET --location=$REGION_FUNCS
echo "<h1>Hola desde GCP Storage</h1>" > index.html
gcloud storage cp index.html gs://$BUCKET
gcloud storage buckets add-iam-policy-binding gs://$BUCKET --member=allUsers --role=roles/storage.objectViewer
echo "https://storage.googleapis.com/$BUCKET/index.html"

# Cloud Function (gen2)
gcloud functions deploy pusc-gce-contar-palabras   --gen2 --region=$REGION_FUNCS --runtime=nodejs20   --entry-point=contarPalabras --trigger-http   --allow-unauthenticated --min-instances=0

# Cloud SQL (creación temporal para CRUD y capturas)
gcloud sql instances create $INSTANCE_SQL --database-version=MYSQL_8_0 --tier=db-f1-micro --region=$REGION_SQL --availability-type=zonal
gcloud sql databases create $DB_NAME --instance=$INSTANCE_SQL
gcloud sql users set-password root --host=% --instance=$INSTANCE_SQL --password 'Root1234!'

# VM Apache e2-micro
gcloud compute firewall-rules create pusc-gce-allow-http --network=default --allow=tcp:80 --target-tags=http-server --direction=INGRESS
gcloud compute instances create $VM_NAME --zone=$ZONE_VM --machine-type=e2-micro --image-family=debian-12 --image-project=debian-cloud --tags=http-server --metadata=startup-script='#!/bin/bash
apt-get update
apt-get install -y apache2
systemctl enable apache2
systemctl start apache2
echo "<h1>It works - PUSC-GCE</h1>" > /var/www/html/index.html
'

# Limpieza
# gcloud compute instances delete $VM_NAME --zone=$ZONE_VM --quiet
# gcloud sql instances delete $INSTANCE_SQL --quiet
# gcloud functions delete pusc-gce-contar-palabras --region=$REGION_FUNCS --quiet
# gcloud storage rm -r gs://$BUCKET
