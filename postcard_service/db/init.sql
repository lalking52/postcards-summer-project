mkdir -p postcard_service/db
cat > postcard_service/db/init.sql << 'EOF'
CREATE TABLE IF NOT EXISTS postcards (
    id SERIAL PRIMARY KEY,
    recipient TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
EOF