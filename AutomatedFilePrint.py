import os

from watchfiles import watch, Change

def only_added(change: Change, path: str) -> bool:
    return change == Change.added


def read(path :str):
    result = []
    f = open(path, "r")
    data = f.read()
    f.close()
    data = data.split(",")

    for item in data:
        result.append(item)
        
    return tuple(result)

watch_folder = read(path="./config.txt")[0]

for changes in watch(watch_folder, raise_interrupt=False,  watch_filter=only_added):
    
    filepath = list(changes)[0][1]
    try:
        os.startfile(filepath, "print")
        print(f"printed {filepath}")
    except Exception as e:
        print(e)
 
    
