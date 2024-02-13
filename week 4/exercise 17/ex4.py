'''
 Use os.listdir (http://mng.bz/YreB) to get the names of files in the current
directory. What file extensions (i.e., suffixes following the final . character)
appear in that directory? It’ll probably be helpful to use os.path.splitext
(http://mng.bz/GV4v)
'''
import os

def check_unique_file_extentions(path):
    output = set()
    lis = os.listdir(path)
    for elem in lis:
        output.add(os.path.splitext(elem)[-1])
    
    return sorted(output)


if __name__ == "__main__":
    print(check_unique_file_extentions('.'))