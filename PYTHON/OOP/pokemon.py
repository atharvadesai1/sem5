class Pokemon:
    def __init__(self,name,type,ranking,version):
        self.name = name
        self.type = type
        self.ranking = ranking
        self.version = version
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Ranking: {self.ranking}")
        print(f"Version: {self.version}")

    def properties(self):
        vowels = "aeiouAEIOU"
        if(self.type[0] in vowels):
            article = 'an'
        else:
            article = 'a'
        print(f"{self.name} is {article} {self.type} type of Pokemon")
        if(self.type.lower()=="fire"):
            print(f"{self.type} pokemons are strong against Grass, Bug, Ice and weak against Water, Rock, Fire")
        elif(self.type.lower()=="water"):
            print(f"{self.type} pokemons are strong against Fire, Ground, Rock and weak against Electric, Grass")
        elif(self.type.lower()=="electric"):
            print(f"{self.type} pokemons are strong against Water, Flying and weak against Ground")
        elif(self.type.lower()=="grass"):
            print(f"{self.type} pokemons are strong against Water, Ground, Rock and weak against Fire, Ice, Poison")
        elif(self.type.lower()=="ice"):
            print(f"{self.type} pokemons are strong against Grass, Ground, Flying, Dragon and weak against Fire, Fighting, Rock, Steel")
        elif(self.type.lower()=="fighting"):
            print(f"{self.type} pokemons are strong against Ice, Rock, Dark, Steel and weak against Flying, Psychic, Fairy")
        elif(self.type.lower()=="poison"):
            print(f"{self.type} pokemons are strong against Grass, Fairy and weak against Ground, Psychic")
        elif(self.type.lower()=="ground"):
            print(f"{self.type} pokemons are strong against Fire, Electric, Poison, Rock, Steel and weak against Water, Ice, Grass")
        elif(self.type.lower()=="flying"):
            print(f"{self.type} pokemons are strong against Grass, Fighting, Bug and weak against Electric, Ice, Rock")
        elif(self.type.lower()=="psychic"):
            print(f"{self.type} pokemons are strong against Fighting, Poison and weak against Bug, Ghost, Dark")
        elif(self.type.lower()=="bug"):
            print(f"{self.type} pokemons are strong against Grass, Psychic, Dark and weak against Fire, Flying, Rock")
        elif(self.type.lower()=="rock"):
            print(f"{self.type} pokemons are strong against Fire, Ice, Flying, Bug and weak against Water, Grass, Fighting, Ground, Steel")
        elif(self.type.lower()=="ghost"):
            print(f"{self.type} pokemons are strong against Psychic, Ghost and weak against Dark")
        elif(self.type.lower()=="steel"):
            print(f"{self.type} pokemons are strong against Ice, Rock, Fairy and weak against Fire, Fighting, Ground")
        elif(self.type.lower()=="dragon"):
            print(f"{self.type} pokemons are strong against Dragon and weak against Ice, Dragon, Fairy")
        elif(self.type.lower()=="dark"):
            print(f"{self.type} pokemons are strong against Psychic, Ghost and weak against Fighting, Bug, Fairy")
        elif(self.type.lower()=="fairy"):
            print(f"{self.type} pokemons are strong against Fighting, Dragon, Dark and weak against Poison, Steel")
        else:
            print("No information available")

pikachu = Pokemon('Pikachu','Electric',4,1)
pikachu
pikachu.properties()
print("\n")
charmender = Pokemon('Charmender','Fire',5,1)
charmender
charmender.properties()
print("\n")
butterfree = Pokemon('Butterfree','Flying',12,3)
butterfree
butterfree.properties()
        