# Local Development Setup

This guide covers setting up your local development environment for the Art Decor AI project.

## System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, macOS 10.15+, or Ubuntu 18.04+
- **RAM**: 8GB (16GB recommended for AI model development)
- **Storage**: 20GB free space
- **Internet**: Stable connection for downloading dependencies

### Recommended for AI Development
- **GPU**: NVIDIA GPU with CUDA support (RTX 3060 or better)
- **RAM**: 32GB+ for large model training
- **Storage**: SSD with 100GB+ free space

## Software Installation

### 1. Python 3.11+

#### Windows
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer with "Add Python to PATH" checked
3. Verify: `python --version` and `pip --version`

#### macOS
```bash
# Using Homebrew (recommended)
brew install python@3.11

# Or download from python.org
```

#### Ubuntu/Linux
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-pip
```

### 2. Node.js 20+

#### Windows/macOS
1. Download from [nodejs.org](https://nodejs.org/)
2. Choose LTS version (20.x)
3. Verify: `node --version` and `npm --version`

#### Ubuntu/Linux
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 3. CUDA 12.x (Optional, for GPU)

#### Windows
1. Download from [NVIDIA CUDA](https://developer.nvidia.com/cuda-downloads)
2. Run installer and follow prompts
3. Verify: `nvcc --version`

#### macOS
```bash
# Install via Homebrew
brew install cuda
```

#### Ubuntu/Linux
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.0.0/local_installers/cuda-repo-ubuntu2004-12-0-local_12.0.0-525.60.13-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2004-12-0-local_12.0.0-525.60.13-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2004-12-0-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```

### 4. Git

#### Windows
1. Download from [git-scm.com](https://git-scm.com/)
2. Use default settings during installation

#### macOS
```bash
# Already installed with Xcode Command Line Tools
# Or install via Homebrew
brew install git
```

#### Ubuntu/Linux
```bash
sudo apt update
sudo apt install git
```

## Project Setup

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd art-decor-ai
```

### 2. Backend Setup

#### Create Virtual Environment
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

#### Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### Configure Environment
```bash
# Copy environment template
cp env.example .env

# Edit .env with your actual values
# Use your favorite editor (VS Code, vim, nano, etc.)
```

### 3. Frontend Setup

```bash
cd frontend
npm install
```

### 4. AI Model Setup

```bash
cd ai-model

# Create virtual environment for AI models
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install AI/ML dependencies
pip install torch torchvision torchaudio
pip install transformers
pip install jupyter notebook
pip install opencv-python
pip install pillow
pip install numpy pandas matplotlib seaborn
```

## Database Setup

### Option 1: Local PostgreSQL
```bash
# Install PostgreSQL
# Windows: Download from postgresql.org
# macOS: brew install postgresql
# Ubuntu: sudo apt install postgresql postgresql-contrib

# Create database
createdb art_decor_ai

# Update .env with local database URL
DATABASE_URL=postgresql://username:password@localhost:5432/art_decor_ai
```

### Option 2: Use Supabase (Recommended)
- Follow Supabase setup in account-setup.md
- Use Supabase connection string in .env

## Redis Setup (Optional)

### Windows
1. Download Redis from [github.com/microsoftarchive/redis](https://github.com/microsoftarchive/redis/releases)
2. Run redis-server.exe

### macOS
```bash
brew install redis
brew services start redis
```

### Ubuntu/Linux
```bash
sudo apt install redis-server
sudo systemctl start redis-server
```

## Running the Application

### 1. Start Backend
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn main:app --reload
```

### 2. Start Frontend
```bash
cd frontend
npm run dev
```

### 3. Access Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Development Tools

### Recommended VS Code Extensions
- Python
- TypeScript and JavaScript Language Features
- Tailwind CSS IntelliSense
- GitLens
- REST Client
- Thunder Client

### Useful Commands

#### Backend
```bash
# Run tests
pytest

# Format code
black .
isort .

# Lint code
flake8
```

#### Frontend
```bash
# Lint code
npm run lint

# Type check
npm run type-check

# Build for production
npm run build
```

## Troubleshooting

### Common Issues

#### Python/Node Version Issues
```bash
# Check versions
python --version
node --version
npm --version

# Update if needed
# Python: Download from python.org
# Node: Download from nodejs.org or use nvm
```

#### Permission Issues (macOS/Linux)
```bash
# Fix npm permissions
sudo chown -R $(whoami) ~/.npm
```

#### CUDA Issues
```bash
# Check CUDA installation
nvcc --version
nvidia-smi

# Install PyTorch with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

#### Database Connection Issues
- Check if PostgreSQL is running
- Verify connection string in .env
- Ensure database exists
- Check firewall settings

### Getting Help
- Check the logs in terminal output
- Review environment variables
- Ensure all services are running
- Check network connectivity

## Next Steps

1. Complete local setup
2. Set up external accounts (see account-setup.md)
3. Configure environment variables
4. Start development!
