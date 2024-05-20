price = [(125,5), (200,12), (251,15), (1100,18)]
final_list = []
for price,gst in price:
    final_list.append((price,gst,price+(price*(gst/100))))

print(final_list)