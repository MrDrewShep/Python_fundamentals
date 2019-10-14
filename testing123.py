
products = [ {"prod_name" : "nvidia"}, {"prod_name" : "amd"}, {"prod_name" : "arm"}, {"prod_name" : "intel"}, {"prod_name" : "risc"}]
search_term = "intel"

for row in products:
    if search_term in row["prod_name"]:
        print("found")
    else:
        print("not found here")