import pickle

# Load the data from the pickle file
with open('submission/predictions.pkl', 'rb') as f:
    data = pickle.load(f)

# Modify the value of the "foo" key
datas = []
for item in data:
    if (isinstance(item, float)) :
        datas.append(item)
        continue
    
    datas.append(item / item.sum())
    


# Save the modified data back to the pickle file
with open('submission/predictions.pkl', 'wb') as f:
    pickle.dump(datas, f)
