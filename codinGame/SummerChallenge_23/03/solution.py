from json import dumps, loads
from typing import List


def merge_files(file_contents: List[str]) -> str:

    d = {}
    lists = []
    sublists = []
    
    for i in file_contents:
        temp = i.split('\n')
        for x in temp:
            lists.append(x)
    
    for i in lists:
        sublists.append(i.split(';'))
    
    for i in sublists:
        for x in i:
            if 'Name=' in x:
                sorting_temp = {}
                temp = []
                r = []
                
                if x[len("Name="):] not in d:
                    d[x[len("Name="):]] = i
                else:
                    d[x[len("Name="):]] += i
                
                if ("Name="+x[len("Name="):] in d[x[len("Name="):]]):
                    d[x[len("Name="):]].remove("Name="+x[len("Name="):])
                
                [temp.append(item) for item in d[x[len("Name="):]] if item not in temp]
                
                for e in temp:
                    sorting_temp[e.split('=')[0]] = e.split('=')[1]

                sorting_temp = dict(sorted(sorting_temp.items(), key=lambda item: item[0]))
                for v in sorting_temp:
                    r.append(v+'='+sorting_temp[v])
                
                d[x[len("Name="):]] = r
    d = sorted(d.items(), key=lambda item: item[0])
    s=''
    for i in d:
        s+='Name='+i[0]
        if len(i[1]):
            s+=';'+';'.join(i[1])
        s+='\n'
    return s[:-1]

# Ignore and do not change the code below


def try_solution(merged_file: str):
    '''
    Try a solution

    Args:

        - str (str): The contents of the merged file.
    '''
    json = merged_file
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = merge_files(
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above

