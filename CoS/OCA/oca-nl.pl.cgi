#!/usr/bin/perl -w

use CGI qw(:standard);

# You might want to change these two lines:
my $appletargs = 'codebase="/users/johanw/CoS/OCA" code="OCA.class" width=550 height=250';
my $mainpage = "http://www.vulcan.homenet.home/users/johanw/CoS/OCA/";

my @questions = (
    "DUMMY",
    "1 Maakt u ondoordachte opmerkingen of uit u beschuldigingen waarvan u later spijt heeft?",
    "2 Blijft u betrekkelijk rustig wanneer anderen van streek raken?",
    "3 Zit u louter voor uw plezier te bladeren in spoorwegboekjes, gidsen of woordenboeken?",
    "4 Wanneer u gevraagd zou worden een beslissing te nemen, zou u zich dan laten beïnvloeden door het feit of u de betrokken persoon mag of niet mag?",
    "5 Wilt u 1, niet meer dan 2 of helemaal geen kinderen, ook al kunt u zich qua gezondheid en inkomen meer kinderen permitteren?",
    "6 Heeft u af en toe spiertrekkingen zonder dat daar een logische verklaring voor is?",
    "7 Geeft u er de voorkeur aan om in een positie te verkeren, waarbij besluitvorming niet tot uw verantwoordelijkheden behoort?",
    "8 Vinden anderen uw doen en laten onvoorspelbaar?",
    "9 Bent u van mening dat er voor de sociale zekerheid meer geld moet worden uitgetrokken?",
    "10 Stelt u veel belang in anderen?",
    "11 Vindt u uw stem eerder monotoon dan levendig?",
    "12 Laat u de ander gewoonlijk het gesprek beginnen?",
    "13 Bent u gauw geïnteresseerd in de conversatie tussen anderen?",
    "14 Zou het idee dat u wild, kleine dieren of vissen pijn zou doen, u ervan weerhouden om te gaan jagen of vissen?",
    "15 Bent u vaak impulsief in uw gedrag?",
    "16 Spreekt u langzaam?",
    "17 Maakt u zich vaak zorgen over de noodzaak uw gezondheid te moeten beschermen?",
    "18 Krijgt u van een onverwachte actie spiertrekkingen?",
    "19 Houdt u gewoonlijk rekening met de gevoelens van uw employes, familieleden of leerlingen bij wat u van hen verlangt?",
    "20 Bent u van mening dat u voor de vuist weg een geldig oordeel zou kunnen geven?",
    "21 Maakt u zich nog steeds zorgen over wat u in het verleden niet is gelukt?",
    "22 Merkt u dat u gedurende een periode van een paar dagen extra actief bent?",
    "23 Neemt u het anderen kwalijk als zij u proberen te vertellen wat u moet doen?",
    "24 Vindt u het gewoonlijk moeilijk om eerlijk voor iets uit te komen en schuld te bekennen?",
    "25 Heeft u liever een kleine kring van intieme vrienden dan een groot aantal vrienden en kennissen?",
    "26 Is uw leven een constante strijd om het bestaan?",
    "27 Zingt of fluit u vaak gewoon voor uw plezier?",
    "28 Vinden uw vrienden u hartelijk?",
    "29 Zou u liever orders geven dan krijgen?",
    "30 Houdt u ervan om anderen te vertellen over de laatste schokkende gedragingen van de mensen waarmee u omgaat?",
    "31 Kunt u instemmen met strenge discipline?",
    "32 Zou de gedachte aan helemaal opnieuw te moeten beginnen u ernstig zorgen baren?",
    "33 Doet u uw best anderen in een goede stemming te brengen en aan het lachen te maken?",
    "34 Vindt u het gemakkelijk om uw gevoelens tot uitdrukking te brengen?",
    "35 Weerhoudt u zich erover te klagen als de ander te laat is voor een afspraak?",
    "36 Wordt u soms door anderen als spelbreker gezien?",
    "37 Vindt u dat er mensen zijn die u beslist onvriendelijk bejegenen en u tegenwerken?",
    "38 Zou u toegeven dat u ongelijk had alleen om de vrede te bewaren?",
    "39 Kent u maar een paar mensen die u echt heel graag mag?",
    "40 Bent u zelden gelukkig, tenzij u daarvoor een bijzondere reden heeft?",
    "41 Praat u met Jan en alleman op feestjes en partijtjes?",
    "42 Treft u redelijke voorzorgsmaatregelen om ongelukken te voorkomen?",
    "43 Maakt alleen de gedachte al om mensen te moeten toespreken, u zenuwachtig?",
    "44 Als u in een winkel een artikel ziet waarop heel duidelijk een te lage prijs staat aangegeven, zou u dan toch proberen het tegen die prijs te krijgen?",
    "45 Heeft u vaak het gevoel dat mensen naar u kijken of achter uw rug over u praten?",
    "46 Raakt u altijd in moeilijkheden verzeild?",
    "47 Heeft u een bepaalde angst of haat?",
    "48 Bent u liever toeschouwer dan deelnemer in een actieve sport?",
    "49 Vindt u het gemakkelijk om onpartijdig te zijn?",
    "50 Heeft u een bepaalde, vaste norm van beleefd gedrag ten opzichte van familieleden?",
    "51 Kunt u op feestjes en partijtjes de bal aan het rollen brengen?",
    "52 Zou u op afbetaling kopen in de hoop dat u bij kunt blijven met betalen?",
    "53 Krijgt u een na-reactie wanneer er iets onverwachts gebeurd is, zoals een ongeluk of een storend voorval?",
    "54 Houdt u eerder rekening met het heil van alle betrokkenen dan met uw eigen persoonlijke voordelen?",
    "55 Krijgt u, bij het luisteren naar een spreker, soms het gevoel dat hij het alleen over u heeft?",
    "56 Wordt u in uw concentratie zelden gestoord door geluiden om u heen?",
    "57 Bent u gewoonlijk helemaal op de hoogte van de dagelijkse gebeurtenissen?",
    "58 Bent u er zeker van dat u de een of andere taak kunt plannen en werken aan de voltooiing ervan binnen een tijdsbestek van 6 maanden?",
    "59 Vindt u dat de hedendaagse ontwikkeling naar een systeem van gevangenissen zonder tralies gedoemd is tot mislukking?",
    "60 Bent u geneigd zich nergens om te bekommeren?",
    "61 Komt het leven u soms als in een droom voor, waarin alles onwerkelijk schijnt?",
    "62 Herstelt u snel van de gevolgen van slecht nieuws?",
    "63 Probeert u, wanneer u kritiek levert, tezelfder tijd aan te moedigen?",
    "64 Vinden anderen u meestal koud?",
    "65 Zijn uw meningen niet belangrijk genoeg om aan anderen te vertellen?",
    "66 Bent u zo zelfverzekerd dat anderen zich daar soms aan ergeren?",
    "67 Houdt u angstvallig bij welke van uw bezittingen u aan uw vrienden heeft uitgeleend?",
    "68 Geniet u van activiteiten die u zelf verkozen heeft?",
    "69 Maakt gevoelige muziek een enorme indruk op u?",
    "70 Als iemand in zijn betrekkingen tot u in een enkel opzicht uw rivaal of tegenstander is, veroordeelt u hem dan helemaal?",
    "71 Zit u vaak na te denken over doodgaan, ziekte, pijn of verdriet?",
    "72 Wekt de gedachte aan je gezicht te kunnen verliezen onrust bij u op?",
    "73 Verzamelt u altijd dingen die wel van pas kunnen komen?",
    "74 Zou u de gebreken bekritiseren en de slechte punten aanwijzen in iemand's karakter of handarbeid?",
    "75 Geeft u openlijk blijk van waardering voor mooie dingen?",
    "76 Geeft u soms dingen weg die eigenlijk niet van u zijn?",
    "77 Groet u mensen uitbundig?",
    "78 Peinst u vaak over vroegere tegenslagen?",
    "79 Vindt men soms dat u uw handelingen of meningen probeert door te drukken?",
    "80 Accepteert u kritiek gemakkelijk en zonder wrok?",
    "81 Wordt u gewoonlijk niet gestoord door geluiden in de omgeving als u probeert te rusten?",
    "82 Wordt u gemakkelijk jaloers?",
    "83 Bent u geneigd dingen uit te stellen tot het te laat is?",
    "84 Houdt u zich liever aan de wensen van anderen in plaats van te proberen uw eigen mening door te drukken?",
    "85 Kunt u zich er gemakkelijk toe brengen om met een project aan de slag te gaan?",
    "86 Bent u een nagelbijter of een potloodknabbelaar?",
    "87 Schroeft u uw emoties op gewoon om meer effect te creëren?",
    "88 Als we een ander land binnenvielen, zou u begrip kunnen opbrengen voor principiële dienstweigeraars van uw eigen land?",
    "89 Zijn er wat uzelf betreft dingen waarover u zich gemakkelijk kunt opwinden?",
    "90 Heeft u maar weinig interesses en activiteiten die u zelf heeft gekozen?",
    "91 Krijgt u wel eens een enkele gedachte die dagenlang blijft rondhangen?",
    "92 Bent u een langzame eter?",
    "93 Kunt u een stabiliserende invloed zijn wanneer anderen in paniek raken?",
    "94 Zou u stoppen om vast te stellen of iemand hulp nodig had, zelfs als men u er niet direct om had gevraagd?",
    "95 Bent u bevooroordeeld ten gunste van uw school, universiteit, club of team enz.?",
    "96 Betaalt u uw schulden en houdt u zich aan uw afspraken als het mogelijk is?",
    "97 Slaapt u goed?",
    "98 Zou u een lichamelijke straf toedienen aan een kind van tien jaar oud, dat u weigerde te gehoorzamen?",
    "99 Heeft u het liefst een passieve rol in een club of organisatie waar u bij hoort?",
    "100 Bent u logisch en wetenschappelijk in uw denken?",
    "101 Heeft de jeugd van nu meer mogelijkheden dan de jeugd van een generatie geleden?",
    "102 Gooit u dingen weg om dan later tot de conclusie te komen dat u ze toch nodig zal hebben?",
    "103 Zou u gemakkelijk opgeven op een ingeslagen koers als deze u veel ongemak bezorgde?",
    "104 Zijn er maar enkele onderwerpen waarvoor u enthousiasme kunt opbrengen?",
    "105 Vindt u de handelingen van anderen zelden verdacht?",
    "106 Vraagt u zich soms wel eens af of er iemand is die echt om u geeft?",
    "107 Wijst u verantwoordelijkheid af, omdat u twijfelt of u deze aankunt?",
    "108 Voelt u wel eens dat u een nieuwtje of de een of andere onbenulligheid gewoon moet door vertellen?",
    "109 Heeft u de neiging een rechtvaardige klacht te overdrijven?",
    "110 Is uw gezichtsuitdrukking eerder gevarieerd dan strak?",
    "111 Moet u een eenmaal verkondigde mening gewoonlijk rechtvaardigen?",
    "112 Bewondert u schoonheid in anderen openlijk en oprecht?",
    "113 Zou het u beslist inspanning kosten om over het onderwerp zelfmoord na te denken?",
    "114 Zou u zichzelf energiek noemen in uw houding ten opzichte van het leven?",
    "115 Zou een meningsverschil uw algemene relatie met een ander beïnvloeden?",
    "116 Baart een geringe tekortkoming van uzelf u zelden zorgen?",
    "117 Vindt u soms dat u teveel praat?",
    "118 Glimlacht u veel?",
    "119 Bent u gauw tevreden?",
    "120 Zou u, ondanks rechtstreekse tegenstand, toch eerder trachten uw zin te krijgen dan toe te geven?",
    "121 Als de afstand niet te groot was, zou u toch liever per auto gaan dan te voet?",
    "122 Raakt u wel eens van streek door het geluid van de wind of een huis dat kraakt?",
    "123 Wordt uw mening beïnvloed doordat u de dingen bekijkt vanuit het standpunt van uw ervaring, beroep of opleiding?",
    "124 Maakt u vaak tactloze opmerkingen?",
    "125 Wantrouwt u mensen die u geld te leen vragen?",
    "126 Speelt eigenbelang een overwegende rol in uw besluitvorming?",
    "127 Kunt u heel enthousiast worden over een simpel niemendalletje?",
    "128 Gaat u vaak tot actie over ook al zegt uw gezond verstand het niet te doen?",
    "129 Bent u voor rassenscheiding en klassenstelsels?",
    "130 Bent u zich bewust van bepaalde lichamelijke hebbelijkheden zoals trekken aan uw haren, neus, oren en dergelijke?",
    "131 Kunt u zich snel aanpassen en gebruik maken van nieuwe omstandigheden en situaties, ook al zijn ze moeilijk?",
    "132 Zijn er van die geluiden die u door merg en been gaan?",
    "133 Kunt u, als u wilt, het standpunt van een ander zien?",
    "134 Gaat u naar bed wanneer het u zint in plaats van precies op tijd?",
    "135 Maken de kleine zwakheden van anderen u ongeduldig?",
    "136 Irriteren anderen u?",
    "137 Bent u minder spraakzaam dan de mensen waarmee u omgaat?",
    "138 Voert u taken gewoonlijk prompt en systematisch uit?",
    "139 Zou u een medereiziger eerder zelf helpen in plaats van dat aan de officiële instanties over te laten?",
    "140 Stemt u altijd op dezelfde partij in plaats van de kandidaten en partijprogramma's te bestuderen?",
    "141 Blijft u vaak stilstaan bij de vroegere ziektes of pijnlijke ervaringen die u heeft gehad?",
    "142 Voelt u zich gauw slecht op uw gemak in een wanordelijke omgeving?",
    "143 Levert u gewoonlijk kritiek op een film of show die u ziet of een boek dat u leest?",
    "144 Kunt u, wanneer u een grappig voorval navertelt, de manier van doen of het dialect in het oorspronkelijke voorval gemakkelijk nadoen?",
    "145 Zijn uw ideeën over onderwerpen, waarin u geen expert bent, belangrijk genoeg om aan anderen te vertellen?",
    "146 Heeft u de neiging om een wanorde in het huis van een ander op te ruimen?",
    "147 Kunt u gemakkelijk een nederlaag accepteren zonder uw teleurstelling te moeten wegslikken?",
    "148 Voelt u zich vaak teneergeslagen?",
    "149 Voelt u zich in de buurt van kinderen ooit slecht op uw gemak?",
    "150 Als u iets niet kunt doen, raakt u dan ontmoedigd in plaats van een andere activiteit of ander systeem te vinden?",
    "151 Is het voor u soms volslagen onmogelijk om mee te doen?",
    "152 Geeft u zelden uiting van uw grieven?",
    "153 Werkt u bij vlagen, zodat u bij tijden haast niets doet, afgewisseld met korte perioden van koortsachtige activiteit?",
    "154 Maakt u zich zorgen over het aantal onafgemaakte karweitjes dat u om handen heeft?",
    "155 Vinden mensen het plezierig in uw gezelschap te zijn?",
    "156 Zou u iemand de laatste twee woorden in een kruiswoordpuzzel kunnen laten afmaken zonder u ermee te bemoeien?",
    "157 Neemt u bij mensen meestal hun goede punten in acht en spreekt u maar zelden geringschattend over hen?",
    "158 Heeft u een gulle glimlach en lacht u spontaan?",
    "159 Bent u beslist en nadrukkelijk in uw spreken en manier van doen?",
    "160 Als u uitbundig bent, uit u dat dan alleen tegenover goede vrienden?",
    "161 Zijn uw intellectuele en andere interesses zo belangrijk dat er voor iets anders maar weinig tijd over blijft?",
    "162 Zou u in de omgeving waar u woont iets nieuws willen beginnen?",
    "163 Zou u de noodzakelijke handelingen verrichten om een dier dood te maken om het uit zijn lijden te verlossen?",
    "164 Kunt u zich gemakkelijk ontspannen?",
    "165 Heeft u weinig spijt van tegenslagen en mislukkingen uit het verleden?",
    "166 Geeft alleen de gedachte al aan angstige of angstaanjagende dingen u een lichamelijke reactie?",
    "167 Kunt u uw oordeel vertrouwen in een emotionele situatie waarbij u betrokken bent?",
    "168 Zou iemand anders kunnen vinden dat u echt actief bent?",
    "169 Vindt u het moeilijk om een begin te maken met iets dat gedaan moet worden?",
    "170 Bent u tegen het systeem van voorwaardelijke in vrijheidstelling voor misdadigers?",
    "171 Brengt u veel tijd door met u nodeloos zorgen te maken?",
    "172 Vindt u het bij een meningsverschil moeilijk te begrijpen hoe de ander uw kant niet kan zien en het daarom niet met u eens is?",
    "173 Kunt u de dagelijkse zorgen van het bestaan redelijk goed aan?",
    "174 Bent u gewoonlijk eerlijk tegenover anderen?",
    "175 Neemt u liever een afwachtende houding aan in plaats van het heft in eigen handen te nemen?",
    "176 Geeft u meer geld uit dan uw inkomen u toelaat?",
    "177 Kunt u zonder u te veel zorgen te maken een weloverwogen risico nemen?",
    "178 Als u betrokken was bij een niet-ernstig auto-ongeluk, zou u er dan echt voor zorgen dat alle eventuele schade die u had veroorzaakt, werd vergoed?",
    "179 Spelen anderen de baas over u?",
    "180 Ziet u bij uw vrienden door de vingers, wat u bij anderen wellicht strenger zou beoordelen?",
    "181 Denkt u vaak na over uw eigen minderwaardigheid?",
    "182 Bekritiseert men u tegen anderen?",
    "183 Vindt u een hartelijke begroeting, zoals een kus, omhelzing of slaan op uw schouder onprettig als dat in het openbaar gebeurt?",
    "184 Laat u regelmatig na de dingen te doen die u zelf wilt doen, omdat u rekening houdt met de verlangens van andere mensen?",
    "185 Bent u soms overtuigd van de juistheid van uw mening over een onderwerp, ook al bent u geen deskundige?",
    "186 Merkt u vaak dat u alle kanten tegelijk opgaat?",
    "187 Heeft u de indruk dat uw kennissen een hogere dunk van uw bekwaamheden hebben dan u?",
    "188 Is alleen de gedachte al aan de dood of zelfs maar iets wat u aan de dood doet denken, afschuwwekkend voor u?",
    "189 Wanneer u een ruzie heeft bijgelegd, blijft u dan nog en tijdje een slecht humeur houden?",
    "190 Heeft u een vriendelijke stem, houding en gezichtsuitdrukking?",
    "191 Vindt u het leven nogal vaag en onwerkelijk?",
    "192 Voelt u zich vaak van streek over het lot van oorlogsslachtoffers en politieke vluchtelingen?",
    "193 Kloppen kennissen zomaar bij u aan voor hulp of advies bij hun persoonlijke moeilijkheden?",
    "194 Als u iets bent kwijt geraakt, krijgt u het idee dat iemand het heeft gestolen of weggemaakt?",
    "195 Als u dacht dat iemand u en uw daden wantrouwde, zou u hem er dan over aanspreken in plaats van hem het zelf te laten uitzoeken?",
    "196 Denkt u wel eens dat u uw leeftijd tegen heeft (te jong of te oud)?",
    "197 Heeft u vlagen van droefheid en neerslachtigheid zonder dat er een aantoonbare reden voor bestaat?",
    "198 Moppert u vaak over de omstandigheden waaronder u moet leven?",
    "199 Heeft u de neiging om uw gevoelens te verbergen?",
    "200 Bent u van mening dat u veel hartelijke vrienden heeft?",
);

# These are the scores each question will give.
# ["Trait (A-J)", Score for "+", Score for "M", Score for "-"]
my @Scores = (
    ["Z",0,0,0], ### Dummy
    ["A",2,4,6], ["C",6,5,3], ["E",6,4,3], ["G",3,4,6], ["I",4,4,5], #   1-  5
    ["C",3,3,6], ["E",3,4,5], ["A",2,4,5], ["I",3,4,4], ["G",5,4,4], #   6- 10
    ["C",3,4,5], ["E",2,4,6], ["G",5,4,3], ["I",2,4,5], ["A",3,3,6], #  11- 15
    ["E",3,4,4], ["A",2,4,5], ["C",2,6,6], ["I",5,3,3], ["G",5,5,3], #  16- 20
    ["B",2,3,6], ["D",1,5,6], ["F",5,4,3], ["H",3,5,6], ["J",3,1,5], #  21- 25
    ["D",2,3,6], ["B",5,4,4], ["J",6,2,2], ["F",6,3,3], ["H",3,4,6], #  26- 30
    ["F",5,4,4], ["D",2,4,6], ["B",6,5,3], ["J",6,3,3], ["H",5,5,2], #  31- 35
    ["B",3,5,6], ["H",3,4,6], ["F",4,4,5], ["J",3,4,5], ["D",2,3,5], #  36- 40
    ["E",6,4,4], ["A",5,3,3], ["C",4,4,5], ["I",2,3,6], ["G",3,4,5], #  41- 45
    ["A",3,3,5], ["C",2,5,6], ["E",3,4,5], ["G",6,4,4], ["I",4,4,3], #  46- 50
    ["E",5,4,2], ["A",3,4,4], ["C",3,4,6], ["I",6,3,3], ["G",2,5,6], #  51- 55
    ["C",5,3,3], ["E",5,4,4], ["A",6,3,3], ["I",1,3,5], ["G",2,5,6], #  56- 60
    ["D",2,4,6], ["B",5,4,4], ["H",5,4,4], ["J",2,2,6], ["F",4,4,5], #  61- 65
    ["F",6,4,3], ["D",2,4,5], ["B",6,4,3], ["J",6,3,3], ["H",4,4,5], #  66- 70
    ["B",3,5,6], ["F",3,4,4], ["D",2,4,5], ["H",2,4,6], ["J",5,3,3], #  71- 75
    ["D",1,3,6], ["J",6,2,2], ["B",2,5,6], ["F",5,4,3], ["H",6,3,3], #  76- 80
    ["C",6,3,3], ["G",3,4,6], ["A",3,3,6], ["I",6,3,2], ["E",6,3,3], #  81- 85
    ["C",2,4,6], ["A",3,3,5], ["I",5,4,3], ["G",2,5,6], ["E",3,3,5], #  86- 90
    ["C",3,4,6], ["E",3,4,4], ["A",5,3,3], ["I",5,4,4], ["G",3,4,5], #  91- 95
    ["A",6,4,2], ["C",5,5,3], ["I",4,4,5], ["E",2,4,5], ["G",4,3,1], #  96-100
    ["B",5,4,4], ["D",2,3,5], ["F",4,4,6], ["J",2,3,6], ["H",6,4,3], # 101-105
    ["B",2,3,7], ["F",2,3,6], ["D",3,4,5], ["H",3,4,5], ["J",5,4,4], # 106-110
    ["D",2,4,5], ["J",6,2,2], ["B",6,4,3], ["F",6,4,3], ["H",3,4,6], # 111-115
    ["B",6,4,3], ["D",3,4,5], ["J",7,2,2], ["H",5,4,3], ["F",5,4,3], # 116-120
    ["A",2,3,6], ["E",4,4,5], ["C",3,4,6], ["G",5,4,3], ["I",1,3,4], # 121-125
    ["G",4,4,6], ["E",5,4,4], ["A",3,4,6], ["I",2,5,6], ["C",3,5,6], # 126-130
    ["A",5,3,2], ["C",2,4,6], ["G",6,4,3], ["E",4,4,3], ["I",2,4,5], # 131-135
    ["C",3,5,5], ["E",3,3,6], ["A",5,3,3], ["I",5,4,4], ["G",2,5,6], # 136-140
    ["B",2,5,6], ["D",1,3,5], ["H",2,4,6], ["J",5,4,3], ["F",5,5,3], # 141-145
    ["D",1,3,5], ["F",6,4,4], ["B",3,4,6], ["J",3,5,5], ["H",2,5,6], # 146-150
    ["B",2,5,6], ["H",6,5,3], ["D",2,4,6], ["F",3,3,5], ["J",7,1,1], # 151-155
    ["D",6,4,2], ["H",7,5,2], ["B",5,5,3], ["F",5,4,2], ["J",2,2,6], # 156-160
    ["G",2,5,6], ["E",6,4,3], ["I",5,4,4], ["C",5,5,2], ["A",6,3,3], # 161-165
    ["C",3,3,6], ["G",6,4,2], ["E",6,4,3], ["A",2,3,6], ["I",3,4,5], # 166-170
    ["C",3,3,6], ["G",3,4,6], ["A",6,3,2], ["I",5,4,3], ["E",0,1,5], # 171-175
    ["A",2,2,6], ["C",6,4,4], ["I",5,3,3], ["E",0,1,5], ["G",3,5,6], # 176-180
    ["B",3,3,6], ["H",3,4,6], ["J",2,4,6], ["D",3,4,6], ["F",6,6,3], # 181-185
    ["D",1,3,5], ["F",3,3,5], ["B",2,2,6], ["H",3,5,5], ["J",6,2,2], # 186-190
    ["D",1,4,5], ["B",2,4,6], ["J",5,4,3], ["H",4,5,6], ["F",6,4,2], # 191-195
    ["B",2,5,6], ["D",2,4,5], ["H",2,5,6], ["F",0,3,5], ["J",5,3,3]  # 196-200
);

my @ScoreWeights = (

        ### Trait A (Unstable -> Stable)

        # Girls (14-18 years)
        [],
        # Boys (14-18 years)
        [],
        # Adult women (18+ years)
        [ 50,
        -100, -100, -100, -100, -100, -100, -100, -100, -100, -100,  #  50- 59
         -99,  -99,  -99,  -98,  -97,  -96,  -95,  -94,  -92,  -90,  #  60- 69
         -88,  -84,  -78,  -74,  -70,  -64,  -60,  -54,  -50,  -44,  #  70- 79
         -38,  -28,  -26,  -20,  -12,   -4,    4,   12,   20,   28,  #  80- 89
          36,   42,   48,   54,   58,   62,   66,   70,   72,   76,  #  90- 99
          78,   80,   84,   86,   88,   90,   92,   94,   96,   98,  # 100-109
          99                                                         # 110
        ],
        # Adult men (18+ years)
        [ 50,
        -100, -100, -100, -100, -100, -100, -100, -100, -100, -100,  #  50- 59
        -100, -100, -100, -100, -100, -100, -100, -100,  -99,  -98,  #  60- 69
         -98,  -97,  -96,  -94,  -92,  -88,  -84,  -82,  -80,  -76,  #  70- 79
         -70,  -64,  -58,  -52,  -46,  -40,  -34,  -28,  -20,  -14,  #  80- 89
          -6,    0,    8,   14,   22,   28,   36,   42,   50,   56,  #  90- 99
          62,   68,   74,   78,   82,   90,   92,   94,   95,   96,  # 100-109
          98                                                         # 110
        ],

        ### Trait B (Depressed -> Happy)

        # Girls (14-18 years)
        [],
        # Boys (14-18 years)
        [],
        # Adult women (18+ years)
        [ 55,
                                      -100, -100, -100, -100,  -99,  #  55- 59
         -99,  -98,  -97,  -97,  -96,  -96,  -95,  -95,  -94,  -94,  #  60- 69
         -93,  -93,  -92,  -92,  -91,  -90,  -88,  -86,  -82,  -80,  #  70- 79
         -76,  -72,  -68,  -66,  -62,  -58,  -54,  -50,  -46,  -44,  #  80- 89
         -40,  -38,  -32,  -28,  -22,  -16,  -10,   -4,    2,   10,  #  90- 99
          20,   30,   38,   46,   54,   62,   68,   74,   80,   86,  # 100-109
          92,   98,  100,  100,  100,  100,  100,  100               # 110-117
        ],
        # Adult men (18+ years)
        [ 55,
                                      -100, -100, -100, -100, -100,  #  55- 59
        -100, -100, -100, -100, -100, -100, -100, -100, -100, -100,  #  60- 69
        -100, -100, -100, -100, -100, -100,  -99,  -98,  -97,  -96,  #  70- 79
         -95,  -95,  -94,  -93,  -92,  -90,  -88,  -86,  -82,  -80,  #  80- 89
         -78,  -70,  -66,  -60,  -55,  -50,  -44,  -40,  -34,  -28,  #  90- 99
         -24,  -18,  -12,   -4,    2,    8,   16,   24,   32,   40,  # 100-109
          48,   56,   64,   72,   78,   84,   88,   92               # 110-117
        ],

        ### Trait C (Nervous -> Composed)

        # Girls (14-18 years)
        [],
        # Boys (14-18 years)
        [],
        # Adult women (18+ years)
        [ 57,
                                                  -100, -100, -100,  #  57- 59
         -99,  -99,  -98,  -98,  -97,  -97,  -96,  -96,  -95,  -94,  #  60- 69
         -93,  -91,  -91,  -90,  -86,  -82,  -76,  -70,  -66,  -60,  #  70- 79
         -54,  -48,  -42,  -36,  -30,  -26,  -20,  -14,   -9,   -2,  #  80- 89
           6,    8,   18,   24,   30,   38,   44,   50,   58,   64,  #  90- 99
          70,   76,   80,   84,   88,   92,   94,   96,   98,  100,  # 100-109
         100,  100,  100,  100,  100                                 # 110-114
        ],
        # Adult men (18+ years)
        [ 57,
                                                  -100, -100, -100,  #  57- 59
        -100, -100, -100, -100, -100, -100,  -99,  -99,  -99,  -99,  #  60- 69
         -99,  -99,  -99,  -99,  -99,  -99,  -98,  -98,  -98,  -98,  #  70- 79
         -97,  -96,  -94,  -92,  -90,  -86,  -82,  -76,  -70,  -63,  #  80- 89
         -58,  -52,  -46,  -40,  -34,  -28,  -22,  -16,  -10,   -4,  #  90- 99
           2,    8,   14,   20,   28,   34,   40,   48,   54,   60,  # 100-109
          68,   74,   82,   88,   94                                 # 110-114
        ],

        ### Trait D (Undependable -> Personable)

        # Girls (14-18 years)
        [],
        # Boys (14-18 years)
        [],
        # Adult women (18+ years)
        [ 37,
                                                  -100,  -99,  -98,  #  37- 39
         -97,  -96,  -95,  -94,  -93,  -92,  -90,  -86,  -82,  -80,  #  40- 49
         -76,  -74,  -70,  -64,  -62,  -60,  -56,  -52,  -50,  -48,  #  50- 59
         -42,  -36,  -30,  -28,  -24,  -20,  -16,  -12,  -10,   -8,  #  60- 69
          -6,   -2,    2,    6,   10,   14,   20,   24,   28,   32,  #  70- 79
          34,   36,   38,   40,   42,   44,   46,   58,   50,   52,  #  80- 89
          54,   58,   62,   66,   68,   70,   76,   80,   85,   88,  #  90- 99
          90,   92,   95,   96,   97,   97,   98,   99,  100         # 100-108
        ],
        # Adult men (18+ years)
        [ 37,
                                                  -100, -100,  -99,  #  37- 39
         -98,  -97,  -96,  -95,  -94,  -93,  -92,  -90,  -86,  -82,  #  40- 49
         -76,  -76,  -70,  -64,  -62,  -60,  -56,  -52,  -50,  -48,  #  50- 59
         -42,  -36,  -30,  -28,  -24,  -20,  -16,  -12,  -10,   -8,  #  60- 69
          -6,   -2,    2,    8,   14,   20,   28,   30,   32,   34,  #  70- 79
          36,   38,   40,   42,   44,   46,   48,   50,   52,   54,  #  80- 89
          58,   62,   66,   68,   70,   76,   80,   85,   88,   90,  #  90- 99
          92,   95,   96,   98,   98,   98,   98,   98,   98         # 100-108
        ],

        ### Trait E (Reactively Retarded -> Active)

        # Girls (14-18 years)
        [],
        # Boys (14-18 years)
        [],
        # Adult women (18+ years)
        [ 54,
                                -100,  -99,  -98,  -97,  -96,  -94,  #  54- 59
         -92,  -90,  -86,  -82,  -78,  -74,  -66,  -58,  -48,  -38,  #  60- 69
         -26,  -12,    2,    4,    8,   12,   16,   20,   24,   28,  #  70- 79
          30,   34,   38,   42,   46,   50,   54,   58,   62,   66,  #  80- 89
          70,   72,   76,   80,   84,   88,   90,   92,   94,   96,  #  90- 99
          97,   97,   98,   99,   99,  100,  100,  100,  100         # 100-108
        ],
        # Adult men (18+ years)
        [ 54,
                                 -99,  -98,  -94,  -92,  -90,  -82,  #  54- 59
         -76,  -70,  -62,  -56,  -50,  -46,  -40,  -36,  -30,  -24,  #  60- 69
         -18,  -12,   -6,   -2,    4,    8,   12,   16,   20,   24,  #  70- 79
          28,   32,   36,   40,   44,   46,   48,   50,   54,   58,  #  80- 89
          62,   66,   70,   72,   76,   80,   84,   88,   90,   93,  #  90- 99
          94,   97,   98,   99,  100                                 # 100-104
        ],

        ### Trait F (Inhibited -> Capable)

        # Girls (14-18 years)
        [],
        # Boys (14-18 years)
        [],
        # Adult women (18+ years)
        [ 58,
                                                        -100,  -99,  #  58- 59
         -98,  -97,  -92,  -86,  -78,  -68,  -58,  -48,  -36,  -22,  #  60- 69
         -10,    3,    6,    9,   12,   15,   18,   21,   24,   27,  #  70- 79
          30,   33,   36,   39,   42,   45,   48,   51,   54,   57,  #  80- 89
          61,   64,   67,   70,   72,   75,   78,   81,   84,   87,  #  90- 99
          90,   92,   94,   96,   98,   98,   99,  100,  100         # 100-108
        ],
        # Adult men (18+ years)
        [ 58,
                                                        -100,  -99,  #  58- 59
         -98,  -97,  -96,  -95,  -94,  -90,  -85,  -80,  -72,  -64,  #  60- 69
         -58,  -50,  -40,  -30,  -20,  -12,   -2,    4,    8,   12,  #  70- 79
          16,   20,   24,   26,   32,   36,   40,   44,   48,   52,  #  80- 89
          56,   60,   70,   74,   78,   82,   86,   88,   90,   91,  #  90- 99
          92,   93,   94,   95,   96,   97,   98,   99,  100         # 100-108
        ],

        ### Trait G (Irresponsible -> Responsible)

        # Girls (14-18 years)
        [],
        # Boys (14-18 years)
        [],
        # Adult women (18+ years)
        [ 55,
                                      -100, -100, -100, -100, -100,  #  58- 59
        -100, -100,  -99,  -99,  -99,  -99,  -99,  -99,  -99,  -98,  #  60- 69
         -98,  -98,  -97,  -96,  -96,  -95,  -94,  -93,  -92,  -91,  #  70- 79
         -90,  -88,  -87,  -84,  -80,  -78,  -72,  -68,  -64,  -58,  #  80- 89
         -52,  -44,  -38,  -28,  -18,  -14,   -8,    0,   10,   20,  #  90- 99
          30,   42,   54,   66,   78,   80,   82,   86,   88,   90,  # 100-109
          98,   99,  100                                             # 110-112
        ],
        # Adult men (18+ years)
        [ 55,
                                      -100, -100, -100, -100, -100,  #  58- 59
        -100, -100, -100,  -99,  -99,  -99,  -99,  -99,  -99,  -99,  #  60- 69
         -99,  -98,  -98,  -96,  -94,  -92,  -92,  -90,  -88,  -88,  #  70- 79
         -86,  -84,  -82,  -80,  -76,  -72,  -66,  -62,  -56,  -52,  #  80- 89
         -46,  -40,  -32,  -26,  -18,  -12,   -4,    4,   12,   16,  #  90- 99
          20,   28,   36,   46,   56,   66,   74,   82,   88,   92,  # 100-109
          94,   96,   99                                             # 110-112
        ],

        ### Trait H (Capacity for Error -> Logical Reasoning)

        # Girls (14-18 years)
        [],
        # Boys (14-18 years)
        [],
        # Adult women (18+ years)
        [ 55,
                                      -100, -100, -100, -100, -100,  #  55- 59
        -100, -100, -100, -100,  -99,  -99,  -98,  -97,  -96,  -95,  #  60- 69
         -94,  -93,  -92,  -91,  -90,  -89,  -88,  -87,  -86,  -85,  #  70- 79
         -84,  -83,  -80,  -76,  -74,  -70,  -66,  -62,  -58,  -56,  #  80- 89
         -52,  -46,  -42,  -36,  -30,  -22,  -12,  -10,   -8,   -6,  #  90- 99
          -4,   -2,    0,    6,   16,   24,   34,   42,   50,   58,  # 100-109
          64,   70,   76,   80,   86,   90                           # 110-115
        ],
        # Adult men (18+ years)
        [ 55,
                                      -100, -100, -100, -100, -100,  #  55- 59
        -100, -100, -100,  -99,  -98,  -98,  -97,  -96,  -96,  -96,  #  60- 69
         -95,  -94,  -93,  -92,  -91,  -90,  -90,  -90,  -89,  -88,  #  70- 79
         -87,  -86,  -84,  -80,  -78,  -76,  -74,  -70,  -66,  -62,  #  80- 89
         -58,  -54,  -50,  -46,  -42,  -36,  -32,  -28,  -24,  -18,  #  90- 99
         -14,  -10,   -4,    2,   16,   28,   36,   40,   48,   56,  # 100-109
          64,   72,   78,   84,   90,  100                           # 110-115
        ],

        ### Trait I (Lack of Accord -> Appreciative)

        # Girls (14-18 years)
        [],
        # Boys (14-18 years)
        [],
        # Adult women (18+ years)
        [ 55,
                                      -100, -100, -100, -100, -100,  #  55- 59
        -100, -100, -100, -100,  -99,  -99,  -99,  -99,  -98,  -98,  #  61- 69
         -98,  -97,  -97,  -96,  -96,  -95,  -92,  -90,  -86,  -80,  #  70- 79
         -70,  -62,  -50,  -40,  -28,  -14,   -2,   10,   12,   22,  #  80- 89
          34,   46,   56,   64,   72,   80,   86,   92,   95,   98,  #  90- 99
          99,  100                                                   # 100-101
        ],
        # Adult men (18+ years)
        [ 55,
                                      -100, -100, -100, -100, -100,  #  55- 59
        -100, -100, -100, -100,  -99,  -99,  -99,  -99,  -98,  -98,  #  61- 69
         -97,  -97,  -96,  -96,  -95,  -92,  -90,  -86,  -80,  -76,  #  70- 79
         -70,  -60,  -56,  -46,  -34,  -22,  -10,    2,   18,   32,  #  80- 89
          46,   60,   72,   80,   82,   86,   90,   96,   97,   98,  #  90- 99
          99,  100                                                   # 100-101
        ],

        ### Trait J (Withdrawn -> Comm. level)

        # Girls (14-18 years)
        [],
        # Boys (14-18 years)
        [],
        # Adult women (18+ years)
        [ 48,
                                                        -100, -100,  #  48- 49
        -100, -100, -100, -100, -100,  -99,  -99,  -99,  -98,  -98,  #  50- 59
         -97,  -96,  -96,  -95,  -95,  -94,  -93,  -92,  -90,  -88,  #  60- 69
         -86,  -84,  -82,  -78,  -76,  -74,  -72,  -70,  -68,  -66,  #  70- 79
         -62,  -60,  -58,  -56,  -50,  -46,  -44,  -40,  -36,  -32,  #  80- 89
         -28,  -24,  -20,  -14,  -10,   -2,    2,    8,   14,   22,  #  90- 99
          30,   38,   44,   52,   58,   64,   68,   74,   80,   84,  # 100-101
          88,   90,   94,   98,  100                                 # 110-114
        ],
        # Adult men (18+ years)
        [ 48,
                                                        -100, -100,  #  48- 49
        -100, -100, -100, -100,  -99,  -99,  -99,  -99,  -98,  -97,  #  50- 59
         -96,  -95,  -94,  -92,  -90,  -86,  -84,  -82,  -80,  -78,  #  60- 69
         -77,  -76,  -74,  -72,  -70,  -68,  -64,  -62,  -60,  -58,  #  70- 79
         -56,  -50,  -46,  -44,  -40,  -36,  -32,  -28,  -24,  -20,  #  80- 89
         -14,  -10,   -4,    2,    6,   16,   22,   30,   38,   44,  #  90- 99
          50,   54,   58,   60,   62,   66,   70,   76,   80,   90,  # 100-101
          96,   97,   98,   99,  100                                 # 110-114
        ]
);

my $correctmistakes = 0;

sub selectcheatmode {
        my($query) = @_;

        print $query->header,
              $query->start_html(-title=>'De OCA test',
                                 -author=>'ulysses@cyclops.den',
                                 -BGCOLOR=>'white'),
              $query->h1("De OCA test"),
              $query->start_form,
              $query->p("Vul een van de keuzevakjes hieronder in. 
Als je \"Geen cheat\" (standaard) kiest, krijg je een blanco vragenformulier te zien; deze optie moet je kiezen als je de test serieus wilt invullen.

Als je eerst wat proeven wilt nemen, of gewoon lui bent, probeer dan een van de volgende vakjes: \"Laagste score\" en \"hoogste score\" geven grafieken met de hoogste en de laagste lijn. \"Willekeurig\" geeft een grafiek met zomaar een lijn."),
              $query->p(
                  $query->radio_group(
                      -NAME      => 'Cheat mode',
                      -VALUES    => ['Geen cheat',
                                     'Laagste score',
                                     'Hoogste score',
                                     'Willekeurig'],
                      -DEFAULT   => 'Geen cheat',
                      -LINEBREAK => 'true')),
              $query->p($query->submit('Action', 'Begin de test')),
              $query->end_form,
              $query->end_html;
}


sub unanswered {
        my($q) = @_;

        my $retval = " ";
        my $i;
        for ($i = 1; $i <= 200; $i++) {
                my $ans;
                $ans = $q->param("$i");
                $retval .= " $i"
                    unless $ans && ($ans eq "+" || $ans eq "M" || $ans eq "-");
        }

        return $retval;
}


sub generateocatable {
        my($query) = @_;
        my $i;

        print $query->header,
              $query->start_html(-title=>'De Oxford Capacity Analysis (OCA)',
                                 -author=>'ulysses@cyclops.den',
                                 -BGCOLOR=>'white'),
              $query->h1("De Oxford Capacity Analysis (OCA)");
        if ($correctmistakes) {
        print $query->hr,
              $query->h3("Je heeft de volgende vragen niet beantwoord (of er is een fout opgetreden):"), unanswered($query),
              $query->p("De antwoorden kunnen pas worden geanalyseerd als alle vragen zijn beantwoord!"),
              $query->hr;
        }

        print $query->p("Allereerst moet ik weten of je een man of een vrouw bent, en of je volwassen bent of niet:"),
              $query->start_form,
              $query->p("Leeftijd (op dit moment alleen 18 jaar of ouder): ",
                        $query->radio_group("-NAME"    => "age",
                                            #"-VALUES"  => ["14-18", "18+"],
                                            "-VALUES"  => ["18+"],
                                            "-DEFAULT" => "18+")),
              $query->p("Geslacht: ",
                        $query->radio_group("-NAME"    => "gender",
                                            "-VALUES"  => ["Man", "Vrouw"],
                                            "-DEFAULT" => "Man")),
              $query->p("Beantwoord nu alle 200 vragen (tenzij je een van de cheat-opties hebt gekozen). Het is belangrijk dat je <em>alle</em> vragen beantwoordt - het resultaat hangt er vanaf. Als je een niet geheel ingevulde test probeert te analyseren, werkt dat niet. Het programma biedt je de mogelijkheid om de niet beantwoorde vragen alsnog te beantwoorden (de al ingevulde vragen blijven gewoon staan).\n"),
              $query->p($query->submit("Action", "Analyseren"), "&nbsp;",
                        $query->reset("Wissen")),
              $query->p("<table border=2>");

        for ($i = 1; $i <= 200; $i++) {
                $_ = $questions[$i];
                chomp;
                # Remove leading number in question;
                # it's there only for reference.
                my ($n, $q) = split / /, $_, 2;
                my $def;
                $c1 = $Scores[$i][1];
                $c2 = $Scores[$i][2];
                $c3 = $Scores[$i][3];

                if ($correctmistakes) {
                        $def = $query->param("$i") ? $query->param("$i") : "Xenu";
                } elsif ($query->param("Cheat mode") eq "Geen cheat") {
                        $def = "Xenu";
                } elsif ($query->param("Cheat mode") eq "Laagste score") {
                    if (($c1 <= $c2) && ($c1 <= $c3)) {
                        $def = "+";
                    } elsif (($c3 <= $c1) && ($c3 <= $c2)) {
                        $def = "-";
                    } elsif (($c2 <= $c1) && ($c2 <= $c3)) {
                        $def = "M";
                    }
                } elsif ($query->param("Cheat mode") eq "Hoogste score") {
                    if (($c1 >= $c2) && ($c1 >= $c3)) {
                        $def = "+";
                    } elsif (($c3 >= $c1) && ($c3 >= $c2)) {
                        $def = "-";
                    } elsif (($c2 >= $c1) && ($c2 >= $c3)) {
                        $def = "M";
                    }
                } elsif ($query->param("Cheat mode") eq "Willekeurig") {
                    $def = ("+","M","-")[rand(3)];
                } else {
                    die "Argh!";
                }

                print "\n<tr><td align=right><bf>&nbsp;$i&nbsp;</bf></td><td>",
                      $query->radio_group("-NAME"    => "$i",
                                          "-VALUES"  => ["+", "M", "-"],
                                          "-DEFAULT" => "$def"),
                      "</td><td>$q</td></tr>";
        }
        print "\n</table>",
              $query->p($query->submit("Action", "Analyseren"), "&nbsp;",
                        $query->reset("Wissen")),
              $query->end_form,
              $query->end_html;
}



sub analysetest {
        my($query) = @_;
        my %traitscore;

        my $gender = $query->param("gender");
        my $age = $query->param("age");
        
        # Find out which correction table we must use
        my $correction = 0;
        $correction += 1 if $gender eq "Man";
        $correction += 2 if $age eq "18+";

        # Sanity check on gender and age
        if ($gender ne "Man" && $gender ne "Vrouw"
        ||  $age ne "14-18" && $age ne "18+" || $correction < 2) {
                $correctmistakes = 1;
                generateocatable($query);
                exit(0);
        }
        
        # Sum up the scores
        my $i;
        for ($i = 1; $i <= 200; $i++) {
                my $answer = $query->param("$i");
                if (!$answer) {
                        $correctmistakes = 1;
                        generateocatable($query);
                        exit(0);
                }
                if ($answer eq "+") {
                        $answer = 1;
                } elsif ($answer eq "M") {
                        $answer = 2;
                } elsif ($answer eq "-") {
                        $answer = 3;
                } else {
                        $correctmistakes = 1;
                        generateocatable($query);
                        exit(0);
                }

                $traitscore{$Scores[$i][0]} += $Scores[$i][$answer];
        }
        
        print $query->header,
              $query->start_html(-title=>'Je OCA geanalyseerd',
                                 -author=>'ulysses@cyclops.den',
                                 -BGCOLOR=>'white'),
              $query->h1("Je OCA geanalyseerd"), "\n";

        print "<pre>";
        my $mytraits = "";
        my @traitnam = ("A","B","C","D","E","F","G","H","I","J");
        my @myscores;
        for ($i = 0; $i < 10; $i++) {
                my $whichscore = 4*$i+$correction;
                my $n = $ScoreWeights[$whichscore][0]-1;

                push @myscores,
                     $ScoreWeights[$whichscore][$traitscore{$traitnam[$i]}-$n];
                $mytraits .= ($i == 0 ? "" : ",").$myscores[-1];
        }

        print <<EOF;
</pre>
<p>
<applet $appletargs
alt="You must have Java enabled to see the graphical analysis of the test.">
  <param name="traits" value="$mytraits">
Sorry, but you must have a Java-capable browser to see the graphical analysis
of the test.
</applet>
</p><p>
The scores are as follows:
<p>
<table border=2>
<tr>
  <td align=center>Trait</td><td align=center>Your score</td>
  <td align=center>For negative scores</td><td align=center>For positive scores</td>
</tr><tr>
  <td align=center>A</td><td align=right>${myscores[0]}&nbsp;</td>
  <td>Unstable</td><td>Stable</td>
</tr><tr>
  <td align=center>B</td><td align=right>${myscores[1]}&nbsp;</td>
  <td>Depressed</td><td>Happy</td>
</tr><tr>
  <td align=center>C</td><td align=right>${myscores[2]}&nbsp;</td>
  <td>Nervous</td><td>Composed</td>
</tr><tr>
  <td align=center>D</td><td align=right>${myscores[3]}&nbsp;</td>
  <td>Uncertainty</td><td>Certainty</td>
</tr><tr>
  <td align=center>E</td><td align=right>${myscores[4]}&nbsp;</td>
  <td>Inactive</td><td>Active</td>
</tr><tr>
  <td align=center>F</td><td align=right>${myscores[5]}&nbsp;</td>
  <td>Inhibited</td><td>Aggressive</td>
</tr><tr>
  <td align=center>G</td><td align=right>${myscores[6]}&nbsp;</td>
  <td>Irresponsible</td><td>Responsible Causative</td>
</tr><tr>
  <td align=center>H</td><td align=right>${myscores[7]}&nbsp;</td>
  <td>Critical</td><td>Correct Estimation</td>
</tr><tr>
  <td align=center>I</td><td align=right>${myscores[8]}&nbsp;</td>
  <td>Lack of Accord</td><td>Appreciative</td>
</tr><tr>
  <td align=center>J</td><td align=right>${myscores[9]}&nbsp;</td>
  <td>Withdrawn</td><td>Comm Level</td>
</tr>
</table>
</p>
<p>
Wilt je nog een keer proberen? Kies dan "Nogmaals" voor een tweede kans. Of kies anders <a href="$mainpage">klik dit</a> om terug te gaan naar de hoofdpagina van deze website.
EOF
        print $query->start_form,
              $query->p($query->submit("Action", "Nogmaals!")),
              $query->end_form,
              $query->end_html;

        exit(0);
}



my $query = new CGI;

if ($query->param("Action")) {
        if ($query->param("Action") eq "Begin de test") {
                generateocatable($query);
                exit(0);
        } elsif ($query->param("Action") eq "Analyseren") {
                analysetest($query);
                exit(0);
        }
}

selectcheatmode($query);

exit(0);

