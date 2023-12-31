### Purpose of the Script:
The provided script generates `.cdf` files for a card game based on specific rules derived from the filenames of card images.

### Steps to Use the Script:

1. **Open a Text Editor:**
   - Open a text editor of your choice (e.g., VSCode, Notepad++, etc.) to view and modify the script.

2. **Download and Install Python:**
   - Ensure that you have Python installed on your computer. If not, download and install it from [Python's official website](https://www.python.org/).

3. **Install Required Packages:**
   - Open a terminal or command prompt and run the following command to install the required package (Pillow):
     ```
     pip install Pillow
     ```

4. **Organize Card Images:**
   - Organize your card images in a folder structure similar to the one specified in the script. For example, place your card images in a folder like `../../Assets/[DIRPATHINSERT]`.

5. **Modify the Script:**
   - Open the script in your text editor.
   - Replace `[DIRPATHINSERT]` with the correct folder path where your card images are stored.

6. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where you saved the script using the `cd` command.
   - Run the script using the following command:
     ```
     python script_name.py
     ```
     Replace `script_name.py` with the actual name of the script.

7. **Review Output:**
   - The script will generate `.cdf` files based on the specified rules and place them in the same directory as your card images.

8. **Check Output Files:**
   - Review the generated `.cdf` files to ensure they meet your expectations. Each file corresponds to a card image.

9. **Troubleshooting:**
   - If you encounter any errors, carefully review the script and ensure that you've followed the instructions for modifying the script.

10. **Customization (Optional):**
   - If needed, you can customize the script further by adjusting the rules for rarity, drop weight, category, and description.

11. **Iterate if Necessary:**
   - If your card images follow a different naming convention, you may need to iterate on the script and make adjustments accordingly.

### Script Explanation:

- **`get_rarity_from_filename(filename)`:** Extracts the rarity of the card from the filename.

- **`get_drop_weight(rarity)`:** Retrieves the drop weight based on the card's rarity.

- **`extract_category_and_description(filename)`:** Extracts the category and description from the filename using parentheses and square brackets, respectively.

- **`generate_cdf_file(card_image_path)`:** Creates a `.cdf` file for each card image based on the specified rules. The file includes metadata such as card ID, rarity, name, category, drop weight, illustration path, and optional description.

- **`cards_folder`:** Specifies the folder where the script looks for card images. Modify this path to match the location of your card images.

### Image Naming Scheme:

#### Card Image Filename Structure:
- The script expects card image filenames to follow a specific structure. Here's an example: `001_Curve_Hopper_rare.png`

#### Components of the Filename:
1. **Card ID (001):** A unique identifier for each card. This should be a numeric value.
2. **Name (Curve Hopper):** The name of the card. Multiple words are separated by underscores.
3. **Rarity (rare):** The rarity of the card. This is indicated by a suffix at the end of the filename.

#### Rarity Suffixes:
- Common: `com`
- Uncommon: `unc`
- Rare: `rare`
- Ancient: `anc`
- Legendary: `leg`

#### Optional Components for Description and Category:
- You can include additional information in the filename using parentheses and square brackets.

   - **Description (e.g., Healing Card):**
     - Example: `002_Healing_Card_common(Healing Card).png`

   - **Category (e.g., Nature):**
     - Example: `003_Nature_Card_rare[Nature].png`

#### Example Filename:
- `001_Curve_Hopper_rare.png` indicates a card with ID 001, named "Curve Hopper," and has a rarity of "rare."

### Notes on Image Naming:
- Ensure that each card image follows the specified structure.
- The script uses this structure to extract information such as card ID, name, rarity, description, and category.

That's it! With the correct image naming scheme, the script will be able to generate `.cdf` files accurately.

### Notes:
- Ensure your card images follow the expected naming conventions and folder structure.
- Review the generated `.cdf` files to verify the correctness of the metadata.

That's it! You should now have successfully used the script to generate `.cdf` files for your card game. If you have any questions or encounter issues, feel free to ask for assistance.
