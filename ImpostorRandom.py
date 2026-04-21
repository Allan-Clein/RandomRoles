import random as rn

NPlayers = ""
NImpostor = ""
NNeutral = ""
Roles = []
players = {}

def Preset():
    global NPlayers, NImpostor, NNeutral
    NPlayers = int(input("Número de jogadores: "))
    NImpostor = int(input("Número de impostores: "))
    NNeutral = int(input("Número de neutros: "))

def RandomRoles():
    global i, NPlayers, NImpostor, NNeutral, t, c, j
    for t in range(NPlayers):
        if NNeutral < 1 and NImpostor < 1:
            Roles.append("Crewmate")
        for c in range(NImpostor):
            if NImpostor > 0 and NNeutral < 1:
                Roles.append("Impostor")
                NImpostor -= 1
        for j in range(NNeutral):
            if NNeutral > 0:
                Roles.append("Neutro")
                NNeutral -= 1

def GeratePlayers():
    global NPlayers, i, player_id, players, role
    for i in range(NPlayers):
        player_id = f"player{i+1}"
        role = Roles[rn.randint(0, len(Roles) -1)]
        players[player_id] = {
            "role" : role
        }
        Roles.remove(role)
    
while True:
    try:
        Preset()
        if NPlayers >= NImpostor + NNeutral:
            break
        else:
            print("Você não pode ter um número inferior de jogadores ao de funções.")
    except:
        print("Algo deu errado, escolha corretamente!")

RandomRoles()
print(Roles)
GeratePlayers()
print(players)