import  os
import shutil

# lists = []
# lists.index()
# dicts = {}
# tuples = ()

ext = 'lastUpdated'

def getIsUnCompletedList(path,arrays = []):

    if os.path.isdir(path):
        [getIsUnCompletedList(os.path.join(path,c)) for c in os.listdir(path)]
    else:
        # arrays.append((lambda path: (path.endswith(".lastUpdated") ? path:None))(path))
        if path.endswith(".jar.lastUpdated"):
            arrays.append(path)
    return arrays



def main():
    path = "E:\\java\\m2\\repository"
    arr = getIsUnCompletedList(path)
    print "\n".join(arr)
    print "\n".join( (os.path.split(filePath)[0]) for filePath in arr  )
    # [(os.removedirs(os.path.split(filePath)[0])) for filePath in arr]
    # [(os.remove(os.path.split(filePath)[0])) for filePath in arr]
    [(shutil.rmtree(os.path.split(filePath)[0])) for filePath in arr]
    
    

if __name__ == '__main__':
    main()




