def replaceWhitespcaes(text:str):
    reptext = """"""
    nb,nt,nnl =0,0,0

    for i in range(len(text)):
        if text[i] == '\n':
            reptext+=("$")
            nnl += 1
            
        elif text[i] == '\t':
            reptext+=("^")
            nt += 1
            
        elif text[i] == " ":
            reptext+=("&")
            nb += 1
            
        else:
            reptext+=(text[i])    

    return reptext,nb,nt,nnl



if __name__ == "__main__":
    

        text = ""

        with open(file=r"text.txt",mode='r') as f:
            text = f.read()
        
        ntext,nB,nT,nNL = replaceWhitespcaes(text)
        print(f"replaced={ntext}, blank= {nB}, tabs={nT}, newlines={nNL} ")


