# Art Decor AI

An intelligent interior design platform that uses AI to help users create beautiful, personalized living spaces.

## 🏗️ Project Structure

```
art-decor-ai/
├── frontend/          # Next.js + Tailwind CSS
├── backend/           # FastAPI + AI agents
├── ai-model/          # AI model weights and notebooks
└── docs/              # Documentation
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **Node.js 20+**
- **CUDA 12.x** (optional, for GPU acceleration)

### Required Accounts

Create accounts for the following services:

- [ ] **GitHub** - Version control and repository
- [ ] **Vercel** - Frontend deployment
- [ ] **Render** (or AWS EC2) - Backend hosting
- [ ] **Supabase** - Database and authentication
- [ ] **AWS S3** - File storage
- [ ] **Google Maps API** - Location services

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd art-decor-ai
   ```

2. **Follow the detailed setup guides:**
   - [Account Setup Guide](./docs/account-setup.md) - Create all required accounts
   - [Local Setup Guide](./docs/local-setup.md) - Set up your development environment
   - [Complete Setup Guide](./docs/setup.md) - Full project setup

3. **Start development:**
   ```bash
   # Backend
   cd backend
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   uvicorn main:app --reload

   # Frontend
   cd frontend
   npm install
   npm run dev
   ```

## 🛠️ Technology Stack

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Vercel** - Deployment

### Backend
- **FastAPI** - Python web framework
- **PostgreSQL** - Database (via Supabase)
- **Redis** - Caching and sessions
- **Celery** - Background tasks
- **Render** - Deployment

### AI/ML
- **PyTorch** - Deep learning framework
- **Transformers** - Pre-trained models
- **OpenCV** - Computer vision
- **Jupyter** - Notebooks and experimentation

### Infrastructure
- **Supabase** - Database and auth
- **AWS S3** - File storage
- **Google Maps** - Location services
- **GitHub** - Version control

## 📚 Documentation

- [Setup Guide](./docs/setup.md) - Complete setup instructions
- [Account Setup](./docs/account-setup.md) - Create required accounts
- [Local Setup](./docs/local-setup.md) - Development environment
- [API Documentation](./docs/api.md) - Backend API reference
- [Frontend Guide](./docs/frontend.md) - Frontend development
- [AI Models](./docs/ai-models.md) - AI model documentation
- [Deployment](./docs/deployment.md) - Deployment instructions

## 🎯 Features

- **AI-Powered Design Suggestions** - Generate interior design ideas
- **Style Classification** - Identify and match design styles
- **Color Palette Generation** - Create harmonious color schemes
- **Furniture Placement** - Optimal furniture arrangement
- **3D Visualization** - Interactive room previews
- **User Authentication** - Secure user accounts
- **Project Management** - Save and organize designs

## 🔧 Development

### Running Locally

1. **Backend API**: http://localhost:8000
2. **Frontend**: http://localhost:3000
3. **API Docs**: http://localhost:8000/docs

### Environment Variables

Copy `backend/env.example` to `backend/.env` and configure:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/art_decor_ai
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
GOOGLE_MAPS_API_KEY=your-google-maps-api-key
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_BUCKET=your-s3-bucket-name
```

## 🚀 Deployment

### Frontend (Vercel)
- Automatic deployment from GitHub
- Configured for Next.js
- CDN and performance optimization

### Backend (Render)
- Automatic deployment from GitHub
- Environment variable configuration
- Auto-scaling and monitoring

### Database (Supabase)
- Managed PostgreSQL
- Built-in authentication
- Real-time subscriptions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- Check the [documentation](./docs/)
- Open an issue on GitHub
- Contact the development team

## 🎨 AI Model Capabilities

- **Interior Design Generation**: Create room layouts and designs
- **Style Transfer**: Apply different design styles to spaces
- **Color Harmony**: Generate complementary color palettes
- **Furniture Recognition**: Identify and suggest furniture
- **Space Optimization**: Maximize room functionality
- **Mood Analysis**: Understand user preferences and style

---

**Happy Designing! 🏠✨**
