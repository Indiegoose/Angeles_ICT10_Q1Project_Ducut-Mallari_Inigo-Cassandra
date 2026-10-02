from pyscript import document

def generate(event):
    
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock = document.getElementById("stock").value

    if not product_name or not stock:
        document.getElementById("sku-output").innerHTML = "Not available. Please fill form completely"
        return

    category_code = category[0:3].upper()          
    product_code = product_name[0:3].upper()      
    stock_code = str(stock)              
    sku = category_code + product_code + stock_code

    document.getElementById("sku-output").innerHTML = f"Generated SKU: <strong>{sku}</strong>"