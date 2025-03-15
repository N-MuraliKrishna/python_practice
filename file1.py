with open ('pythonlogo.png','rb') as fobj:
    data=fobj.read()
    with open ('duplicatepythonlogo.png','wb') as gobj:
        gobj.write(data)
