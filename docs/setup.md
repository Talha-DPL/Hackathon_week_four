# Setup Guide

This guide will help you set up the Art Decor AI project locally.

## Prerequisites

### Required Software

1. **Python 3.11+**
   - Download from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **Node.js 20+**
   - Download from [nodejs.org](https://nodejs.org/)
   - Verify installation: `node --version`

3. **CUDA 12.x (Optional, for GPU acceleration)**
   - Download from [NVIDIA CUDA](https://developer.nvidia.com/cuda-downloads)
   - Required for AI model training and inference

### Required Accounts

Create accounts for the following services:

#### 1. GitHub
- Go to [github.com](https://github.com)
- Create a new account or sign in
- Create a new repository for the project

#### 2. Vercel
- Go to [vercel.com](https://vercel.com)
- Sign up with GitHub
- Connect your repository for frontend deployment

#### 3. Render (Alternative: AWS EC2)
- Go to [render.com](https://render.com)
- Sign up with GitHub
- Set up for backend deployment

#### 4. Supabase
- Go to [supabase.com](https://supabase.com)
- Create a new project
- Note down your project URL and API key

#### 5. AWS S3
- Go to [aws.amazon.com](https://aws.amazon.com)
- Create an AWS account
- Set up S3 bucket for file storage
- Create IAM user with S3 permissions

#### 6. Google Maps API
- Go to [Google Cloud Console](https://console.cloud.google.com)
- Enable Maps JavaScript API
- Create API key

## Local Setup

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd art-decor-ai
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
cp env.example .env
# Edit .env with your actual values
```

### 3. Frontend Setup
```bash
cd frontend
npm install
```

### 4. AI Model Setup
```bash
cd ai-model
# Download model weights to weights/ directory
# Set up your preferred AI framework (PyTorch, TensorFlow, etc.)
```

## Environment Variables

Copy `backend/env.example` to `backend/.env` and fill in your values:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/art_decor_ai
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_BUCKET=your-s3-bucket-name
```

## Running the Application

### Backend
```bash
cd backend
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm run dev
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
