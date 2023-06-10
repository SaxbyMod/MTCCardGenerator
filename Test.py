import os
import re

def generate_cdf_file(card_image_path):
    card_id = os.path.splitext(os.path.basename(card_image_path))[0].split("_", 1)[1].replace(" ", "_").lower()
    card_id = re.sub(r'\W+', '_', card_id)
    card_id = f'card_{card_id}'

    image_name = os.path.splitext(os.path.basename(card_image_path))[0].split("_", 1)[1]

    illustration_path = f'Inscryption_Extras/{os.path.splitext(os.path.basename(card_image_path))[0]}'

    cdf_data = f'''
EditionID=inscryption_extras
CardID={card_id}
RarityLevel=common

Name={image_name}
Category=Inscryption Extras
DropWeight=10

IllustrationPath={illustration_path}
'''

    cdf_name = os.path.splitext(os.path.basename(card_image_path))[0]
    cdf_name = re.sub(r'\W+', '_', cdf_name)
    cdf_name = f'{cdf_name}.cdf'

    with open(cdf_name, 'w') as file:
        file.write(cdf_data)

# Fetching images from 2 folders up > Assets > Inscryption_Finale_Cards
cards_folder = os.path.abspath(os.path.join(os.getcwd(), "../../Assets/Inscryption_Extras"))
for filename in os.listdir(cards_folder):
    if filename.endswith(".png"):
        card_image_path = os.path.join(cards_folder, filename)
        generate_cdf_file(card_image_path)
