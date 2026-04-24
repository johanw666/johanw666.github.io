#!/usr/bin/perl -w

use CGI qw(:standard);

# You might want to change these two lines:
my $appletargs = 'codebase="/users/johanw/CoS/OCA" code="OCA.class" width=550 height=250';
my $mainpage = "http://www.vulcan.homenet.home/users/johanw/CoS/OCA/";

my @questions = (
    "DUMMY",
    "1 Do you make thoughtless remarks or accusations which later you regret?",
    "2 When others are getting rattled, do you remain fairly composed?",
    "3 Do you browse through railway timetables, directories, or dictionaries just for
pleasure?",
    "4 When asked to make a decision, would you be swayed by your like or dislike of the
personality involved?",
    "5 Do you intend two or less children in your family even though your health and income
will permit more?",
    "6 Do you get occasional twitches of your muscles, when there is no logical reason for
it?",
    "7 Would you prefer to be in a position where you did not have the responsibilities of
making decisions?",
    "8 Are your actions considered unpredictable by other people?",
    "9 Do you consider more money should be spent on social security?",
    "10 Do other people interest you very much?",
    "11 Is your voice monotonous, rather than varied in pitch?",
    "12 Do you normally let the other person start the conversation?",
    "13 Are you readily interested in other people's conversations?",
    "14 Would the idea of inflicting pain on game, small animals or fish prevent you from
hunting or fishing?",
    "15 Are you often impulsive in your behavior?",
    "16 Do you speak slowly?",
    "17 Are you usually concerned about the need to protect your health?",
    "18 Does an unexpected action cause your muscles to twitch?",
    "19 Are you normally considerate in your demands on your employees, relatives, or pupils?",
    "20 Do you consider that you could give a valid \"snap judgment\"?",
    "21 Do your past failures still worry you?",
    "22 Do you find yourself being extra-active for periods lasting several days?",
    "23 Do you resent the efforts of others to tell you what to do?",
    "24 Is it normally hard for you to \"own up and take the blame\"?",
    "25 Do you have a small circle of close friends, rather than a large number of friends,
speaking acquaintances?",
    "26 Is your life a constant struggle for survival?",
    "27 Do you often sing or whistle just for the fun of it?",
    "28 Are you considered warm-hearted by your friends?",
    "29 Would you rather give orders than take them?",
    "30 Do you enjoy telling people the latest scandal about your associates?",
    "31 Could you agree to \"strict discipline\"?",
    "32 Would the idea of making a com-plete new start cause you much concern?",
    "33 Do you make efforts to get others to laugh and smile?",
    "34 Do you find it easy to express your emotions?",
    "35 Do you refrain from complaining when the other person is late foran appointment?",
    "36 Are you sometimes considered by others a \"spoilsport\"?",
    "37 Do you consider there are other people who are definitely unfriendly toward you and
work against you?",
    "38 Would you admit you were wrong just to \"keep the peace\"?",
    "39 Do you have only a few people of whom you are really fond?",
    "40 Are you rarely happy, unless you have a special reason?",
    "41 Do you \"circulate around\" at a social gathering?",
    "42 Do you take reasonable precaution to prevent accidents?",
    "43 Does the idea of talking in front of people make you nervous?",
    "44 If you saw an article in a shop obviously mistakenly marked lower than its correct
price, would you try to get it at that price?",
    "45 Do you often feel that people are looking at you or talking about you behind your
back?",
    "46 Are you \"always getting into trouble\"?",
    "47 Have you any particular hate or fear?",
    "48 Do you prefer to be an onlooker rather than participate in any active sport?",
    "49 Do you find it easy to be impartial?",
    "50 Have you a definitely set standard of courteous behavior in front of other members of
your family?",
    "51 Can you \"start the ball rolling\" at a social gathering?",
    "52 Would you \"buy on credit\" with the hope that you can keep up the payments?",
    "53 Do you get an after-reaction when something unexpected such as an accident or other
disturbing incident takes place?",
    "54 Do you consider the good of all concerned rather than your own personal advantages?",
    "55 When hearing a lecturer, do you sometimes experience the idea that the speaker is
referring entirely to you?",
    "56 Does \"external noise\" rarely interfere with your concentration?",
    "57 Are you usually \"up-to-date\" on everyday affairs?",
    "58 Can you confidently plan and work towards carrying out an event in six months time?",
    "59 Do you consider the modern \"prisons without bars\" system doomed to failure?",
    "60 Do you tend to be careless?",
    "61 Do you ever get a \"dreamlike\" feeling toward life when it all seems unreal?",
    "62 Do you speedily recover from the effects of bad news?",
    "63 When you criticize - do you at the same time try to encourage?",
    "64 Are you normally considered \"cold\"?",
    "65 Are your opinions insufficiently important to tell other people?",
    "66 Are you so self-assured that it sometimes annoys others?",
    "67 Do you keep \"close contact\" on articles of yours which you have loaned to friends?",
    "68 Do you enjoy activities of your own choosing?",
    "69 Does emotional music have quite an effect on you?",
    "70 Do you completely condemn a person because he is a rival or opponent in some aspect of
your relations with him?",
    "71 Do you often \"sit and think\" about death, sickness, pain and sorrow?",
    "72 Are you perturbed at the idea of loss of dignity?",
    "73 Are you always collecting things which \"might be useful\"?",
    "74 Would you criticize faults and point out the bad points on someone else's character or
handiwork?",
    "75 Are you openly appreciative of beautiful things?",
    "76 Do you sometimes give away articles which strictly speaking do not belong to you?",
    "77 Do you greet people effusively?",
    "78 Do you often ponder on previous misfortunes?",
    "79 Are you sometimes considered forceful in your actions or opinions?",
    "80 Do you accept criticism easily and without resentment?",
    "81 Are you usually undisturbed by \"noises off\" when you are trying to rest?",
    "82 Are you likely to be jealous?",
    "83 Do you tend to put off doing things and then discover it is too late?",
    "84 Do you prefer to abide by the wishes of others rather than seek to have your own way?",
    "85 Do you find it easy to get yourself started on a project?",
    "86 Do you bite your fingernails or chew the end of your pencil?",
    "87 Do you \"turn up the volume\" of your emotions just to create an effect?",
    "88 If we were invading another country, would you feel sympathetic towards conscientious
objectors in this country?",
    "89 Are there some things about yourself on which you are touchy?",
    "90 Do you have few interests and activities that are your own choice?",
    "91 Do you ever get a single thought which hangs around for days?",
    "92 Are you a slow eater?",
    "93 Can you be a stabilizing influence when others get panicky?",
    "94 Would you stop and find out whether a person needed help even though they had not
directly asked you for it?",
    "95 Are you prejudiced in favor of your own school, college, club or team, etc.?",
    "96 Do you pay your debts and keep your promises when it is possible?",
    "97 Do you sleep well?",
    "98 Would you use corporal punishment on a child aged ten if it refused to obey you?",
    "99 Do you prefer to take a passive role in any club or organization to which you belong?",
    "100 Are you logical and scientific in your thinking?",
    "101 Does the youth of today have more opportunity than that of a generation ago?",
    "102 Do you throw things away only to discover that you need them later?",
    "103 Would you give up easily on a given course if it were causing you a considerable
amount of inconvenience?",
    "104 Do you \"wax enthusiastic\" about only a few subjects?",
    "105 Do you rarely suspect the actions of others?",
    "106 Do you sometimes wonder if anyone really cares about you?",
    "107 Do you turn down responsibility because you doubt your fitness to cope?",
    "108 Do you sometimes feel compelled to repeat some interesting item or tidbit?",
    "109 Do you tend to exaggerate a justifiable grievance?",
    "110 Is your facial expression varied rather than set?",
    "111 Do you usually need to justify or back up an opinion once stated?",
    "112 Do you openly and sincerely admire beauty in other people?",
    "113 Would it take a definite effort on your part to consider the subject of suicide?",
    "114 Would you consider yourself energetic in your attitude toward life?",
    "115 Would a disagreement affect your general relationship with another person?",
    "116 Does a minor failure on your part rarely trouble you?",
    "117 Do you sometimes feel that you talk too much?",
    "118 Do you smile much?",
    "119 Are you easily pleased?",
    "120 When met with direct opposition would you still seek to have your own way rather than
give in?",
    "121 Provided the distance were not too great, would you still prefer to ride rather than
walk?",
    "122 Do you ever get disturbed by the noise of the wind or a \"house settling down\"?",
    "123 Is your opinion influenced by looking at things from the standpoint of your
experiences, occupation or training?",
    "124 Do you often make tactless blunders?",
    "125 Are you suspicious of people who ask to borrow money from you?",
    "126 Are your decisions swayed by personal interests?",
    "127 Can you get quite enthusiastic over \"some simple little thing\"?",
    "128 Do you frequently take action even though you know your own good judgment would
indicate otherwise?",
    "129 Are you in favor of color bar and class distinction?",
    "130 Are you aware of any habitual physical mannerisms such as pulling your hair, nose,
ears, or such like?",
    "131 Can you quickly adapt and make use of new conditions and situations even though they
may be difficult?",
    "132 Do some noises \"set your teeth on edge\"?",
    "133 Can you see the other fellow's point of view when you wish to?",
    "134 Do you go to bed when you want to, rather than \"by the clock\"?",
    "135 Do the \"petty foibles\" of others make you impatient?",
    "136 Do children irritate you?",
    "137 Are you less talkative than your associates?",
    "138 Do you usually carry out assignments promptly and systematically?",
    "139 Would you assist a fellow traveler rather than leave it to the officials?",
    "140 When voting, do you vote the same party ticket straight rather than studying the
candidates and issues?",
    "141 Do you frequently dwell on your past illnesses or painful experiences?",
    "142 Do you get very ill at ease in disordered surroundings?",
    "143 Do you usually criticize a film or show that you see or a book that you read?",
    "144 When recounting some amusing incident can you easily imitate the mannerisms or the
dialect in the original incident?",
    "145 In subjects about which you are not expert, are your own ideas of sufficient
importance as to tell others?",
    "146 Do you have a tendency to tidy up a disorder of somebody else's household?",
    "147 Can you accept defeat easily without the necessity of \"swallowing your
disappointment\"?",
    "148 Do you often feel depressed?",
    "149 Are you ever ill at ease in the company of children?",
    "150 Do you get frustrated at not being able to do something rather than finding a
substitute activity or system?",
    "151 Are you sometimes completely unable to enter the spirit of things?",
    "152 Do you rarely express your grievances?",
    "153 Do you work in \"spurts,\" being relatively inactive and then furiously active for a
day or two?",
    "154 Does the number of uncompleted jobs you have on hand bother you?",
    "155 Do people enjoy being in your company?",
    "156 Could you allow someone to finish those \"final two words\" in a crossword puzzle
without interfering?",
    "157 Do you consider the best points of most people and only rarely speak slightingly of
them?",
    "158 Do you laugh or smile quite readily?",
    "159 Are you definite and emphatic in voice and manner?",
    "160 Are you effusive only to close friends if at all?",
    "161 Are your interests and fields of knowledge so important as to give little time for
anything else?",
    "162 Would you like to \"start a new activity\" in the area in which you live?",
    "163 Would you make the necessary actions to kill an animal in order to put it out of
pain?",
    "164 Is it easy for you to relax?",
    "165 Do you have little regret on past misfortunes and failures?",
    "166 Does the idea of fear or apprehension give you a physical reaction?",
    "167 Can you trust the decision of your judgment in an emotional situation in which you are
involved?",
    "168 Could someone else consider that you were really active?",
    "169 Do you find it hard to get started on a task that needs to be done?",
    "170 Are you opposed to the \"probation system\" for criminals?",
    "171 Do you spend much time on needless worries?",
    "172 In a disagreement do you find it hard to understand how the other person fails to see
your side, and thus agree with you?",
    "173 Do you cope with everyday problems of living quite well?",
    "174 Are you usually truthful to others?",
    "175 Would you rather \"wait for something to happen\" as opposed to you causing it?",
    "176 Do you spend too freely in relation to your income?",
    "177 Can you take a \"calculated risk\" without too much worry?",
    "178 If you were involved in a slight car accident, would you really take the trouble to
see that any damage you did was made good?",
    "179 Do others push you around?",
    "180 Do you make allowances for your friends where with others you might judge more
severely?",
    "181 Do you often ponder over your own inferiority?",
    "182 Do people criticize you to others?",
    "183 Are you embarrassed by a hearty greeting such as a kiss, hug, or pat on the back, if
done in public?",
    "184 Do you frequently not do something you want to do because of other people's desires?",
    "185 Are you sometimes convinced of the correctness of your opinions about a subject even
though you are not an expert?",
    "186 Do you often find yourself \"going off in all directions at once\"?",
    "187 Do your acquaintances seem to think more of your abilities than you do?",
    "188 Is the idea of death or even reminders of death abhorrent to you?",
    "189 Having settled an argument out do you continue to feel disgruntled for a while?",
    "190 Are you friendly in voice, attitude, and expression?",
    "191 Does life seem rather vague and unreal to you?",
    "192 Do you often feel upset about the fate of war victims and political refugees?",
    "193 Do \"mere acquaintances\" appeal to you for aid or advice in their personal
difficulties?",
    "194 If you lose an article, do you get the idea that \"someone must have stolen or mislaid
it\"?",
    "195 If you thought that someone was suspicious of you and your actions, would you tackle
them on the subject rather than leaving them to work it out?",
    "196 Do you sometimes feel that your age is against you (too young or too old)?",
    "197 Do you have spells of being sad and depressed for no apparent reason?",
    "198 Do you do much grumbling about conditions you have to face in life?",
    "199 Do you tend to hide your feelings?",
    "200 Do you consider you have many warm friends?",
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
              $query->start_html(-title=>'The OCA test',
                                 -author=>'ulysses@cyclops.den',
                                 -BGCOLOR=>'white'),
              $query->h1("The OCA test"),
              $query->start_form,
              $query->p("First, select the \"cheat mode\" you'd like to use.
Selecting \"No cheating\" (default) gives you a blank sheet if you'd like to do
the test without cheating.  On the other hand, if you'd like to experiment a
little, or is lazy, you can select one of the following options: \"Low/high
scores\" gives you a sheet with defaults that will give you the lowest/highest
score possible, while \"Random\" gives you a randomly filled in test."),
              $query->p(
                  $query->radio_group(
                      -NAME      => 'Cheat mode',
                      -VALUES    => ['No cheating',
                                     'Low scores',
                                     'High scores',
                                     'Random'],
                      -DEFAULT   => 'No cheating',
                      -LINEBREAK => 'true')),
              $query->p($query->submit('Action', 'Start test')),
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
              $query->start_html(-title=>'The Oxford Capacity Analysis (OCA)',
                                 -author=>'ulysses@cyclops.den',
                                 -BGCOLOR=>'white'),
              $query->h1("The Oxford Capacity Analysis (OCA)");
        if ($correctmistakes) {
        print $query->hr,
              $query->h3("You did not answer the following questions (or an error occured):"),
              unanswered($query),
              $query->p("The test can not be analysed until all questions are answered!"),
              $query->hr;
        }

        print $query->p("First, I need to know your gender, and whether you're an adult or
not:"),
              $query->start_form,
              $query->p("Age (only 18+ implemented so far): ",
                        $query->radio_group("-NAME"    => "age",
                                            #"-VALUES"  => ["14-18", "18+"],
                                            "-VALUES"  => ["18+"],
                                            "-DEFAULT" => "18+")),
              $query->p("Gender: ",
                        $query->radio_group("-NAME"    => "gender",
                                            "-VALUES"  => ["Male", "Female"],
                                            "-DEFAULT" => "Male")),
              $query->p("Next, I want you to answer all 200 questions (unless
you have selected one of the cheating modes).  It's important that you fill in
<em>all</em> the questions - the test result depends on that.  If you submit an
incomplete test sheet, the script will complain, and take you back so you can
fill out the missing questions (with all your other answers intact.\n"),
              $query->p($query->submit("Action", "Analyse"), "&nbsp;",
                        $query->reset("Reset form")),
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
                } elsif ($query->param("Cheat mode") eq "No cheating") {
                        $def = "Xenu";
                } elsif ($query->param("Cheat mode") eq "Low scores") {
                    if (($c1 <= $c2) && ($c1 <= $c3)) {
                        $def = "+";
                    } elsif (($c3 <= $c1) && ($c3 <= $c2)) {
                        $def = "-";
                    } elsif (($c2 <= $c1) && ($c2 <= $c3)) {
                        $def = "M";
                    }
                } elsif ($query->param("Cheat mode") eq "High scores") {
                    if (($c1 >= $c2) && ($c1 >= $c3)) {
                        $def = "+";
                    } elsif (($c3 >= $c1) && ($c3 >= $c2)) {
                        $def = "-";
                    } elsif (($c2 >= $c1) && ($c2 >= $c3)) {
                        $def = "M";
                    }
                } elsif ($query->param("Cheat mode") eq "Random") {
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
              $query->p($query->submit("Action", "Analyse"), "&nbsp;",
                        $query->reset("Reset form")),
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
        $correction += 1 if $gender eq "Male";
        $correction += 2 if $age eq "18+";

        # Sanity check on gender and age
        if ($gender ne "Male" && $gender ne "Female"
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
              $query->start_html(-title=>'Your OCA analysed',
                                 -author=>'ulysses@cyclops.den',
                                 -BGCOLOR=>'white'),
              $query->h1("Your OCA analysed"), "\n";

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
Would you like to try again?  Press the "Once more!" button for another time
through.  Otherwise, <a href="$mainpage">click here</a> to go back to the main
CoS-page of this website.
EOF
        print $query->start_form,
              $query->p($query->submit("Action", "Once more!")),
              $query->end_form,
              $query->end_html;

        exit(0);
}



my $query = new CGI;

if ($query->param("Action")) {
        if ($query->param("Action") eq "Start test") {
                generateocatable($query);
                exit(0);
        } elsif ($query->param("Action") eq "Analyse") {
                analysetest($query);
                exit(0);
        }
}

selectcheatmode($query);

exit(0);

