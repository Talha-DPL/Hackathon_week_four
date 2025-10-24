-- Art.Decor.AI Database Schema
-- Supabase PostgreSQL Database

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";

-- Users table (extends Supabase auth.users)
CREATE TABLE IF NOT EXISTS user_profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    preferred_styles TEXT[] DEFAULT '{}',
    color_profile JSONB DEFAULT '{}',
    budget_range JSONB DEFAULT '{"min": 0, "max": 1000}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Artwork catalog
CREATE TABLE IF NOT EXISTS artwork (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    brand VARCHAR(100),
    price DECIMAL(10,2),
    style_tags TEXT[] DEFAULT '{}',
    dominant_palette JSONB DEFAULT '{}',
    image_url TEXT NOT NULL,
    dimensions JSONB DEFAULT '{}',
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Artwork embeddings for vector search
CREATE TABLE IF NOT EXISTS artwork_embedding (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    vector VECTOR(512), -- DINOv2/CLIP embedding dimension
    artwork_id UUID REFERENCES artwork(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Room uploads and analysis
CREATE TABLE IF NOT EXISTS room_upload (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    room_type VARCHAR(50), -- living_room, bedroom, kitchen, etc.
    s3_url TEXT NOT NULL,
    palette_json JSONB DEFAULT '{}',
    lighting_json JSONB DEFAULT '{}',
    wall_detection_json JSONB DEFAULT '{}',
    style_analysis JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- User sessions and interactions
CREATE TABLE IF NOT EXISTS session (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    query_text TEXT,
    query_type VARCHAR(20), -- photo, text, voice
    topk_ids UUID[] DEFAULT '{}',
    chosen_id UUID REFERENCES artwork(id),
    rationale TEXT,
    satisfaction_score INTEGER CHECK (satisfaction_score >= 1 AND satisfaction_score <= 5),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Trend analysis and recommendations
CREATE TABLE IF NOT EXISTS trend_analysis (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    style VARCHAR(100) NOT NULL,
    trend_score DECIMAL(3,2) DEFAULT 0.0,
    seasonal_factor DECIMAL(3,2) DEFAULT 1.0,
    region VARCHAR(100),
    analysis_data JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Local stores and availability
CREATE TABLE IF NOT EXISTS local_stores (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    phone VARCHAR(20),
    website TEXT,
    store_type VARCHAR(50), -- gallery, furniture_store, art_supply
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Store inventory
CREATE TABLE IF NOT EXISTS store_inventory (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    store_id UUID REFERENCES local_stores(id) ON DELETE CASCADE,
    artwork_id UUID REFERENCES artwork(id) ON DELETE CASCADE,
    available BOOLEAN DEFAULT TRUE,
    stock_quantity INTEGER DEFAULT 0,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_artwork_style_tags ON artwork USING GIN(style_tags);
CREATE INDEX IF NOT EXISTS idx_artwork_price ON artwork(price);
CREATE INDEX IF NOT EXISTS idx_room_upload_user_id ON room_upload(user_id);
CREATE INDEX IF NOT EXISTS idx_session_user_id ON session(user_id);
CREATE INDEX IF NOT EXISTS idx_artwork_embedding_vector ON artwork_embedding USING ivfflat (vector vector_cosine_ops);
CREATE INDEX IF NOT EXISTS idx_local_stores_location ON local_stores(latitude, longitude);

-- Row Level Security (RLS) policies
ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE room_upload ENABLE ROW LEVEL SECURITY;
ALTER TABLE session ENABLE ROW LEVEL SECURITY;

-- User can only access their own data
CREATE POLICY "Users can view own profile" ON user_profiles
    FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own profile" ON user_profiles
    FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Users can view own room uploads" ON room_upload
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can view own sessions" ON session
    FOR SELECT USING (auth.uid() = user_id);

-- Functions for updating timestamps
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Triggers for updated_at
CREATE TRIGGER update_user_profiles_updated_at BEFORE UPDATE ON user_profiles
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_artwork_updated_at BEFORE UPDATE ON artwork
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
