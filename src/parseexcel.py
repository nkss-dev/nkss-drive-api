import pandas, json
x = pandas.read_excel("links.xlsx")

coursecodes = ['CEIR11', 'CEIR12', 'CEPC12', 'CEPC14', 'CELR12', 'CELR14', 'CEPC21', 'CEPC25', 'CEPC27', 'CEPC29', 'CELR21', 'CELR23', 'CELR25', 'CEPC22', 'CEPC26', 'CELR22', 'CELR24', 'CELR26', 'CELR28', 'CEPC31', 'CEPC33', 'CEPC35', 'CEPC37', 'CEPC39', 'CELR31', 'CELR33', 'CEPC41', 'CEPC43', 'CEPC45', 'CEPC47', 'CEPC42', 'CEPC44', 'CELR42', 'CEPE12', 'CEPE13', 'CEPE14', 'CEPE15', 'CEOE16', 'CEPE17', 'CEPE18', 'CEPE19', 'CEPE20', 'CEPE40', 'CEOE11', 'CEOE12', 'CEOE13', 'CEOE14', 'CEOE15', 'CCEOE18', 'CHIR11', 'CHLR11', 'CHIR12', 'CHIR13', 'CHIR14', 'CHLR12', 'CSIR11', 'CSIR13', 'CSPC10', 'CSPC12', 'CSPC14', 'CSIR12', 'CSPC21', 'CSPC23', 'CSPC25', 'CSPC27', 'CSPC29', 'CSPC20', 'CSPC22', 'CSPC24', 'CSPC26', 'CSPE20', 'CSPE22', 'CSPE24', 'CSPE26', 'CSPE60', 'CSPE62', 'CSPE64', 'CSPC31', 'CSPC33', 'CSPC35', 'CSPC37', 'CSPE31', 'CSPE33', 'CSPE35', 'CSPE37', 'CSPE71', 'CSPE73', 'CSPE75', 'CSPE77', 'CSPC41', 'CSPC43', 'CSPC45', 'CSPE41', 'CSPE43', 'CSPE45', 'CSPE47', 'CSPC40', 'CSPE40', 'CSPE42', 'CSPE44', 'CSPE46', 'CSOE41', 'CSOE40', 'CSOE42', 'ECPC11', 'ECPC12', 'ECPC30', 'ECPC31', 'ECPC32', 'ECPC33', 'ECPC34', 'ECPC35', 'ECPC40', 'ECPC42', 'ECPC43', 'ECPE40', 'ECPE41', 'ECPE42', 'ECPE43', 'ECPC50', 'ECPC51', 'ECPC52', 'ECPC53', 'ECPE50', 'ECPE51', 'ECPE52', 'ECPE53', 'ECPE54', 'ECOE50', 'ECOE51', 'ECPC70', 'ECPC71', 'ECPC72', 'ECPE70', 'ECPE71', 'ECPE72', 'ECPE73', 'ECPE74', 'ECPE75', 'ECPE76', 'ECPE', 'ECPE78', 'ECOE70', 'ECOE71', 'ECOE72', 'ECPC80', 'ECPE80', 'ECPE81', 'ECPE82', 'ECPE83', 'ECPE84', 'ECPE85', 'ECPE86', 'ECPE87', 'ECPE88', 'ECOE80', 'ECOE81', 'ECLR30', 'ECLR31', 'ECLR32', 'ECLR33', 'ECLR40', 'ECLR41', 'ECLR42', 'ECLR43', 'ECLR50', 'ECLR51', 'ECLR52', 'ECLR70', 'ECLR71', 'EEIR', 'EEPC', 'EEPC12', 'EEPC21', 'EEPC22', 'EEPC24', 'EEPC25', 'EEPC26', 'EEPC27', 'EEPC28', 'EEPC29', 'EEPC31', 'EEPC33', 'EEPC35', 'EEPC40', 'EEPC41', 'EEPC43', 'EEPC45', 'EEPE21A', 'EEPE21B', 'EEPE21C', 'EEPE22A', 'EEPE22B', 'EEPE22C', 'EEPE31A', 'EEPE31B', 'EEPE31C', 'EEPE33A', 'EEPE33B', 'EEPE33C', 'EEPE41A', 'EEPE41B', 'EEEPE41C', 'EEPE43A', 'EEPE43B', 'EEPE43C', 'EEPE43D', 'EEPE40A', 'EEPE40B', 'EEPE40C', 'EEPE40D', 'EEPE42A', 'EEPE42B', 'EEPE42C', 'EEPE42D', 'EEPE44A', 'EEPE44B', 'EEPE44C', 'EELR12', 'EELR', 'EELR21', 'EELR25', 'EELR22', 'EELR24', 'EELR26', 'EELR28', 'EELR31', 'EELR33', 'EELR35', 'EELR43', 'EELR41', 'ITIR13', 'ITPC10', 'ITPC12', 'ITPC14', 'ITIR12', 'ITPC21', 'ITPC23', 'ITPC25', 'ITPC27', 'ITPC29', 'ITPC20', 'ITPC22', 'ITPC24', 'ITPC26', 'ITPE20', 'ITPE22', 'ITPE24', 'ITPE26', 'ITPE60', 'ITPE62', 'ITPE64', 'ITPC31', 'ITPC33', 'ITPC35', 'ITPC37', 'ITPE31', 'ITPE33', 'ITPE35', 'ITPE37', 'ITPE39', 'ITPE71', 'ITPE73', 'ITPE75', 'ITPE77', 'ITPE79', 'ITPC41', 'ITPC43', 'ITPC45', 'ITPE41', 'ITPE43', 'ITPE45', 'ITPE47', 'ITPC40', 'ITPE42', 'ITPE44', 'ITPE46', 'ITPE48', 'ITOE41', 'ITOE40', 'ITOE42', 'MEIR12', 'MEIR11', 'MEPC10', 'MEPC11', 'MEPC12', 'MELR10', 'MEPC13', 'MEPC14', 'MEPC15', 'MEPC16', 'MEPC17', 'MELR11', 'MELR12', 'MELR13', 'MEPC18', 'MEPC19', 'MEPC20', 'MEPC', 'MELR', 'MELR15', 'MELR16', 'MELR17', 'MEPE10', 'MEPE11', 'MEPE12', 'MEPE13', 'MEPE14', 'MEPE15', 'MEPC22', 'MEPC23', 'MEPC24', 'MEPC25', 'MELR18', 'MELR19', 'MELR20', 'MEPE16', 'MEPE17', 'MEPE18', 'MEPE19', 'MEPE20', 'MEPE21', 'MEPC26', 'MEPC27', 'MEPC28', 'MELR21', 'MEPE22', 'MEPE23', 'MEPE25', 'MEPE26', 'MEPE27', 'MEPE', 'MEPC29', 'MEPE29', 'MEPE30', 'MEPE31', 'MEPE32', 'MEPE33', 'MEPE37', 'MEPE39', 'MEPE41', 'MELR14', 'PHIR11', 'PHIR12A', 'PHIR12B', 'PHIR12C', 'PHIR12', 'PHOE10', 'PHOE11', 'PHOE', 'PHOE13', 'PHOE14', 'PHOE15', 'PHOE16', 'PRIR11', 'PRPC10', 'PRPC11', 'PRPC12', 'PRPC13', 'PRPC14', 'PRPC15', 'PRPC16', 'PRPC17', 'PRPC19', 'PRPL10', 'PRPL11', 'PRPL12', 'PRPL13', 'PRPC18', 'PRPC20', 'PRPC21', 'PRPL14', 'PRPL15', 'PRPL16', 'PRPE10', 'PRPE11', 'PRPE12', 'PRPE13', 'PRPE14', 'PRPE15', 'PRPC22', 'PRPC23', 'PRPC24', 'PRPC25', 'PRPL17', 'PRPL18', 'PRPE16', 'PRPE17', 'PRPE18', 'PRPE19', 'PRPE20', 'PRPE21', 'PRPC26', 'PRPC27', 'PRPC28', 'PRPL', 'PRPL20', 'PRPE23', 'PRPE24', 'PRPE', 'PRPE27', 'PRPE28', 'PRPE29', 'PRPE30', 'PRPC29', 'PRPE33', 'PRPE34', 'PRPE35', 'PRPE37', 'PRPE39', 'PRPE40', 'PRPE41', 'PRPE43', 'PRPE45']

pptmimeList = ["application/vnd.ms-powerpoint","application/vnd.openxmlformats-officedocument.presentationml.presentation"]

outfile = open("links.json","w")

for i in range(len(x.index)):
    
    ID = x.loc[i]["id"]
    name = x.loc[i]["name"]
    mime = x.loc[i]["mimeType"]
    tag = json.loads(x.loc[i]["tags"].replace("'",'"'))

    newEntry = [ID, name, mime, tag]
    newtag = []

    typicalAncestors = []
    for c in coursecodes:
        for t in tag:
            if c in t:
                typicalAncestors += [t]
                if "course:" + c not in newtag:
                    newtag.append("course:" + c)

    if "Reference Books" in tag:
        newtag.append("kind:book")
        typicalAncestors.append("Reference Books")
    elif "Lecture Notes" in tag or "Notes" in tag:
        newtag.append("kind:notes")
        typicalAncestors.append("Lecture Notes")
        typicalAncestors.append("Notes")
    
    if mime in pptmimeList:
        print(ID,name,mime)
        newtag.append("kind:lecture-ppt")
    try:
        tag = json.loads(tag + "\n")
    except:
        pass
    
    for t in tag:
        if t not in typicalAncestors and t:
            newtag.append("other:"+t)

    newEntry[-1] = newtag
    outfile.write(json.dumps(newEntry))
    outfile.write("\n")

outfile.close()
