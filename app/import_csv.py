import pandas as pd
from db import create_product as cp, sku_exists as se

#path = "C:\\Users\\Utilizador\\Documents\\VSC\\Meus exercícios\\products\\inputs\\new_product.csv"
required_columns = ["sku", "name", "price", "stock"]

def csv_to_db(localPath):
    df = pd.read_csv(localPath)
    df.columns = df.columns.str.lower()
    
    if not all(col in df.columns for col in required_columns):
        missing_cols = [col for col in required_columns if col not in df.columns]
        return f"Faltam as seguintes colunas obrigatórias: {', '.join(missing_cols)}"
    
    df = df[required_columns]
    
    
    num_lines = df.shape[0]
    added_lines = 0
    rejected_lines = 0
    
    for row in df.itertuples():
        sku = row.sku
        if(pd.isna(sku) or len(sku) != 6 or not sku.startswith("SKU") or not sku[3:].isdigit()):
            #print(f"SKU {sku} é inválido. Produto não importado.")
            rejected_lines += 1
            continue

        name = row.name
        if pd.isna(name) or len(name) < 3:
            #print(f"Nome {name} é inválido. Produto não importado.")
            rejected_lines += 1
            continue
    
        price = row.price
        try:
            if pd.isna(price):
                rejected_lines += 1
                continue
            price = float(price)
            if price < 0.01:
                #print(f"Preço {price} é inválido. Produto não importado.")
                rejected_lines += 1
                continue
        except (ValueError, TypeError):
            #print("Tipo de dado inválido. Produto não importado.")
            rejected_lines += 1
            continue
    
        stock = row.stock
        try:
            if pd.isna(stock):
                rejected_lines += 1
                continue
            stock = int(stock)
            if stock < 1:
                #print(f"Stock {stock} é inválido. Produto não importado.")
                rejected_lines += 1
                continue
        except (ValueError, TypeError):
            #print("Tipo de dado inválido. Produto não importado.")
            rejected_lines += 1
            continue
    
        if se(sku):
            #print(f"SKU {sku} já existe. Produto não importado.")
            rejected_lines += 1
        else:
            cp(sku, name, price, stock)
            added_lines += 1

    return f"{num_lines} linhas lidas.\n{added_lines} produtos importados.\n{rejected_lines} produtos rejeitados."
    
if __name__ == "__main__":
    print(csv_to_db("C:\\Users\\Utilizador\\Documents\\VSC\\Meus exercícios\\products\\inputs\\HP_Product.csv"))