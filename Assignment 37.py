# Read product file and tran_dtl file and implement inner join using loops (use two0 for loops)

product_path = 'SQL FILES/product.csv'
tran_dtl_path = 'SQL FILES/tran_dtl_1_2019.csv '

product_dict = {}
tran_dtl_dict = {}

count = -1


# product_file
print(" opening product file")
for row in open(product_path):
    #skipping the header row
    if (count == -1):
        count+=1
        continue
#extracting the data in the rows
    p_id, description, price, category, max_qty = row.strip().split(",")
    p_id = int(p_id) #converting the P_id to integers
    product_dict[p_id] = [p_id, description, price, category, max_qty]

#print("product_dictionary")
#print(product_dict)


#tran_dtl file
#print("opening tran dtl file")

for row in open(tran_dtl_path):
    if (count == 0):
        count += 1
        continue
#extracting the date in the rows
    tran_id, p_id, tran_price, tran_qty, date = row.strip().split(",")
    p_id = int(p_id)
    tran_dtl_dict[p_id] = [tran_id, p_id, tran_price, tran_qty, date]
#print("tran_dtl_dictionary")
#print(tran_dtl_dict)

inner_join = []
for key,value in product_dict.items():
    if(key in tran_dtl_dict):
        line = value + tran_dtl_dict[key]
        inner_join.append(line)

print(inner_join)
