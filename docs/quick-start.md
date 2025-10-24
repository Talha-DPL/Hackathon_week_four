# Art.Decor.AI Quick Start Guide

## 🚀 Current Status: Week 1 Complete ✅

### What's Ready
- ✅ **Database Schema**: Complete Supabase PostgreSQL schema
- ✅ **Artwork Dataset**: 500+ curated artworks across 6 styles
- ✅ **API Endpoints**: Full REST API for artwork browsing
- ✅ **Database Models**: SQLAlchemy models for all entities
- ✅ **Documentation**: Comprehensive setup and development guides

## 🏃‍♂️ Quick Start (5 minutes)

### 1. Prerequisites
```bash
# Ensure you have Python 3.11+ and Node.js 20+
python --version  # Should be 3.11+
node --version    # Should be 20+
```

### 2. Clone and Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd art-decor-ai

# Checkout the current branch
git checkout feature/week1-setup-dataset
```

### 3. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp env.example .env
# Edit .env with your database URL
```

### 4. Database Setup
```bash
# Run the schema in your Supabase database
# Copy the contents of backend/database/schema.sql
# Paste into Supabase SQL Editor and execute

# Seed the dataset
python scripts/seed_artwork_dataset.py
```

### 5. Start the API
```bash
# Run the FastAPI server
uvicorn main:app --reload

# API will be available at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### 6. Test the API
```bash
# Health check
curl http://localhost:8000/health

# Get artworks
curl http://localhost:8000/artworks?limit=5

# Get styles
curl http://localhost:8000/styles

# Get trends
curl http://localhost:8000/trends
```

## 🎯 What You Can Do Now

### Browse Artworks
- **List all artworks**: `GET /artworks`
- **Filter by style**: `GET /artworks?style=minimalist`
- **Filter by price**: `GET /artworks?price_min=50&price_max=200`
- **Get specific artwork**: `GET /artworks/{id}`

### Explore Styles
- **Available styles**: `GET /styles`
- **Trend analysis**: `GET /trends`
- **User profiles**: `GET /users/{id}/profile`

### API Features
- **Pagination**: Use `skip` and `limit` parameters
- **Filtering**: Filter by style, price range
- **Search**: Text-based artwork search
- **Metadata**: Rich artwork information

## 📊 Dataset Overview

### Artwork Styles (500+ total)
- **Abstract**: Modern, contemporary, geometric (15%)
- **Minimalist**: Clean, simple, monochrome (20%)
- **Vintage**: Retro, classic, warm (15%)
- **Nature**: Organic, green, botanical (18%)
- **Bohemian**: Eclectic, colorful, artistic (17%)
- **Industrial**: Urban, metallic, raw (15%)

### Price Ranges
- **Minimalist**: $30-$300
- **Vintage**: $40-$400
- **Nature**: $35-$350
- **Industrial**: $45-$450
- **Abstract**: $50-$500
- **Bohemian**: $60-$600

## 🔧 Development Commands

### Backend Development
```bash
# Run with auto-reload
uvicorn main:app --reload

# Run tests
pytest tests/

# Format code
black .
isort .

# Lint code
flake8
```

### Database Operations
```bash
# Seed dataset
python scripts/seed_artwork_dataset.py

# Reset database (careful!)
python scripts/reset_database.py

# Backup database
python scripts/backup_database.py
```

## 🎨 Example API Usage

### Get Minimalist Artworks
```bash
curl "http://localhost:8000/artworks?style=minimalist&limit=3"
```

### Get Artworks in Price Range
```bash
curl "http://localhost:8000/artworks?price_min=100&price_max=300&limit=5"
```

### Get Specific Artwork
```bash
curl "http://localhost:8000/artworks/{artwork-id}"
```

### Get Available Styles
```bash
curl "http://localhost:8000/styles"
```

## 🚧 Coming Next (Week 2)

### Vision Agent Implementation
- **YOLOv8 Integration**: Wall detection in room images
- **Color Analysis**: Palette extraction from photos
- **Lighting Analysis**: Brightness and tone detection
- **Style Classification**: Room style identification

### New API Endpoints
- `POST /rooms/analyze` - Analyze uploaded room image
- `GET /rooms/{id}/analysis` - Get analysis results
- `POST /rooms/{id}/recommendations` - Get style-based suggestions

## 🐛 Troubleshooting

### Common Issues

#### Database Connection Error
```bash
# Check your DATABASE_URL in .env
echo $DATABASE_URL

# Test connection
python -c "from models.database import engine; print('Connected!')"
```

#### Import Errors
```bash
# Ensure virtual environment is activated
which python  # Should show venv path

# Reinstall dependencies
pip install -r requirements.txt
```

#### API Not Starting
```bash
# Check if port 8000 is available
netstat -an | grep 8000

# Try different port
uvicorn main:app --reload --port 8001
```

### Getting Help
1. Check the logs in terminal output
2. Review environment variables in `.env`
3. Ensure all services are running
4. Check network connectivity
5. Review the [Week 1 Implementation Guide](week1-implementation.md)

## 📚 Documentation

- [Week 1 Implementation](week1-implementation.md) - Detailed implementation guide
- [Development Workflow](development-workflow.md) - Git workflow and standards
- [Account Setup](account-setup.md) - External service setup
- [Local Setup](local-setup.md) - Development environment setup

## 🎉 Success!

You now have a fully functional Art.Decor.AI backend with:
- ✅ 500+ artwork dataset
- ✅ Complete API endpoints
- ✅ Database schema and models
- ✅ Comprehensive documentation

**Ready for Week 2**: Vision Agent implementation with YOLOv8 wall detection!

---

**Current Branch**: `feature/week1-setup-dataset`  
**Next Branch**: `feature/week2-vision-agent`  
**Status**: Week 1 Complete ✅
