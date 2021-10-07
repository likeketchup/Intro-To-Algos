from typing import List
#cat input_file.txt | python script.py

def parse_input(num_pages:int,num_requests:int,request:List)-> int:
    misses : int = 0
    pages = []
    pages_used = 0
    for i in range(num_requests):
        if(pages_used<num_pages):
            pages.append(request[i])
            misses+=1
            pages_used+=1
            continue
        else:
            if(request[i] in pages):
                continue
            # page fault 
            farthest = -1
            index_of_substitute = 0
            #find the farthest page
            for num,j in enumerate(pages):
                # if this page will occur 
                if j in request[i:]:
                    next = request[i:].index(j)
                    if farthest<next:
                        farthest = next
                        index_of_substitute = num
                #this page will not occur in the future 
                else:
                    #pages[num] = request(i)
                    farthest = -1
                    index_of_substitute = num
                    break
            pages[index_of_substitute] = requests[i]
            misses+=1

    return misses

if __name__ =="__main__":
    num_instances=int(input())
    for _ in range(num_instances):
        num_pages: int = input()
        num_requests : int = input()
        requests = input().split(" ")
        print((parse_input(int(num_pages),int(num_requests),requests)))