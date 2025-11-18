#!/bin/bash
set -e

# Configuration from arguments
PROJECT_ID=$1
REGION=${2:-us-central1}
SERVICE_NAME=${3:-tc-mcp-server}

if [ -z "$PROJECT_ID" ]; then
    echo "Usage: ./deploy.sh <PROJECT_ID> [REGION] [SERVICE_NAME]"
    echo "Example: ./deploy.sh my-gcp-project us-central1 tc-mcp-server"
    exit 1
fi

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
