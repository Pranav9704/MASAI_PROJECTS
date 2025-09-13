magic_matrix=lo_shu_grid=[[4,9,2],[3,5,7],[8,1,6]]
alpha=["","aijqy","bkr","cgls","dmt","ehnx","uvw","oz","fp"]

class Qsum:
    def __init__(self,number):
        self.number=number
    def nanosum(self):
        sum=0
        self.number=list(str(self.number).strip())
        for i in range(len(self.number)):
            sum=sum+int(self.number[i])
        if sum>9:
            A=Qsum(sum)
            sum=A.nanosum()
        return sum
    
class name:
    def __init__(self,name):
        self.name=name.strip().lower()
    def nanosum(self):
      x=0
      for j in str(self.name):
        for i in alpha:
          if j in i:
            x+=alpha.index(i)
      return x
#name    
N=input("enter your name: ")
A=name(N)
NM=A.nanosum()
A=Qsum(NM)
X=A.nanosum()

#DAY        
DAY=DD=int(input("enter the date of birth: "))
A=Qsum(DD)
DD=A.nanosum()

#MONTH
MONTH=MM=int(input("enter the month number of birth: "))
A=Qsum(MM)
MM=A.nanosum()

#YEAR
YEAR=YY=int(input("enter the year of birth: "))
A=Qsum(YY)
YY=A.nanosum()

sex=input("enter your sex(male/female): ").upper().strip()

#NUMBER TYPES
Driver_number=DD
conductor_number=DD+MM+YY
A=Qsum(conductor_number)
conductor_number=A.nanosum()

if sex=="MALE":
    if YY<=1999:
        universal_number=11-YY
        A=Qsum(universal_number)
        universal_number=A.nanosum()
        
    if YY>=2000:
        universal_number=10-YY
        A=Qsum(universal_number)
        universal_number=A.nanosum()
       
        
        
if sex=="FEMALE":
    if YY<=1999:
        universal_number=4+YY
        A=Qsum(universal_number)
        universal_number=A.nanosum()

    if YY>=2000:
        universal_number=3+YY
        A=Qsum(universal_number)
        universal_number=A.nanosum()
        

#compiling_all_numbers_data
result=[X,DAY,MONTH,YY,Driver_number,conductor_number,universal_number]
Yr=list(str(YEAR))
Yr=list(set(map(int,Yr)))
Z=[]
for i in Yr:
    if i>0:
        result.append(i)
result=list(set(result))
l_total=[]
Absence_total=[]
numbers=[1,2,3,4,5,6,7,8,9,11,22,33]
for i in result:
    for j in numbers:
        if i == j:
            l_total.append(j)  #collecting important data


#your's current qualities
print("\n")            
print("__________________YOUR'S_CURRENT_QUALITIES_________________________")
interpretations = {
        1: "Independent, leader, new beginnings.",
        2: "Diplomatic, cooperative, sensitive.",
        3: "Expressive, creative, social.",
        4: "Practical, disciplined, hardworking.",
        5: "Adventurous, freedom-loving, flexible.",
        6: "Responsible, nurturing, family-oriented.",
        7: "Analytical, introspective, spiritual.",
        8: "Ambitious, material success, authority.",
        9: "Compassionate, humanitarian, ending/closure.",
        11: "Spiritual insight, visionary (master).",
        22: "Master builder, large-scale achievements (master).",
        33: "Teacher/teacher of teachers, highly compassionate (master)."}

for num,quality in interpretations.items():
    for i in l_total:
        if num == i:
            print(quality)



#powers:
print("\n")            
print("__________________YOUR'S_HIDDEN_POWERS________________________")
powers_data={(4,9,2):"mind(logic) power",(3,5,7):"emotion power",(8,1,6):"practical power",(4,3,8):"thought power",(9,5,1):"will power",(2,7,6):"action power"}
output_power={}
for lst,pwr in powers_data.items():
    percentage=0
    for i in l_total:
        if i in lst:
            percentage+=33
    output_power[pwr]=percentage
#print(output_power)
for quality,pwr in output_power.items():
    print(f"{quality}: {pwr}%")



    

#your's qualities to be improved
print("\n")            
print("__________________YOUR'S_QUALITIES_TO_BE IMPROVED________________________")
absence_corrections ={
        1: '''Absent means: Lack of confidence, difficulty taking initiative, dependence on others.
Correction:
Develop self-reliance.
Set small personal goals and achieve them.
Wear or use Sun-related things (gold, copper, yellow).\n''',
        2: '''Absent means: Trouble working in partnerships, may appear insensitive, lack of diplomacy.
Correction:
Practice patience, teamwork, and listening.
Strengthen Moon energy (silver, water, calmness, meditation).\n''',
        3: '''Absent means: Difficulty expressing thoughts, lack of confidence in speech, less creativity.
Correction:
Learn to express feelings through art, music, writing.
Strengthen Jupiter energy (yellow, chanting, teaching).\n''',
        4: '''Absent means: Disorderly, restless, avoid responsibility, dislike routine.
Correction:
Build consistent habits (daily schedule).
Strengthen Rahu energy (order, planning, working with hands).\n''',
        5: '''Absent means: Rigid, less adventurous, trouble adapting to change, shy in public.
Correction:
Travel, meet new people, try new experiences.
Strengthen Mercury energy (green, communication skills, business).\n''',
        6: '''Absent means: Weak family ties, avoid responsibility, imbalance in relationships.
Correction:
Spend time with family, take responsibility.
Strengthen Venus energy (beauty, art, harmony, pink/white colors).\n''',
        7: '''Absent means: Materialistic, superficial, avoids deep thinking, restless mind.
Correction:
Practice meditation, solitude, and self-reflection.
Strengthen Ketu energy (simple living, spirituality, silence).\n''',
        8: '''Absent means: Fear of authority, difficulty managing money, avoid responsibility.
Correction:
Learn discipline in finance and leadership.
Strengthen Saturn energy (black/blue, service, patience, discipline).\n''',
        9: '''Absent means: Self-centered, less compassion, trouble letting go of things.
Correction:
Practice charity, forgiveness, and kindness.
Strengthen Mars energy (red, courage, sports, physical activity).\n''',}
            
Absence_total=list(set(numbers)-set(l_total))
for num,Aquality in absence_corrections.items():
    for i in Absence_total:
        if num == i:
            print(Aquality)


#81 personality qualities to bring in life
QUALITIES={
        1: '''[emotion and colors in life]: Confidence, ambition, independence, and strong-willed determination.,\n[material]:Leadership symbols, awards, and innovative creations,Gold,\n[Gemstones]:Ruby and amber\n''',

        2: '''[emotion and colors in life]:White and silver, Empathy, intuition, sensitivity, and patience.,\n[material]:Pairs of items, creating balance and symmetry in a home.,\n[Gemstones]: Pearl, moonstone, and jade.
\n''',
        

        3: '''[emotion and colors in life]: Light yellow, green, and orange. Enthusiasm, optimism, and charm.,\n[material]: Art supplies, musical instruments, and creative projects.,\n[Gemstones]:Yellow sapphire.\n''',

        4: '''[emotion and colors in life]:Dependability, loyalty, discipline, and practicality.,\n[material]: Buildings, systems, and anything with a solid foundation.
,\n[Gemstones]:Emerald.\n''',

        5: '''[emotion and colors in life]:Adaptability, resourcefulness, and wit.,\n[material]:Vehicles, communication devices, and travel gear.,\n[Gemstones]:Diamond and emerald\n''',

        6: '''[emotion and colors in life]:Blue, pink, and green. Compassion, loyalty, and artistic appreciation.,\n[material]: A stable home, art, and items that create harmony.,\n[Gemstones]: Diamond and jade.\n''',

        7: '''[emotion and colors in life]:Introspection, deep thinking, and spiritual attunement.,\n[material]: Books, spiritual tools, and items that facilitate solitude,\n[Gemstones]: Cat's eye, amethyst, and lapis lazuli.\n''',

        8: '''[emotion and colors in life]:Introspection, deep thinking, and spiritual attunement.,\n[material]:Books, spiritual tools, and items that facilitate solitude.\n[Gemstones]:Cat's eye, amethyst, and lapis lazuli.\n''',

        9: '''[emotion and colors in life]:Ambition, determination, and resilience,\n[material]: Financial investments, corporate structures, and businesses.,\n[Gemstones]:Blue sapphire, onyx, and obsidian.\n'''
        }


N1=["","FORTUNES FAVOURITE","BEST FOR NAVY AND WATER","BEST FOR OCCULT","POLITICS","BANKING AND FINANCE","LUXARY GLAMOUR","OCCULT/EDUCATION","STRUGGLE/MARRIAGE ISSUES/POLICE/POILITICS","SUPER SUCCESSFUL"]
N2=["","SUCCESSFULL","WATER RELATED WORK","OCCULT/EDUCATION/HEALER","STRUGGLE/DEPRESSION","BEST FOR REAL STATE BANKING AND FINANCE","SWEETS","TEACHING/OCCULT","STRUGGLE/HEALTH ISSUES","MARRIAGE PROBLEMS"]
N3=["","OCCULT/EDUCATION/HEALER/DOCTOR/ADMIN","WATER RELATED WORK","EDUCATION/OCCULT","SALES/MARKETING","EXELLENT IN COMMUNICATION","STRUGGLE/HEALTH/MARRIAGE ISSUES","EDUCATION/OCCULT","LAWER/PRINTING/SALES","EDUCATION/DOCTOR/ADMIN"]
N4=["","POLITICS","DEPRESSION AND STRUGGLE","SALES/MARKETING/OCCULT/EDUCATION","BEST FOR LAW/STRUGGLE","BANKING AND EVENT MANAGEMENT","MEDIA/LUXARY/GLAMOUR","SUCCESSFULL/OCCULT BEST","STRUGGLE/BEST FOR LAW","STRUGGLE/HEALTH ISSUES"]
N5=["","SUCCESSFULL FINANCE/LOAN/PROPERTY","REAL STATE","COMMUNICATION AND OCCULT","OVERALL SUCCESSFULL SALES/MARKETING","VERY SUCCESSSFULL","VERY SUCCESSFULL","OCCULT AND BANKING","PROPERTY","SUCCESSFULL"]
N6=["","MEDIA/LUXARY/GLAMOUR","SWEET SHOP","HEALTH/MARRAGE ISSUES","SUCCESSFUL/MEDIA","SUPER SUCCESSFULL","SUPER SUCCESSFUL MEDIA/FILMS/TOURS","SUCCESSFUL/SPORTS/ROMANTIC","BEST FOR LAW","SUCCESSFUL/CONTROVERSIES"]
N7=["","BEST IN OCCULT","OCCULT/INTUTION","TEACHING/HEALING/OCCULT","SUCCESSFULL","OCCULT","SPORTS","DISAPPOINTMENT/MARRAGE ISSUES","OCCULT","TEACHING OCCULT"]                                                                                
N8=["","MARRAIGE PROBLEM","HEALTH ISSUES","LAW/PRINTING","SALES/MARKETING STRUGGLES","REAL STATE","BEST FOR LAW","OCCULT","STRUGGLE BUT GOOD IN SPORTS","ARMY"]
N9=["","SUCCESSFULL","STRUGGLE/MARRIAGE ISSUES","OCCULT/HEALING","STRUGGLE/HEALTH ISSUES","SUCCESSSFULL","CONTROVERSIES","OCCULT/TEACHING","ARMY/POLICE","MARRAIAGE PROBLEM"]
N=["",N1,N2,N3,N4,N5,N6,N7,N8,N9]
ask=input("________________'DO_ U_TO_ADD_SOMETHING_TO_YOUR_PERSONALITY_OR_LIFE'_________________\n\n(yes/no): ").strip()
ask=ask.lower()
if ask=="yes":
    print("enter the quality u want in life from the following options: ")
    print(f"choose the index: ")
    for i in range(1,10):
        for j in range(1,10):
            print(f"{N[i][j]}: {i,j}")
    I=list(set(map(int,input("enter pair of numbers with space: ").split())))
    print(f"__________________THE_QULITIES_TO_BRING_OF:_{N[i][j]}_BY_FOLLOWS______________________")
    for i in I:
        print(QUALITIES[i])
else:
    print("______________THE_END________________")

    
