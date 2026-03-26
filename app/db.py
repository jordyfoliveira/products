import psycopg as pgsql
from psycopg.types.json import Jsonb
import datetime

def get_conn():
    return pgsql.connect(
        #host="localhost",
        #port=5433,
        host="db",
        port="5432",
        dbname="products_db",
        user="app",
        password="app",
    )
    
def log_action(cur, action: str, entity: str, entity_id: int, details: Jsonb):
    cur.execute(
        """
        INSERT INTO audit_logs (action, entity, entity_id, details)
        VALUES (%s, %s, %s, %s);
        """,
        (action, entity, entity_id, details),
    )
    
def list_products():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, sku, name, price, stock, is_active, created_at
                FROM products
                ORDER BY id;
                """
            )
            return cur.fetchall()
        
def sku_exists(sku : str) -> bool:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT sku
                FROM products
                WHERE sku = %s;
                """,
                (sku,)
                )
            result = cur.fetchone()
    return False if result is None else True
        
def get_sku_by_id(cur, product_id : int) -> str | None:
    cur.execute(
        """
        SELECT sku
        FROM products
        WHERE id = %s;
        """,
        (product_id,)
        )
    result = cur.fetchone()
    return None if result is None else result[0]
        
def get_product_by_id(product_id : int) -> tuple[int, str, str, float, int, bool, datetime.datetime] | None:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, sku, name, price, stock, is_active, created_at
                FROM products
                WHERE id = %s;
                """,
                (product_id,)
            )
            result = cur.fetchone()
    #if result is None:
        #return None
    return None if result is None else result

def create_product(sku: str, name: str, price: float, stock: int):
    data = {"sku": sku, "name": name, "price": price, "stock": stock}
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO products (sku, name, price, stock)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
                """,
                (sku, name, price, stock),
            )
            product_id = cur.fetchone()[0]
            log_action(cur, "Insert", sku, product_id, Jsonb(data))
        #conn.commit() #redundância com with get_conn() as conn
    return product_id

def update_stock(product_id: int, new_stock: int) -> int | None:
    data = {"id": product_id, "stock": new_stock}
    with get_conn() as conn:
        with conn.cursor() as cur:
            get_sku = get_sku_by_id(cur, product_id)
            cur.execute(
                """
                UPDATE products
                SET stock = %s,
                    updated_at = NOW()
                WHERE id = %s
                RETURNING id;
                """,
                (new_stock, product_id),
            )
            result = cur.fetchone()
            if result is not None and get_sku is not None:
                log_action(cur, "Update", get_sku, result[0], Jsonb(data))
            #if result is not None:
            #    conn.commit() #redundância com with get_conn() as conn
    #if result is None:
        #return None if result is None
    return None if result is None else result[0]

def delete_product(product_id: int) -> int | None:
    data = {"id": product_id}
    with get_conn() as conn:
        with conn.cursor() as cur:
            get_sku = get_sku_by_id(cur, product_id)
            cur.execute(
                """
                DELETE
                FROM products
                WHERE id = %s
                RETURNING id;
                """,
                (product_id,)
            )
            result = cur.fetchone()
            if result is not None and get_sku is not None:
                log_action(cur, "Delete", get_sku, result[0], Jsonb(data))
        #if result is not None:
        #    conn.commit() #redundância com with get_conn() as conn
    #if result is None:
        #return None
    return None if result is None else result[0]
    
if __name__ == "__main__":
    product_by_id = get_product_by_id(22)
    print(product_by_id)
    #delete = delete_product(38)
    #print("Produto removido: ", delete)
    #new_id = create_product("SKU010", "Produto Teste", 9.99, 10)
    #print("Criado produto ID:", new_id)
    #updated = update_stock(1, 50)
    #print("Atualizado:", updated)
    
    #products = list_products()
    #print(products)
    # Teste rápido: liga e faz um SELECT simples
    #with get_conn() as conn:
    #    with conn.cursor() as cur:
    #        cur.execute("SELECT 1;")
    #        print("DB OK ->", cur.fetchone())
    
    
#def create_product(sku: str, name: str, price: float, stock: int):
#    with get_conn() as conn:
#        with conn.cursor() as cur:
#            cur.execute(
#                """
#                INSERT INTO products (sku, name, price, stock)
#                VALUES (%s, %s, %s, %s)
#                RETURNING id;
#                """,
#                (sku, name, price, stock),
#            )
#            product_id = cur.fetchone()[0]
#        #conn.commit() #redundância com with get_conn() as conn
#    return product_id