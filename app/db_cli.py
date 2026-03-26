from db import list_products, get_product_by_id, create_product, update_stock, delete_product, sku_exists, get_conn
from pathlib import Path
import json
import datetime


def handle_list() -> str | list[tuple[int, str, str, float, int, bool, datetime.datetime]]:
    text = list_products()    
    #if text == []:
    if not text:
        text = "Sem produtos para mostrar."
        #text = "id | sku | name | price | stock | active | created_at"
    return text

def handle_get_by_id() -> str  | tuple[int, str, str, float, int, bool, datetime.datetime]:
    product_id = input("Introduza um id: ")
    while not product_id.isdigit():
        print("ID inválido. Introduza pfv o ID do produto.")
        product_id = input("Introduza um id: ")
    product_id = int(product_id)
                
    text = get_product_by_id(product_id)
    if text is None:
        text = "Produto não encontrado."
    return text

def handle_create() -> str:
    val = input("Introduza um id com formato 000: SKU")
    while len(val) != 3 or not val.isdigit():
        print("Sku inválido.")
        val = input("Introduza um id com formato 000: SKU")
    sku = "SKU" + val
                
    name = input("Introduza um nome: ")
    while len(name) < 3:
        print("Nome inválido.")
        name = input("Introduza um nome: ")
                
    price = input("Introduza um preço: ")
    while True:
        try:
            price = float(price)
            if price > 0:
                break
            else:
                print("Não é um valor válido")
                price = input("Introduza um preço: ")
        except ValueError:
            print("Não é um valor válido")
            price = input("Introduza um preço: ")
                
    stock = input("Introduza um stock: ")
    while not stock.isdigit():
        print("Quantidade inválida.")
        stock = input("Introduza um stock: ")
    stock = int(stock)
                
    text = sku_exists(sku)
    if text:
        text = "SKU já existente. Pfv introduza um novo SKU único para criar novo produto."
    else:
        newproduct = create_product(sku, name, price, stock)
        text =  "Novo produto criado com o ID " + str(newproduct)
    return text

def handle_update_stock() -> str:
    product_id = input("Introduza um id: ")
    while not product_id.isdigit():
        print("ID inválido. Introduza pfv o ID do produto.")
        product_id = input("Introduza um id: ")
    product_id = int(product_id)
                
    stock = input("Introduza um stock: ")
    while not stock.isdigit():
        print("Quantidade inválida.")
        stock = input("Introduza um stock: ")
    stock = int(stock)
                
    text = update_stock(product_id, stock)
    if text is None:
        text = "Produto não encontrado."
    else:
        #text = "Stock do produto " + str(product_id) + " actualizado para " + str(stock) + "."
        text = f"Stock do produto {product_id} actualizado para {stock}."
    return text

def handle_delete() -> str:
    product_id = input("Introduza um id: ")
    while not product_id.isdigit():
        print("ID inválido.")
        product_id = input("Introduza um id: ")
    product_id = int(product_id)
                
    text = delete_product(product_id)
    if text is None:
        text = "Produto não encontrado / nada apagado"
    else:
        text = "Produto removido."
    return text

def handle_export_json(path: Path) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    
    results = []
    columns = ["id", "sku", "name", "price", "stock", "active", "created_at"]
    rows = list_products()
    
    for row in rows:
        data = dict(zip(columns, row))
        data["created_at"] = data["created_at"].isoformat()
        data["price"] = float(data["price"])
        results.append(data)
    #print(results)
    
    
    with path.open("w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=2)
        
    return "Ficheiro criado."

def handle_logs() -> str | list[tuple[int, datetime.datetime, str, str, int]]:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, ts, action, entity, entity_id
                FROM  audit_logs
                ORDER BY id DESC;
                """
            )
            result = cur.fetchmany(5)
    return "Sem logs." if not result else result

def menu():
    while True:
        print("1) Listar produtos")
        print("2) Ver produto por ID")
        print("3) Criar produto")
        print("4) Atualizar stock")
        print("5) Apagar produto")
        print("6) Exportar produtos (JSON)")
        print("7) Listar audit logs (opcional)")
        print("0) Sair")
        option = input("Escolha uma opção: ").strip()
        
        if option == "1":
            val = handle_list()
            print(val)
        
        elif option == "2":
            val = handle_get_by_id()
            print(val)
        
        elif option == "3":
            val = handle_create()
            print(val)
        
        elif option == "4":
            val = handle_update_stock()
            print(val)
        
        elif option == "5":
            val = handle_delete()
            print(val)
        
        elif option == "6":
            default_output = Path("output") / "products.json"
            val = handle_export_json(default_output)
            print(val)
            
        elif option == "7":
            val = handle_logs()
            print (val)
        
        elif option == "0":
            break
    
if __name__ == "__main__":
    #print(sku_exists("SKU001"))
    menu()