import os
import re

def get_rarity_from_filename(filename):
    suffix_match = re.search(r'_(com|common|unc|uncommon|rare|anc|ancient|leg|legendary)\.png$', filename, flags=re.IGNORECASE)
    if suffix_match:
        return suffix_match.group(1).lower()
    else:
        return 'common'

def generate_cdf_file(card_image_path):
    card_id = os.path.splitext(os.path.basename(card_image_path))[0].split("_", 1)[1].replace(" ", "_").lower()
    card_id = re.sub(r'\W+', '_', card_id)
    card_id = f'card_{card_id}'

    image_name = os.path.splitext(os.path.basename(card_image_path))[0].split("_", 1)[1]

    illustration_path = f'inscryption act 2 art pack/{os.path.splitext(os.path.basename(card_image_path))[0]}'

    rarity = get_rarity_from_filename(os.path.basename(card_image_path))

    cdf_data = f'''
EditionID=inscryption_act_2_art_pack
CardID={card_id}
RarityLevel={rarity}

Name={image_name}
Category=Inscryption Act2 Art Pack
DropWeight=10

IllustrationPath={illustration_path}
'''

    cdf_name = os.path.splitext(os.path.basename(card_image_path))[0]
    cdf_name = re.sub(r'\W+', '_', cdf_name)
    cdf_name = f'{cdf_name}.cdf'

    with open(cdf_name, 'w') as file:
        file.write(cdf_data)

# Fetching images from 2 folders up > Assets > Inscryption_Finale_Cards
cards_folder = os.path.abspath(os.path.join(os.getcwd(), "../../Assets/inscryption act 2 art pack"))
for filename in os.listdir(cards_folder):
    if filename.endswith(".png"):
        card_image_path = os.path.join(cards_folder, filename)
        generate_cdf_file(card_image_path)
