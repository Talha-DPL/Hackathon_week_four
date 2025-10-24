# Account Setup Guide

This guide provides step-by-step instructions for creating all required accounts for the Art Decor AI project.

## 1. GitHub Account

### Purpose
- Version control and code repository
- CI/CD integration
- Project collaboration

### Setup Steps
1. Go to [github.com](https://github.com)
2. Click "Sign up" if you don't have an account
3. Choose a username, email, and password
4. Verify your email address
5. Create a new repository named `art-decor-ai`
6. Set repository to public or private (your choice)

### Required Actions
- [ ] Create GitHub account
- [ ] Create new repository
- [ ] Generate Personal Access Token (Settings > Developer settings > Personal access tokens)
- [ ] Note down your GitHub username and token

## 2. Vercel Account

### Purpose
- Frontend deployment and hosting
- Automatic deployments from GitHub
- CDN and performance optimization

### Setup Steps
1. Go to [vercel.com](https://vercel.com)
2. Click "Sign up" and choose "Continue with GitHub"
3. Authorize Vercel to access your GitHub account
4. Import your `art-decor-ai` repository
5. Configure build settings:
   - Framework Preset: Next.js
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `.next`

### Required Actions
- [ ] Create Vercel account
- [ ] Connect GitHub repository
- [ ] Configure deployment settings
- [ ] Note down your Vercel domain

## 3. Render Account (Alternative: AWS EC2)

### Purpose
- Backend API hosting
- Database hosting
- Background job processing

### Setup Steps
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Create a new Web Service
4. Connect your repository
5. Configure settings:
   - Environment: Python 3
   - Build Command: `cd backend && pip install -r requirements.txt`
   - Start Command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

### Required Actions
- [ ] Create Render account
- [ ] Create Web Service
- [ ] Configure environment variables
- [ ] Note down your Render URL

## 4. Supabase Account

### Purpose
- PostgreSQL database
- Authentication
- Real-time subscriptions
- File storage

### Setup Steps
1. Go to [supabase.com](https://supabase.com)
2. Click "Start your project"
3. Sign up with GitHub
4. Create a new project:
   - Name: `art-decor-ai`
   - Database Password: (generate strong password)
   - Region: Choose closest to your users
5. Wait for project setup (2-3 minutes)
6. Go to Settings > API to get your keys

### Required Actions
- [ ] Create Supabase project
- [ ] Note down Project URL
- [ ] Note down anon/public key
- [ ] Note down service_role key
- [ ] Set up database schema

## 5. AWS S3 Account

### Purpose
- File storage for images
- Model weights storage
- Static asset hosting

### Setup Steps
1. Go to [aws.amazon.com](https://aws.amazon.com)
2. Create AWS account (requires credit card)
3. Go to S3 service
4. Create a new bucket:
   - Bucket name: `art-decor-ai-storage` (must be globally unique)
   - Region: Choose appropriate region
   - Block all public access: Uncheck (for public assets)
5. Create IAM user:
   - Go to IAM > Users > Create user
   - Username: `art-decor-ai-s3-user`
   - Attach policy: `AmazonS3FullAccess`
   - Create access key

### Required Actions
- [ ] Create AWS account
- [ ] Create S3 bucket
- [ ] Create IAM user
- [ ] Note down Access Key ID and Secret Access Key
- [ ] Configure bucket permissions

## 6. Google Maps API

### Purpose
- Location services
- Maps integration
- Geocoding

### Setup Steps
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select existing
3. Enable APIs:
   - Maps JavaScript API
   - Geocoding API
   - Places API
4. Create credentials:
   - Go to APIs & Services > Credentials
   - Create API Key
   - Restrict the key to your domains

### Required Actions
- [ ] Create Google Cloud project
- [ ] Enable required APIs
- [ ] Create API key
- [ ] Configure API restrictions
- [ ] Note down your API key

## Environment Variables Summary

After setting up all accounts, you'll need these environment variables:

```env
# GitHub
GITHUB_TOKEN=your-github-token

# Vercel
VERCEL_TOKEN=your-vercel-token

# Render
RENDER_API_KEY=your-render-api-key

# Supabase
SUPABASE_URL=your-supabase-url
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_KEY=your-supabase-service-key

# AWS S3
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_BUCKET=your-s3-bucket-name
AWS_REGION=your-aws-region

# Google Maps
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
```

## Next Steps

1. Complete all account setups
2. Configure environment variables
3. Set up local development environment
4. Deploy to staging
5. Deploy to production

## Security Notes

- Never commit API keys to version control
- Use environment variables for all secrets
- Enable API key restrictions where possible
- Regularly rotate access keys
- Monitor usage and costs
