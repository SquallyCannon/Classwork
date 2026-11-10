import pokebase as pb
import random
import tkinter as Tk
from tkinter import *

root = Tk()
root.geometry(f'{1000}x{750}')
root.title('POKEMON GOTTA CATCH UM ALLLLLLLLLLLLLLLLL OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOH')

def get_wordle_pokemon(poke):
    global pokemon, pokemon_species, types, pokemon_color, pokemon_habitat, pokemon_egg, pokemon_gen, pokemon_evolution
    pokemon = pb.pokemon(poke)
    pokemon_species = pb.pokemon_species(poke)

    types = [t.type.name for t in pokemon.types]
    try:
        if types[1].capitalize() == "Wow":
            print("WOW")
    except:
        types.append(None)
    pokemon_color = pokemon_species.color.name
    pokemon_egg = pokemon_species.egg_groups
    try:
        if pokemon_egg[1].capitalize() == "Wow":
            print("WOW")
    except:
        pokemon_egg.append(None)
    pokemon_gen = pokemon_species.generation
    pokemon_habitat = pokemon_species.habitat
    pokemon_evolution = 0
    pokemon_evolution1 = None
    pokemon_evolution2 = None
    pokemon_evolution1 = pokemon_species.evolves_from_species
    try:
        pokemone = pb.pokemon_species(str(pokemon_evolution1))
        pokemon_evolution2 = pokemone.evolves_from_species
    except:
        pokemon_evolution2 = None

    if pokemon_evolution1 != None:
        pokemon_evolution += 1
    if pokemon_evolution2 != None:
        pokemon_evolution += 1
    
    '''print(pokemon.id)
    if pokemon_egg[1] == None or pokemon_habitat == None or types[1] == None:
        if pokemon_egg[1] == None and pokemon_habitat == None and types[1] == None:
            print(pokemon.name.capitalize(), pokemon_gen.name.capitalize(), pokemon_color.capitalize(), types[0].capitalize(), None, pokemon_egg[0].name.capitalize(), None, None, pokemon_evolution)
        elif pokemon_egg[1] == None and pokemon_habitat == None:
            print(pokemon.name.capitalize(), pokemon_gen.name.capitalize(), pokemon_color.capitalize(), types[0].capitalize(), types[1].capitalize(), pokemon_egg[0].name.capitalize(), None, None, pokemon_evolution)
        elif pokemon_habitat == None and types[1] == None:
            print(pokemon.name.capitalize(), pokemon_gen.name.capitalize(), pokemon_color.capitalize(), types[0].capitalize(), None, pokemon_egg[0].name.capitalize(), pokemon_egg[1].name.capitalize(), None, pokemon_evolution)
        elif pokemon_egg[1] == None and types[1] == None:
            print(pokemon.name.capitalize(), pokemon_gen.name.capitalize(), pokemon_color.capitalize(), types[0].capitalize(), None, pokemon_egg[0].name.capitalize(), None, pokemon_habitat.name.capitalize(), pokemon_evolution)
        elif types[1] == None:
            print(pokemon.name.capitalize(), pokemon_gen.name.capitalize(), pokemon_color.capitalize(), types[0].capitalize(), None, pokemon_egg[0].name.capitalize(), pokemon_egg[1].name.capitalize(), pokemon_habitat.name.capitalize(), pokemon_evolution)
        elif pokemon_habitat == None:
            print(pokemon.name.capitalize(), pokemon_gen.name.capitalize(), pokemon_color.capitalize(), types[0].capitalize(), types[1].capitalize(), pokemon_egg[0].name.capitalize(), pokemon_egg[1].name.capitalize(), None, pokemon_evolution)
        elif pokemon_egg[1] == None:
            print(pokemon.name.capitalize(), pokemon_gen.name.capitalize(), pokemon_color.capitalize(), types[0].capitalize(), types[1].capitalize(), pokemon_egg[0].name.capitalize(), None, pokemon_habitat.name.capitalize(), pokemon_evolution)
    else:
        print(pokemon.name.capitalize(), pokemon_gen.name.capitalize(), pokemon_color.capitalize(), types[0].capitalize(), types[1].capitalize(), pokemon_egg[0].name.capitalize(), pokemon_egg[1].name.capitalize(), pokemon_habitat.name.capitalize(), pokemon_evolution)'''

def get_pokemon(event):
    global pokemon, types, pokemon_color, pokemon_habitat, pokemon_egg, pokemon_evolution, entry, quality, guess, pokemon_names, border, cooldown
    if cooldown:
        return
    cooldown = True
    entry.config(state="disabled")
    pokemon_suggestions.place_forget()
    iname = False
    ityper1 = False
    ityper2 = False
    icolor = False
    igen = False
    iegg1 = False
    iegg2 = False
    ihabitat = False
    ievolution = False
    ichecks = [iname,ityper1, ityper2, icolor, igen, iegg1, iegg2, ihabitat, ievolution]
    if entry.get() in pokemon_names:
        ipokemon_species = pb.pokemon_species(entry.get())
        ipokemon = pb.pokemon(ipokemon_species.id)

        itypes = [t.type.name for t in ipokemon.types]
        try:
            if itypes[1].capitalize() == None:
                print("WOW")
        except:
            itypes.append(None)
        ipokemon_color = ipokemon_species.color.name
        ipokemon_egg = ipokemon_species.egg_groups
        try:
            if ipokemon_egg[1].capitalize() == None:
                print("WOW")
        except:
            ipokemon_egg.append(None)
        ipokemon_gen = ipokemon_species.generation
        ipokemon_habitat = ipokemon_species.habitat
        ipokemon_evolution = 0
        ipokemon_evolution1 = None
        ipokemon_evolution2 = None
        ipokemon_evolution1 = ipokemon_species.evolves_from_species
        try:
            ipokemone = pb.pokemon_species(str(ipokemon_evolution1))
            ipokemon_evolution2 = ipokemone.evolves_from_species
        except:
            ipokemon_evolution2 = None

        if ipokemon_evolution1 != None:
            ipokemon_evolution += 1
        if ipokemon_evolution2 != None:
            ipokemon_evolution += 1

        if ipokemon.name == pokemon.name:
            iname = True
        if itypes[0] in types:
            ityper1 = True
        if itypes[1] in types:
            ityper2 = True
        if ipokemon_color == pokemon_color:
            icolor = True
        if str(ipokemon_egg[0]) in (str(pokemon_egg[0]), str(pokemon_egg[1])):
            iegg1 = True
        if str(ipokemon_egg[1]) in (str(pokemon_egg[0]), str(pokemon_egg[1])):
            iegg2 = True
        if ipokemon_gen.name == pokemon_gen.name:
            igen = True
        if ipokemon_habitat == None or pokemon_habitat == None:
            if pokemon_habitat == ipokemon_habitat:
                ihabitat = True
        else:
            if ipokemon_habitat.name == pokemon_habitat.name:
                ihabitat = True
        if ipokemon_evolution == pokemon_evolution:
            ievolution = True
        
        name_label = Label(root, text = f"{ipokemon.name.capitalize()}")
        name_label.grid(row=guess, column=quality, pady=10, padx=5)
        quality +=1

        gen_label = Label(root, text = f"{ipokemon_gen.name.capitalize()}", background="#888888")
        gen_label.grid(row=guess, column=quality, pady=10, padx=5)
        quality +=1

        color_label = Label(root, text = f"Color: {ipokemon_color.capitalize()}", background="#888888")
        color_label.grid(row=guess, column=quality, pady=10, padx=5)
        quality +=1

        if itypes[1] == None:
            type_label = Label(root, text = f"Types: {itypes[0].capitalize()}, {None}", background="#888888")
        else:
            type_label = Label(root, text = f"Types: {itypes[0].capitalize()}, {itypes[1].capitalize()}", background="#888888")
        type_label.grid(row=guess, column=quality, pady=10, padx=5)
        quality +=1

        if ipokemon_egg[1] == None:
            egg_label = Label(root, text = f"Egg Groups: {ipokemon_egg[0].name.capitalize()}, {None}", background="#888888")
        else:
            egg_label = Label(root, text = f"Egg Groups: {ipokemon_egg[0].name.capitalize()}, {ipokemon_egg[1].name.capitalize()}", background="#888888")
        egg_label.grid(row=guess, column=quality, pady=10, padx=5)
        quality +=1
        
        if ipokemon_habitat == None:
            habitat_label = Label(root, text = f"Habitat: {None}", background="#888888")
        else:
            habitat_label = Label(root, text = f"Habitat: {ipokemon_habitat.name.capitalize()}", background="#888888")
        habitat_label.grid(row=guess, column=quality, pady=10, padx=5)
        quality +=1

        evolution_label = Label(root, text = f"Evolution: {ipokemon_evolution}", background="#888888")
        evolution_label.grid(row=guess, column=quality, pady=10, padx=5)
        quality = 0
        guess += 1
        for widget in root.winfo_children():
            if widget._name == "lbb":
                border.destroy()
        border = Label(root, text=f"Guess: {guess-1}").grid(row=0, column=0, padx=30, pady=10)
        
        checky = 0
        ichecks = [iname,igen, icolor, ityper1, ityper2, iegg1, iegg2, ihabitat, ievolution]
        correct_color = "#00cc00"
        partial_collor = "#cccc00"
        if iname == True:
            name_label.configure(background=correct_color)
        if igen == True:
            gen_label.configure(background=correct_color)
        if icolor == True:
            color_label.configure(background=correct_color)
        if ityper1 == True and ityper2 == True:
            type_label.configure(background=correct_color)
        elif ityper1 == True or ityper2 == True:
            type_label.configure(background=partial_collor)
        if iegg1 == True and iegg2 == True:
            egg_label.configure(background=correct_color)
        elif iegg1 == True or iegg2 == True:
            egg_label.configure(background=partial_collor)
        if ihabitat == True:
            habitat_label.configure(background=correct_color)
        if ievolution == True:
            evolution_label.configure(background=correct_color)
        #print(ichecks)
        for check in ichecks:
            if check == True:
                checky +=1
        if checky == 9:
            name_label.configure(background=correct_color)
            entry.grid_remove()
            Button(
                root,
                text="Restart?", width=10,
                command=lambda: restarter(),
            ).grid(row=guess+1, column=4)
            Button(
                root,
                text="Nah", width=10,
                command=lambda: doner(),
            ).grid(row=guess+1, column=5)
        else:
            entry.grid_configure(row=entry.grid_info()["row"] + 1)
            quality +=1
    root.after(1000, lambda: entry.config(state="normal"))
    root.after(2000, cooldowner)
    pokemon_suggestions.place()

def restarter():
    global guess, quality, poke, entry, masterlable, border, base_label1, base_label2, base_label3, base_label4, base_label5, base_label6, base_label7
    for widget in root.winfo_children():
        if isinstance(widget, Label) or isinstance(widget, Button):
            widget.destroy()
    guess = 1
    quality = 1
    masterlable = Label(root, text = f"Input a pokemon's name into the feild below to start.", font=(30))
    masterlable.place(x=250)
    border = Label(root, text=f"Guess: {guess}").grid(row=0, column=0, padx=30, pady=10)
    base_label1 = Label(root, text="Name").grid(row=guess, column=quality, pady=10, padx=5)
    quality +=1
    base_label2 = Label(root, text="Generation").grid(row=guess, column=quality, pady=10, padx=5)
    quality +=1
    base_label3 = Label(root, text="Color").grid(row=guess, column=quality, pady=10, padx=5)
    quality +=1
    base_label4 = Label(root, text="Types: one two").grid(row=guess, column=quality, pady=10, padx=5)
    quality +=1
    base_label5 = Label(root, text="Egg Groupes: one two").grid(row=guess, column=quality, pady=10, padx=5)
    quality +=1
    base_label6 = Label(root, text="Habitats").grid(row=guess, column=quality, pady=10, padx=5)
    quality +=1
    base_label7 = Label(root, text="Evolution").grid(row=guess, column=quality, pady=10, padx=5)
    quality = 1
    guess += 1
    poke = random.randint(1,1025)
    #print(poke)
    get_wordle_pokemon(poke)
    entry.grid()
    entry.grid_configure(row=guess)

def doner():
    root.destroy()

def cooldowner():
    global cooldown
    cooldown = False


listfuncs = True
if listfuncs:
    def autocomplete(event):
        if event.keysym in ("Return", "Up", "Down", "Escape"):
            return

        typed = entry.get().lower()
        pokemon_suggestions.delete(0, END)

        if not typed:
            pokemon_suggestions.place_forget()
            return

        matches = [name for name in pokemon_names if name.startswith(typed)]

        for name in matches[:6]:
            pokemon_suggestions.insert(END, name)

        if matches:
            show_suggestions()
        else:
            pokemon_suggestions.place_forget()

    def select_pokemon(event):
        selection = pokemon_suggestions.curselection()

        if selection:
            selected = pokemon_suggestions.get(selection[0])

            entry.delete(0, END)
            entry.insert(0, selected)

            pokemon_suggestions.grid_remove()
            entry.focus_set()

    def show_suggestions():
        entry.update_idletasks()

        pokemon_suggestions.place(
            x=entry.winfo_x(),
            y=entry.winfo_y() + entry.winfo_height(),
            width=entry.winfo_width()
        )

        pokemon_suggestions.lift()

    def hide_suggestions(event):
        if event.widget not in (entry, pokemon_suggestions):
            pokemon_suggestions.place_forget()


pokemon_names = [ "Names:",
    "bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon",
    "charizard", "squirtle", "wartortle", "blastoise", "caterpie",
    "metapod", "butterfree", "weedle", "kakuna", "beedrill",
    "pidgey", "pidgeotto", "pidgeot", "rattata", "raticate",
    "spearow", "fearow", "ekans", "arbok", "pikachu",
    "raichu", "sandshrew", "sandslash", "nidoran-f", "nidorina",
    "nidoqueen", "nidoran-m", "nidorino", "nidoking", "clefairy",
    "clefable", "vulpix", "ninetales", "jigglypuff", "wigglytuff",
    "zubat", "golbat", "oddish", "gloom", "vileplume",
    "paras", "parasect", "venonat", "venomoth", "diglett",
    "dugtrio", "meowth", "persian", "psyduck", "golduck",
    "mankey", "primeape", "growlithe", "arcanine", "poliwag",
    "poliwhirl", "poliwrath", "abra", "kadabra", "alakazam",
    "machop", "machoke", "machamp", "bellsprout", "weepinbell",
    "victreebel", "tentacool", "tentacruel", "geodude", "graveler",
    "golem", "ponyta", "rapidash", "slowpoke", "slowbro",
    "magnemite", "magneton", "farfetchd", "doduo", "dodrio",
    "seel", "dewgong", "grimer", "muk", "shellder",
    "cloyster", "gastly", "haunter", "gengar", "onix",
    "drowzee", "hypno", "krabby", "kingler", "voltorb",
    "electrode", "exeggcute", "exeggutor", "cubone", "marowak",
    "hitmonlee", "hitmonchan", "lickitung", "koffing", "weezing",
    "rhyhorn", "rhydon", "chansey", "tangela", "kangaskhan",
    "horsea", "seadra", "goldeen", "seaking", "staryu",
    "starmie", "mr-mime", "scyther", "jynx", "electabuzz",
    "magmar", "pinsir", "tauros", "magikarp", "gyarados",
    "lapras", "ditto", "eevee", "vaporeon", "jolteon",
    "flareon", "porygon", "omanyte", "omastar", "kabuto",
    "kabutops", "aerodactyl", "snorlax", "articuno", "zapdos",
    "moltres", "dratini", "dragonair", "dragonite", "mewtwo",
    "mew",
# Generation II
    "chikorita", "bayleef", "meganium", "cyndaquil", "quilava",
    "typhlosion", "totodile", "croconaw", "feraligatr", "sentret",
    "furret", "hoothoot", "noctowl", "ledyba", "ledian",
    "spinarak", "ariados", "crobat", "chinchou", "lanturn",
    "pichu", "cleffa", "igglybuff", "togepi", "togetic",
    "natu", "xatu", "mareep", "flaaffy", "ampharos",
    "bellossom", "marill", "azumarill", "sudowoodo", "politoed",
    "hoppip", "skiploom", "jumpluff", "aipom", "sunkern",
    "sunflora", "yanma", "wooper", "quagsire", "espeon",
    "umbreon", "murkrow", "slowking", "misdreavus", "unown",
    "wobbuffet", "girafarig", "pineco", "forretress", "dunsparce",
    "gligar", "steelix", "snubbull", "granbull", "qwilfish",
    "scizor", "shuckle", "heracross", "sneasel", "teddiursa",
    "ursaring", "slugma", "magcargo", "swinub", "piloswine",
    "corsola", "remoraid", "octillery", "delibird", "mantine",
    "skarmory", "houndour", "houndoom", "kingdra", "phanpy",
    "donphan", "porygon2", "stantler", "smeargle", "tyrogue",
    "hitmontop", "smoochum", "elekid", "magby", "miltank",
    "blissey", "raikou", "entei", "suicune", "larvitar",
    "pupitar", "tyranitar", "lugia", "ho-oh", "celebi",

    # Generation III
    "treecko", "grovyle", "sceptile", "torchic", "combusken",
    "blaziken", "mudkip", "marshtomp", "swampert", "poochyena",
    "mightyena", "zigzagoon", "linoone", "wurmple", "silcoon",
    "beautifly", "cascoon", "dustox", "lotad", "lombre",
    "ludicolo", "seedot", "nuzleaf", "shiftry", "taillow",
    "swellow", "wingull", "pelipper", "ralts", "kirlia",
    "gardevoir", "surskit", "masquerain", "shroomish", "breloom",
    "slakoth", "vigoroth", "slaking", "nincada", "ninjask",
    "shedinja", "whismur", "loudred", "exploud", "makuhita",
    "hariyama", "azurill", "nosepass", "skitty", "delcatty",
    "sableye", "mawile", "aron", "lairon", "aggron",
    "meditite", "medicham", "electrike", "manectric", "plusle",
    "minun", "volbeat", "illumise", "roselia", "gulpin",
    "swalot", "carvanha", "sharpedo", "wailmer", "wailord",
    "numel", "camerupt", "torkoal", "spoink", "grumpig",
    "spinda", "trapinch", "vibrava", "flygon", "cacnea",
    "cacturne", "swablu", "altaria", "zangoose", "seviper",
    "lunatone", "solrock", "barboach", "whiscash", "corphish",
    "crawdaunt", "baltoy", "claydol", "lileep", "cradily",
    "anorith", "armaldo", "feebas", "milotic", "castform",
    "kecleon", "shuppet", "banette", "duskull", "dusclops",
    "tropius", "chimecho", "absol", "wynaut", "snorunt",
    "glalie", "spheal", "sealeo", "walrein", "clamperl",
    "huntail", "gorebyss", "relicanth", "luvdisc", "bagon",
    "shelgon", "salamence", "beldum", "metang", "metagross",
    "regirock", "regice", "registeel", "latias", "latios",
    "kyogre", "groudon", "rayquaza", "jirachi", "deoxys",

    # Generation IV
    "turtwig", "grotle", "torterra", "chimchar", "monferno",
    "infernape", "piplup", "prinplup", "empoleon", "starly",
    "staravia", "staraptor", "bidoof", "bibarel", "kricketot",
    "kricketune", "shinx", "luxio", "luxray", "budew",
    "roserade", "cranidos", "rampardos", "shieldon", "bastiodon",
    "burmy", "wormadam", "mothim", "combee", "vespiquen",
    "pachirisu", "buizel", "floatzel", "cherubi", "cherrim",
    "shellos", "gastrodon", "ambipom", "drifloon", "drifblim",
    "buneary", "lopunny", "mismagius", "honchkrow", "glameow",
    "purugly", "chingling", "stunky", "skuntank", "bronzor",
    "bronzong", "bonsly", "mime-jr", "happiny", "chatot",
    "spiritomb", "gible", "gabite", "garchomp", "munchlax",
    "riolu", "lucario", "hippopotas", "hippowdon", "skorupi",
    "drapion", "croagunk", "toxicroak", "carnivine", "finneon",
    "lumineon", "mantyke", "snover", "abomasnow", "weavile",
    "magnezone", "lickilicky", "rhyperior", "tangrowth", "electivire",
    "magmortar", "togekiss", "yanmega", "leafeon", "glaceon",
    "gliscor", "mamoswine", "porygon-z", "gallade", "probopass",
    "dusknoir", "froslass", "rotom", "uxie", "mesprit",
    "azelf", "dialga", "palkia", "heatran", "regigigas",
    "giratina", "cresselia", "phione", "manaphy", "darkrai",
    "shaymin", "arceus",

    # Generation V
    "victini", "snivy", "servine", "serperior", "tepig",
    "pignite", "emboar", "oshawott", "dewott", "samurott",
    "patrat", "watchog", "lillipup", "herdier", "stoutland",
    "purrloin", "liepard", "pansage", "simisage", "pansear",
    "simisear", "panpour", "simipour", "munna", "musharna",
    "pidove", "tranquill", "unfezant", "blitzle", "zebstrika",
    "roggenrola", "boldore", "gigalith", "woobat", "swoobat",
    "drilbur", "excadrill", "audino", "timburr", "gurdurr",
    "conkeldurr", "tympole", "palpitoad", "seismitoad", "throh",
    "sawk", "sewaddle", "swadloon", "leavanny", "venipede",
    "whirlipede", "scolipede", "cottonee", "whimsicott", "petilil",
    "lilligant", "basculin", "sandile", "krokorok", "krookodile",
    "darumaka", "darmanitan", "maractus", "dwebble", "crustle",
    "scraggy", "scrafty", "sigilyph", "yamask", "cofagrigus",
    "tirtouga", "carracosta", "archen", "archeops", "trubbish",
    "garbodor", "zorua", "zoroark", "minccino", "cinccino",
    "gothita", "gothorita", "gothitelle", "solosis", "duosion",
    "reuniclus", "ducklett", "swanna", "vanillite", "vanillish",
    "vanilluxe", "deerling", "sawsbuck", "emolga", "karrablast",
    "escavalier", "foongus", "amoonguss", "frillish", "jellicent",
    "alomomola", "joltik", "galvantula", "ferroseed", "ferrothorn",
    "klink", "klang", "klinklang", "tynamo", "eelektrik",
    "eelektross", "elgyem", "beheeyem", "litwick", "lampent",
    "chandelure", "axew", "fraxure", "haxorus", "cubchoo",
    "beartic", "cryogonal", "shelmet", "accelgor", "stunfisk",
    "mienfoo", "mienshao", "druddigon", "golett", "golurk",
    "pawniard", "bisharp", "bouffalant", "rufflet", "braviary",
    "vullaby", "mandibuzz", "heatmor", "durant", "deino",
    "zweilous", "hydreigon", "larvesta", "volcarona", "cobalion",
    "terrakion", "virizion", "tornadus", "thundurus", "reshiram",
    "zekrom", "landorus", "kyurem", "keldeo", "meloetta",
    "genesect",

    # Generation VI
    "chespin", "quilladin", "chesnaught", "fennekin", "braixen",
    "delphox", "froakie", "frogadier", "greninja", "bunnelby",
    "diggersby", "fletchling", "fletchinder", "talonflame", "scatterbug",
    "spewpa", "vivillon", "litleo", "pyroar", "flabebe",
    "floette", "florges", "skiddo", "gogoat", "pancham",
    "pangoro", "furfrou", "espurr", "meowstic", "honedge",
    "doublade", "aegislash", "spritzee", "aromatisse", "swirlix",
    "slurpuff", "inkay", "malamar", "binacle", "barbaracle",
    "skrelp", "dragalge", "clauncher", "clawitzer", "helioptile",
    "heliolisk", "tyrunt", "tyrantrum", "amaura", "aurorus",
    "sylveon", "hawlucha", "dedenne", "carbink", "goomy",
    "sliggoo", "goodra", "klefki", "phantump", "trevenant",
    "pumpkaboo", "gourgeist", "bergmite", "avalugg", "noibat",
    "noivern", "xerneas", "yveltal", "zygarde", "diancie",
    "hoopa", "volcanion",

    # Generation VII
    "rowlet", "dartrix", "decidueye", "litten", "torracat",
    "incineroar", "popplio", "brionne", "primarina", "pikipek",
    "trumbeak", "toucannon", "yungoos", "gumshoos", "grubbin",
    "charjabug", "vikavolt", "crabrawler", "crabominable", "oricorio",
    "cutiefly", "ribombee", "rockruff", "lycanroc", "wishiwashi",
    "mareanie", "toxapex", "mudbray", "mudsdale", "dewpider",
    "araquanid", "fomantis", "lurantis", "morelull", "shiinotic",
    "salandit", "salazzle", "stufful", "bewear", "bounsweet",
    "steenee", "tsareena", "comfey", "oranguru", "passimian",
    "wimpod", "golisopod", "sandygast", "palossand", "pyukumuku",
    "type-null", "silvally", "minior", "komala", "turtonator",
    "togedemaru", "mimikyu", "bruxish", "drampa", "dhelmise",
    "jangmo-o", "hakamo-o", "kommo-o", "tapu-koko", "tapu-lele",
    "tapu-bulu", "tapu-fini", "cosmog", "cosmoem", "solgaleo",
    "lunala", "nihilego", "buzzwole", "pheromosa", "xurkitree",
    "celesteela", "kartana", "guzzlord", "necrozma", "magearna",
    "marshadow", "poipole", "naganadel", "stakataka", "blacephalon",
    "zeraora", "meltan", "melmetal",

    # Generation VIII
    "grookey", "thwackey", "rillaboom", "scorbunny", "raboot",
    "cinderace", "sobble", "drizzile", "inteleon", "skwovet",
    "greedent", "rookidee", "corvisquire", "corviknight", "blipbug",
    "dottler", "orbeetle", "nickit", "thievul", "gossifleur",
    "eldegoss", "wooloo", "dubwool", "chewtle", "drednaw",
    "yamper", "boltund", "rolycoly", "carkol", "coalossal",
    "applin", "flapple", "appletun", "silicobra", "sandaconda",
    "cramorant", "arrokuda", "barraskewda", "toxel", "toxtricity",
    "sizzlipede", "centiskorch", "clobbopus", "grapploct", "sinistea",
    "polteageist", "hatenna", "hattrem", "hatterene", "impidimp",
    "morgrem", "grimmsnarl", "obstagoon", "perrserker", "cursola",
    "sirfetchd", "mr-rime", "runerigus", "milcery", "alcremie",
    "falinks", "pincurchin", "snom", "frosmoth", "stonjourner",
    "eiscue", "indeedee", "morpeko", "cufant", "copperajah",
    "dracozolt", "arctozolt", "dracovish", "arctovish", "duraludon",
    "dreepy", "drakloak", "dragapult", "zacian", "zamazenta",
    "eternatus", "kubfu", "urshifu", "zarude", "regieleki",
    "regidrago", "glastrier", "spectrier", "calyrex", "wyrdeer",
    "kleavor", "ursaluna", "basculegion", "sneasler", "overqwil",
    "enamorus",

    # Generation IX
    "sprigatito", "floragato", "meowscarada", "fuecoco", "crocalor",
    "skeledirge", "quaxly", "quaxwell", "quaquaval", "lechonk",
    "oinkologne", "tarountula", "spidops", "nymble", "lokix",
    "pawmi", "pawmo", "pawmot", "tandemaus", "maushold",
    "fidough", "dachsbun", "smoliv", "dolliv", "arboliva",
    "squawkabilly", "nacli", "naclstack", "garganacl", "charcadet",
    "armarouge", "ceruledge", "tadbulb", "bellibolt", "wattrel",
    "kilowattrel", "maschiff", "mabosstiff", "shroodle", "grafaiai",
    "bramblin", "brambleghast", "toedscool", "toedscruel", "klawf",
    "capsakid", "scovillain", "rellor", "rabsca", "flittle",
    "espathra", "tinkatink", "tinkatuff", "tinkaton", "wiglett",
    "wugtrio", "bombirdier", "finizen", "palafin", "varoom",
    "revavroom", "cyclizar", "orthworm", "glimmet", "glimmora",
    "greavard", "houndstone", "flamigo", "cetoddle", "cetitan",
    "veluza", "dondozo", "tatsugiri", "annihilape", "clodsire",
    "farigiraf", "dudunsparce", "kingambit", "great-tusk", "scream-tail",
    "brute-bonnet", "flutter-mane", "slither-wing", "sandy-shocks",
    "iron-treads", "iron-bundle", "iron-hands", "iron-jugulis",
    "iron-moth", "iron-thorns", "frigibax", "arctibax", "baxcalibur",
    "gimmighoul", "gholdengo", "wo-chien", "chien-pao", "ting-lu",
    "chi-yu", "roaring-moon", "iron-valiant", "koraidon", "miraidon",
    "walking-wake", "iron-leaves", "dipplin", "poltchageist", "sinistcha",
    "okidogi", "munkidori", "fezandipiti", "ogerpon", "archaludon",
    "hydrapple", "gouging-fire", "raging-bolt", "iron-boulder",
    "iron-crown", "terapagos", "pecharunt"]
gen = 0
cooldown = False

poke = random.randint(1,1025)
#poke = 311
#print(poke)

get_wordle_pokemon(poke)

guess = 1
quality = 1

base_label1 = Label(root, text="Name", background="#cc0000", foreground="#33cccc", name="lb1").grid(row=guess, column=quality, pady=10, padx=5)
quality +=1
base_label2 = Label(root, text="Generation", background="#cc5000", foreground="#33a0cc", name="lb2").grid(row=guess, column=quality, pady=10, padx=5)
quality +=1
base_label3 = Label(root, text="Color", background="#cccc00", foreground="#3333cc", name="lb3").grid(row=guess, column=quality, pady=10, padx=5)
quality +=1
base_label4 = Label(root, text="Types: one two", background="#00cc00", foreground="#cc33cc", name="lb4").grid(row=guess, column=quality, pady=10, padx=5)
quality +=1
base_label5 = Label(root, text="Egg Groupes: one two", background="#0000cc", foreground="#cccc33", name="lb5").grid(row=guess, column=quality, pady=10, padx=5)
quality +=1
base_label6 = Label(root, text="Habitats", background="#4000cc", foreground="#b0cc33", name="lb6").grid(row=guess, column=quality, pady=10, padx=5)
quality +=1
base_label7 = Label(root, text="Evolution", background="#9000cc", foreground="#6ccc33", name="lb7").grid(row=guess, column=quality, pady=10, padx=5)
quality = 1
guess += 1

masterlable = Label(root, text = f"Input a pokemon's name into the field below to start.", font=(30), name="lbm")
masterlable.place(x=250)
border = Label(root, text=f"Guess: {guess-1}", name="lbb")
border.grid(row=0, column=0, padx=30, pady=10)

entry = Entry(
    root, width=12, name= "pokemon",
    background= "#FFFFFF"
    )
entry.grid(row=guess, column=quality)
entry.bind("<KeyRelease>", autocomplete)
entry.bind("<Return>", get_pokemon)
entry.insert(0, "bulbasaur")

pokemon_suggestions = Listbox(
    entry.master,
    height=6,
    width=12,
    background="#FFFFFF",
    selectbackground="#ADD8E6",
    exportselection=False
)

pokemon_suggestions.place_forget()
pokemon_suggestions.bind("<ButtonRelease-1>", select_pokemon)
root.bind("<Button-1>", hide_suggestions)

root.mainloop()
