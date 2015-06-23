def conta(a):
    '''conta le femmine'''
    colonna=a[:,0]
    femmine=colonna.sum()
    maschi=a.shape - femmine
    return femmine, maschi
print femmine, maschi
