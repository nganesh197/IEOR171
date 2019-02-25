def take_all(arr):
    for each in arr:

        present, absent = split_p_a(each[1])

        present = each_name(present)
        absent = each_name(absent)

        each[1] = present
        each.extend([absent])
    return arr

def starboard(darr, carr):
    for c in carr:
        if c[0] in darr:
            darr[c[0]][0] += c[1]
            darr[c[0]][1] += c[2]
    # print(darr)
    return darr

def split_p_a(arr):
    #find the indexes of present and past
    if "present" in arr:
        pindex_start = ((arr.index("present")+len("present")+2))
        pindex_end = (arr.index("absent"))
        pname = arr[pindex_start : pindex_end]
        #print(pname) #shows all the names that are present

        aindex_start = ((arr.index("absent")+len("absent")+2))
        aname = arr[aindex_start :]
        #print(aname) #shows all the names that are absent
        return pname, aname
    return "FORMAT INCORRECT", "FORMAT INCORRECT"

def each_name(subarr):
    return subarr.split(',')

def create_blanks(cr):
    panda = list(cr.values())
    for i in range(len(panda)):
        plen = len(panda[i][0])
        alen = len(panda[i][1])
        pminusa = plen - alen
        #print(panda[i][0])

        for j in range(pminusa):
            panda[i][1] += ['']

    return cr
