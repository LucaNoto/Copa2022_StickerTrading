
def FindSwappables(myNeed,myRepeated,peerNeed,peerRepeated,shinnyForShinny=True):
    #Shinny Stickers
    shinny=["00","FWC 1","FWC 2","FWC 3","FWC 4","FWC 5","FWC 6","FWC 7","QAT 2","ECU 2","SEN 2","NED 2","ENG 2","IRN 2","USA 2","WAL 2","ARG 2","KSA 2","MEX 2","POL 2","FRA 2","AUS 2","DEN 2","TUN 2","ESP 2","CRC 2","GER 2","JPN 2","BEL 2","MAR 2","CAN 2","CRO 2","BRA 2","SRB 2","SUI 2","CMR 2","POR 2","GHA 2","URU 2","KOR 2","FWC 19","FWC 20","FWC 21","FWC 22","FWC 23","FWC 24","FWC 25","FWC 26","FWC 27","FWC 28","FWC 29"]
    
    #Splitting strings
    myNeed = [i.strip() for i in myNeed.split(":")[1].split(",")]
    myRepeated = [i.strip() for i in myRepeated.split(":")[1].split(",")]

    peerNeed = [i.strip() for i in peerNeed.split(":")[1].split(",")]
    peerRepeated = [i.strip() for i in peerRepeated.split(":")[1].split(",")]


    if shinnyForShinny:
        needShinny = [i for i in myNeed if i in peerRepeated if i in shinny]
        giveShinny = [i for i in myRepeated if i in peerNeed if i in shinny]
#         print(len(needShinny),len(giveShinny))
        if len(needShinny)>len(giveShinny):
            addPadding = [i for i in myRepeated if i not in giveShinny and i in shinny][:len(needShinny)-len(giveShinny)]
            giveShinny.extend(addPadding)
            if len(needShinny)>len(giveShinny):
                needShinny = needShinny[:len(giveShinny)]
        elif len(giveShinny)>len(needShinny):
            addPadding = [i for i in peerRepeated if i not in needShinny and i in shinny][:len(giveShinny)-len(needShinny)]
            needShinny.extend(addPadding)
            if len(giveShinny)>len(needShinny):
                giveShinny = giveShinny[:len(needShinny)]
        
    elif shinnyForShinny == False:
        shinny = []
        needShinny = []
        giveShinny = []

    need = [i for i in myNeed if i in peerRepeated and i not in shinny]
    give = [i for i in myRepeated if i in peerNeed and i not in shinny]
#     print(len(need),len(give))

    if len(need)>len(give):
        addPadding = [i for i in myRepeated if i not in give and i not in shinny][:len(need)-len(give)]
        give.extend(addPadding)
        if len(need)>len(give):
            need = need[:len(give)]
    elif len(give)>len(need):
        addPadding = [i for i in peerRepeated if i not in need and i not in shinny][:len(give)-len(need)]
        need.extend(addPadding)
        if len(give)>len(need):
            give = give[:len(need)]

    #updating repeated lists for continuous trading
    myRepeatedUpdated = [i for i in myRepeated if i not in give and i not in giveShinny]
    myPaddingRepeated = [i for i in need if i not in myNeed]
    myRepeatedUpdated.extend(myPaddingRepeated)

    peerRepeatedUpdated = [i for i in peerRepeated if i not in need and i not in needShinny]
    peerPaddingRepeated = [i for i in give if i not in peerNeed]
    peerRepeatedUpdated.extend(peerPaddingRepeated)

    #updating repeated lists for continuous trading
    myNeedUpdated = [i for i in myNeed if i not in need and i not in needShinny]
    peerNeedUpdated = [i for i in peerNeed if i not in give and i not in giveShinny]

    if shinnyForShinny:
        outputText = f'''
QUERO:
- Brilhantes (total -> {len(needShinny)}): {', '.join(needShinny)} 

- Normais (total -> {len(need)}): {', '.join(need)} 

Minhas repetidas depois dessa troca (total -> {len(myRepeatedUpdated)}): {', '.join(myRepeatedUpdated)} 

As que me faltam depois dessa troca (total -> {len(myNeedUpdated)}): {', '.join(myNeedUpdated)} 

-------------------------

TE DOU:
- Brilhantes (total -> {len(giveShinny)}): {', '.join(giveShinny)} 

- Normais (total -> {len(give)}): {', '.join(give)}

Suas repetidas depois dessa troca (total -> {len(peerRepeatedUpdated)}): {', '.join(peerRepeatedUpdated)} 

As que te faltam depois dessa troca (total -> {len(peerNeedUpdated)}): {', '.join(peerNeedUpdated)} 
        '''
    else:
        outputText = f'''
QUERO (total -> {len(need)}): {', '.join(need)} 

Minhas repetidas depois dessa troca (total -> {len(myRepeatedUpdated)}): {', '.join(myRepeatedUpdated)} 

As que me faltam depois dessa troca (total -> {len(myNeedUpdated)}): {', '.join(myNeedUpdated)} 
-------------------------

TE DOU (total -> {len(give)}): {', '.join(give)}

Suas repetidas depois dessa troca (total -> {len(peerRepeatedUpdated)}): {', '.join(peerRepeatedUpdated)} 

As que te faltam depois dessa troca (total -> {len(peerNeedUpdated)}): {', '.join(peerNeedUpdated)} 

        '''


    return {'outputText':outputText, 
            'need':need,
            'needShinny':needShinny, 
            'give':give, 
            'giveShinny':giveShinny,
            'myRepeatedUpdated':myRepeatedUpdated, 
            'peerRepeatedUpdated':peerRepeatedUpdated, 
            'myNeed':myNeed,
            'myRepeated':myRepeated,
            'peerNeed':peerNeed,
            'peerRepeated':peerRepeated,
            'myNeedUpdated':myNeedUpdated,
            'peerNeedUpdated':peerNeedUpdated
            }
