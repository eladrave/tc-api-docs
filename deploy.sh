#!/bin/bash
set -e

# Default configuration
PROJECT_ID=${1:-chkp-gcp-prd-kenobi-box}
REGION="us-central1"
SERVICE_NAME="tc-mcp-server"
IMAGE_NAME="gcr.io/$PROJECT_ID/$SERVICE_NAME"

echo "========================================================"
echo "Deploying $SERVICE_NAME to Google Cloud Run"
echo "Project: $PROJECT_ID"
echo "Region:  $REGION"
echo "Image:   $IMAGE_NAME"
echo "========================================================"

# 1. Prepare Dockerfile
# We need the Dockerfile in the root for the build context to be correct
echo "[1/3] Preparing Dockerfile..."
if [ -f "MCP/Dockerfile" ]; then
    cp MCP/Dockerfile Dockerfile
else
    echo "Error: MCP/Dockerfile not found!"
    exit 1
fi

# 2. Build and Push Image
echo "[2/3] Building and Pushing Container Image..."
gcloud builds submit --tag "$IMAGE_NAME" --project "$PROJECT_ID" .

# Cleanup temporary Dockerfile
rm Dockerfile

# 3. Deploy to Cloud Run
echo "[3/3] Deploying to Cloud Run..."
gcloud run deploy "$SERVICE_NAME" \
    --image "$IMAGE_NAME" \
    --project "$PROJECT_ID" \
    --region "$REGION" \
    --allow-unauthenticated

echo "========================================================"
echo "Deployment Complete!"
echo "Service URL: $(gcloud run services describe $SERVICE_NAME --project $PROJECT_ID --region $REGION --format 'value(status.url)')"
echo "========================================================"
