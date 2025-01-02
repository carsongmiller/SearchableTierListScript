import re
import urllib.request

birdList = []
wingsearchHTMLFileName = "Wingsearch - Wingspan cards search.html"
tierListHTMLFileName = "Wingspan Bird Card Tier List • Wingsplain.html"

with open(wingsearchHTMLFileName, 'r', encoding='utf-8') as file:
    wingsearchHTML = file.read()
    birdList = re.findall("assets\/cards\/birds\/(\d*)[\S\s]*?class=\"title\".*?c87=\"\">(.*)<\/span>", wingsearchHTML)
    # sanitize
    birdList = [(x[0], x[1].strip()) for x in birdList]

# clean up some names that are different between wingsearch and wingsplain
for i in range(len(birdList)):
    bird = birdList[i]
    match bird[1]:
        case "Abbott's Booby":
            birdList[i] = (bird[0], "Abbot's Booby")
        case "Black-Headed Gull":
            birdList[i] = (bird[0], "Black Headed Gull")
        case "Ash-Throated Flycatcher":
            birdList[i] = (bird[0], "Ash Throated Flycatcher")
        case "Black-Throated Diver":
            birdList[i] = (bird[0], "Black Throated Diver")
        case "Australian Owlet-Nightjar":
            birdList[i] = (bird[0], "Australian Owlet Nightjar")
        case "Broad-Winged Hawk":
            birdList[i] = (bird[0], "Broad Winged Hawk")
        case "Black-Chinned Hummingbird":
            birdList[i] = (bird[0], "Black Chinned Hummingbird")
        case "Black-Crowned Night-Heron":
            birdList[i] = (bird[0], "Black Crowned Night Heron")
        case "Brown-Headed Cowbird":
            birdList[i] = (bird[0], "Brown Headed Cowbird")
        case "Black-Bellied Whistling Duck":
            birdList[i] = (bird[0], "Black Bellied Whistling Duck")
        case "Black-Billed Magpie":
            birdList[i] = (bird[0], "Black Billed Magpie")
        case "Pied-Billed Grebe":
            birdList[i] = (bird[0], "Pied Billed Grebe")
        case "Black-Tailed Godwit":
            birdList[i] = (bird[0], "Black Tailed Godwit")
        case "Black-Necked Stilt":
            birdList[i] = (bird[0], "Black Necked Stilt")
        case "Black-Shouldered Kite":
            birdList[i] = (bird[0], "Black Shouldered Kite")
        case "Red-Breasted Merganser":
            birdList[i] = (bird[0], "Red Breasted Merganser")
        case "Blue-Gray Gnatcatcher":
            birdList[i] = (bird[0], "Blue Grey Gnatcatcher")
        case "Chestnut-Collared Longspur":
            birdList[i] = (bird[0], "Chestnut Collared Longspur")
        case "Rose-Ringed Parakeet":
            birdList[i] = (bird[0], "Rose Ringed Parakeet")
        case "Blue-Winged Warbler":
            birdList[i] = (bird[0], "Blue Winged Warbler")
        case "Count Raggi's Bird-of-Paradise":
            birdList[i] = (bird[0], "Count Raggi's Bird of Paradise")
        case "White-Throated Dipper":
            birdList[i] = (bird[0], "White Throated Dipper")
        case "Dark-Eyed Junco":
            birdList[i] = (bird[0], "Dark Eyed Junco")
        case "Eurasian Collared-Dove":
            birdList[i] = (bird[0], "Eurasian Collared Dove")
        case "Graceful Prinia":
            birdList[i] = (bird[0], "Graceful Prina")
        case "Double-Crested Cormorant":
            birdList[i] = (bird[0], "Double Crested Cormorant")
        case "Grey-Headed Mannikin":
            birdList[i] = (bird[0], "Grey Headed Mannikin")
        case "Kākāpō":
            birdList[i] = (bird[0], "Kakapo")
        case "Magpie-Lark":
            birdList[i] = (bird[0], "Magpie Lark")
        case "Many-Colored Fruit Dove":
            birdList[i] = (bird[0], "Many Colored Fruit Dove")
        case "Green Pygmy-Goose":
            birdList[i] = (bird[0], "Green Pygmy Goose")
        case "Long-Tailed Tit":
            birdList[i] = (bird[0], "Long Tailed Tit")
        case "Horsfield's Bronze-Cuckoo":
            birdList[i] = (bird[0], "Horsfield's Bronze Cuckoo")
        case "Kererū":
            birdList[i] = (bird[0], "Kereru")
        case "Orange-Footed Scrubfowl":
            birdList[i] = (bird[0], "Orange Footed Scrubfowl")
        case "Red-Breasted Nuthatch":
            birdList[i] = (bird[0], "Red Breasted Nuthatch")
        case "Plains-Wanderer":
            birdList[i] = (bird[0], "Plains Wanderer")
        case "Red-Legged Partridge":
            birdList[i] = (bird[0], "Red Legged Partridge")
        case "Red-Winged Blackbird":
            birdList[i] = (bird[0], "Red Winged Black Bird")
        case "Red-Backed Fairywren":
            birdList[i] = (bird[0], "Red Backed Fairywren")
        case "Ruby-Throated Hummingbird":
            birdList[i] = (bird[0], "Ruby Throated Hummingbird")
        case "Red-Cockaded Woodpecker":
            birdList[i] = (bird[0], "Red Cockaded Woodpecker")
        case "Red-Eyed Vireo":
            birdList[i] = (bird[0], "Red Eyed Vireo")
        case "Red-Headed Woodpecker":
            birdList[i] = (bird[0], "Red Headed Woodpecker")
        case "Red-Winged Parrot":
            birdList[i] = (bird[0], "Red Winged Parrot")
        case "Scissor-Tailed Flycatcher":
            birdList[i] = (bird[0], "Scissor Tailed Flycatcher")
        case "Pink-Eared Duck":
            birdList[i] = (bird[0], "Pink Eared Duck")
        case "Pūkeko":
            birdList[i] = (bird[0], "Pukeko")
        case "Ring-Billed Gull":
            birdList[i] = (bird[0], "Ring Billed Gull")
        case "Rose-Breasted Grosbeak":
            birdList[i] = (bird[0], "Rose Breasted Grosbeak")
        case "Ruby-Crowned Kinglet":
            birdList[i] = (bird[0], "Ruby Crowned Kinglet")
        case "Red-Backed Shrike":
            birdList[i] = (bird[0], "Red Backed Shrike")
        case "Red-Bellied Woodpecker":
            birdList[i] = (bird[0], "Red Bellied Woodpecker")
        case "Red-Capped Robin":
            birdList[i] = (bird[0], "Red Capped Robin")
        case "Wedge-Tailed Eagle":
            birdList[i] = (bird[0], "Wedge Tailed Eagle")
        case "White-Backed Woodpecker":
            birdList[i] = (bird[0], "White Backed Woodpecker")
        case "White-Bellied Sea-Eagle":
            birdList[i] = (bird[0], "White Bellied Sea Eagle")
        case "Short-Toed Treecreeper":
            birdList[i] = (bird[0], "Short Toed Treecreeper")
        case "Red-Necked Avocet":
            birdList[i] = (bird[0], "Red Necked Avocet")
        case "White-Breasted Nuthatch":
            birdList[i] = (bird[0], "White Breasted Nuthatch")
        case "Red-Shouldered Hawk":
            birdList[i] = (bird[0], "Red Shouldered Hawk")
        case "Red-Tailed Hawk":
            birdList[i] = (bird[0], "Red Tailed Hawk")
        case "White-Faced Ibis":
            birdList[i] = (bird[0], "White Faced Ibis")
        case "White-Throated Swift":
            birdList[i] = (bird[0], "White Throated Swift")
        case "Rufous-Banded Honeyeater":
            birdList[i] = (bird[0], "Rufous Banded Honeyeater")
        case "Rufous Night-Heron":
            birdList[i] = (bird[0], "Rufous Night Heron")
        case "Wood Stork":
            birdList[i] = (bird[0], "Woodstork")
        case "Violet-Green Swallow":
            birdList[i] = (bird[0], "Violet Green Swallow")
        case "White-Breasted Woodswallow":
            birdList[i] = (bird[0], "White Breasted Woodswallow")
        case "Steller's Jay":
            birdList[i] = (bird[0], "Stellar's Jay")
        case "Sulphur-Crested Cockatoo":
            birdList[i] = (bird[0], "Sulphur Crested Cockatoo")
        case "Yellow-Billed Cuckoo":
            birdList[i] = (bird[0], "Yellow Billed Cuckoo")
        case "Yellow-Headed Blackbird":
            birdList[i] = (bird[0], "Yellow Headed Blackbird")
        case "European Bee-Eater":
            birdList[i] = (bird[0], "European Bee Eater")
        case "Willie-Wagtail":
            birdList[i] = (bird[0], "Willie Wagtail")
        case "Tūī":
            birdList[i] = (bird[0], "Tui")
        case "White-Crowned Sparrow":
            birdList[i] = (bird[0], "White Crowned Sparrow")
        case "White-Faced Heron":
            birdList[i] = (bird[0], "White Faced Heron")
        case "Yellow-Bellied Sapsucker":
            birdList[i] = (bird[0], "Yellow Bellied Sapsucker")
        case "Yellow-Breasted Chat":
            birdList[i] = (bird[0], "Yellow Breasted Chat")
        case "Yellow-Rumped Warbler":
            birdList[i] = (bird[0], "Yellow Rumped Warbler")
        case "Golden-Headed Cisticola":
            birdList[i] = (bird[0], "Golden Headed Cisticola")


with open(tierListHTMLFileName, 'r', encoding='utf-8') as fileRead:
    tierListHTML = fileRead.read()
    for match in birdList:
        tierListHTML = re.sub(match[1], "<a href=\"https://navarog.github.io/wingsearch/card/" + match[0] + "\">" + match[1] + "</a>", tierListHTML)

    fileWrite = open("madeSearchable.html", "w", encoding='utf-8')
    fileWrite.write(tierListHTML)
    fileWrite.close()