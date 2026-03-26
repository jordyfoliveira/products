-- products table
CREATE TABLE IF NOT EXISTS products (
  id          SERIAL PRIMARY KEY,
  sku         TEXT NOT NULL UNIQUE,
  name        TEXT NOT NULL,
  description TEXT,
  price       NUMERIC(10,2) NOT NULL CHECK (price >= 0),
  stock       INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
  is_active   BOOLEAN NOT NULL DEFAULT TRUE,
  created_at  TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

-- audit logs table (eventos "de negócio")
CREATE TABLE IF NOT EXISTS audit_logs (
  id        SERIAL PRIMARY KEY,
  ts        TIMESTAMP NOT NULL DEFAULT NOW(),
  action    TEXT NOT NULL,
  entity    TEXT NOT NULL,
  entity_id INT,
  details   JSONB
);

-- índices úteis
CREATE INDEX IF NOT EXISTS idx_products_name ON products (name);
CREATE INDEX IF NOT EXISTS idx_audit_logs_ts ON audit_logs (ts);