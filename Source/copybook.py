# FUNCTIONS TO HANDLE THE HIERARCHICAL STACK #
def fGetSetack():
    global stack, output
    tmp = output
    for k in stack:
        tmp = tmp[stack[k]]
    return tmp

def fRemStack(iStack,iLevel):
    NewStack = {}
    for k in iStack:
        if k < iLevel: NewStack[k] = iStack[k]
    return NewStack

# TYPE AND LENGTH CALCULATION #
def getLenType(atr):
    ret = {}
    FirstCh = atr[3][:1].upper()
    Picture = atr[3].upper()

    #data type
    if   'COMP-3'in atr and FirstCh=='S': ret['type'] = "pd+"
    elif 'COMP-3'in atr:                  ret['type'] = "pd"
    elif 'COMP'  in atr and FirstCh=='S': ret['type'] = "bi+"
    elif 'COMP'  in atr:                  ret['type'] = "bi"
    elif FirstCh=='S':                    ret['type'] = "zd+"
    elif FirstCh=='9':                    ret['type'] = "int"
    elif FirstCh=='X':                    ret['type'] = "string"
    else:                                 ret['type'] = "ch"

    #Total data length
    PicNum = Picture.replace("V"," ").replace("S","").replace("-","").split()
    Lgt = 0
    for x in PicNum:
        if x.find("(") > 0: 
            Lgt += int(x[x.find("(")+1:x.find(")")])
        else:
            Lgt += len(x)

    ret['length'] = Lgt

    #Data size in bytes
    if   ret['type'][:2] == "pd": ret['bytes'] = round((Lgt/2))+1
    elif ret['type'][:2] == "bi": 
        if   Lgt <  5:             ret['bytes'] = 2
        elif Lgt < 10:             ret['bytes'] = 4
        else         :             ret['bytes'] = 8
    else:                          
        if FirstCh=='-': Lgt += 1
        ret['bytes'] = Lgt
        
    return ret

############# DICTIONARY AND HIERARCHICAL LOGIC ###########################
def add2dict(lvl, grp, itm, stt, id):

    global cur, output, last, stack, FillerCount

    if itm.upper() == "FILLER":
        FillerCount += 1
        itm = itm + "-" + str(FillerCount)

    if lvl <= cur: stack = fRemStack(stack, lvl)

    stk = fGetSetack()
    stk[itm]= {}
    stk[itm]['id'] = id
    stk[itm]['level'] = lvl
    stk[itm]['group'] = grp

    if grp == True:
        stack[lvl] = itm
        cur = lvl
        if 'OCCURS'in stt: stk[itm]['occurs'] = int(stt[3])
        if 'REDEFINES'in stt: stk[itm]['redefines'] = stt[3]
    else:
        tplen = {}
        tplen = getLenType(stt)
        stk[itm]['pict'] = stt[3]
        stk[itm]['type'] = tplen['type']
        stk[itm]['length'] = tplen['length']
        stk[itm]['bytes'] = tplen['bytes']
                
############################### MAIN ###################################
# READS, CLEANS AND JOINS LINES #

FillerCount=0
cur=0
output={}
stack = {}

def toDict(lines):

    id = 0
    stt = ""
    for line in lines: 
        if line[6] != "*": stt += line.replace('\t', '    ')[6:72]    

    # READS FIELD BY FIELD / SPLITS ATTRIBUTES #
    for variable in stt.split("."):
        
        attribute=variable.split()

        if len(attribute) > 0:
            if attribute[0] != '88': 
                id += 1
                add2dict(int(attribute[0]), False if 'PIC'in attribute else True, attribute[1], attribute, id)

    return output
    
    #Create the extraction File
def CreateExtraction(obj, alt={}):
    global lrecl
    for k in obj:
        if type(obj[k]) is dict:

            t = 1 if 'occurs' not in obj[k] else obj[k]['occurs']
            
            iTimes = 0
            while iTimes < t:
                iTimes +=1

                if 'redefines' not in obj[k]:

                    if k in alt:
                        obj[k] = alt[k]

                    if obj[k]['group'] == True: 
                        CreateExtraction(obj[k], alt)
                    else:
                        # item = {}
                        # item['type'] = obj[k]['type']
                        # item['bytes']  = obj[k]['bytes']
                        # item['name'] = k
                        # transf.append(item)
                        # lrecl = lrecl + obj[k]['bytes']
                        item = {}
                        item['type'] = obj[k]['type']
                        item['bytes']  = obj[k]['bytes']
                        item['name'] = k
                        transf.append(item)
                        lrecl = lrecl + obj[k]['bytes']
                            
                        itemtable=k + " " + obj[k]['type']
                        transf1.append(itemtable)
        
                        itemtable="(.{" + str(obj[k]['bytes']) + "})"
                        transf2.append(itemtable)
                elif not alt:
                    red = {}
                    red[obj[k]['redefines']] = obj[k]
                    red[obj[k]['redefines']]['newname'] = k
                    altlay.append(red)