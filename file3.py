import pickle
D={'ios':['macbook','iphone'],'android':['samsung','nokia','oneplus']}
with open('os.pkl','wb') as fobj:
    enc=pickle.dump(D,fobj)
