#ver1.01
import json
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
from sys import argv


# BodySlide options, to be completed
bodyslide_elems = [
    "Ankles",
    "AppleCheeks",
    "Arms",
    "Back",
    "Belly",
    "BigBelly",
    "BigButt",
    "BigTorso",
    "BreastCleavage",
    "BreastFlatness",
    "BreastGravity",
    "BreastHeight",
    "BreastPerkiness",
    "Breasts",
    "BreastsFantasy",
    "BreastsSH",
    "BreastsSmall",
    "BreastsSSH",
    "BreastWidth",
    "Butt",
    "ButtCrack",
    "ButtShape2",
    "ButtSmall",
    "CalfSize",
    "CalfSmooth",
    "ChubbyArms",
    "ChubbyButt",
    "ChubbyLegs",
    "ChubbyWaist",
    "DoubleMelon",
    "Groin",
    "HipBone",
    "Hips",
    "KneeHeight",
    "Legs",
    "NippleAreola",
    "NippleDistance",
    "NippleDown",
    "NippleLength",
    "NippleSize",
    "NippleTip",
    "NippleUp",
    "NipplePerkiness",
    "RoundAss",
    "PushUp",
    "ShoulderSmooth",
    "ShoulderWidth",
    "SlimThighs",
    "Thighs",
    "TummyTuck",
    "Waist",
    "WideWaistLine",
]


def load_json(file):
    """Load and parse JSON file, handling any JSON errors."""
    try:
        with open(file, 'r') as handle:
            parsed = json.load(handle)
        return parsed
    except json.JSONDecodeError as e:
        # Log error message and skip the file
        error_message = f"Skipping file due to JSONDecodeError at {file}: {str(e)}"
        print(error_message)
        log_error(error_message)
        return None  # Return None for invalid JSON


def save_xml(file, data):
    """Saves the file to the fixed directory: /output/CalienteTools/BodySlide/SliderPresets/."""
    # Define the output directory
    output_dir = os.path.join(os.getcwd(), 'output', 'CalienteTools', 'BodySlide', 'SliderPresets')
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, f"{file}.xml")
    with open(output_path, 'w') as handle:
        handle.write(prettify(data.getroot()))


def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = MD.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


def log_error(message):
    """Append error message to an error log file."""
    error_log_path = os.path.join(os.getcwd(), 'error_log.txt')
    with open(error_log_path, 'a') as error_log:
        error_log.write(message + '\n')


def convert_racemenu_2_bodyslide(file_path: str, small_size_modifier: float = 0.5, big_size_modifier: float = 1.5,
                                 group_name: str = None, body_name: str = None):
    try:
        # Read input file
        input_data = load_json(file_path)

        # Skip processing if JSON is invalid
        if input_data is None:
            return

        # Get bodyMorph node
        body_morph = input_data['bodyMorphs']  # This might raise KeyError if 'bodyMorphs' is missing
        size = 'small' if input_data['actor']['weight'] < 50 else 'big'

        # Fill missing entries
        for e in bodyslide_elems:
            if e not in [a['name'] for a in body_morph]:
                body_morph.append({
                    'name': e,
                    'keys': [{'value': 0}]  # Providing default value for missing 'keys'
                })

        # Build XML
        r = ET.Element('SliderPresets')
        tree = ET.ElementTree(r)
        root = tree.getroot()

        file_name = os.path.splitext(os.path.basename(file_path))[0]
        preset = ET.SubElement(root, 'Preset')
        preset.attrib['name'] = file_name
        preset.attrib['set'] = body_name if body_name else file_name + " body"

        if group_name:
            group = ET.SubElement(preset, 'Group')
            group.attrib['name'] = group_name

        # Calculate new values
        for entry in body_morph:
            # Check if 'keys' exists and has valid data
            if 'keys' not in entry or not isinstance(entry['keys'], list):
                error_message = f"Missing 'keys' in bodyMorph entry for '{entry.get('name', 'Unknown')}' in {file_path}"
                print(error_message)
                log_error(error_message)
                continue  # Skip to the next entry if 'keys' is missing

            # Sum the 'value' fields from 'keys'
            value = sum(key.get('value', 0) for key in entry['keys'])
            name = entry['name']

            if name not in bodyslide_elems:
                bodyslide_elems.append(name)

            value_new = round(value * 100)
            slider = ET.SubElement(preset, 'SetSlider')
            slider.attrib['name'] = name
            slider.attrib['size'] = "small"
            slider.attrib['value'] = str(round(value_new * small_size_modifier)) if size == "small" else str(value_new)

            slider = ET.SubElement(preset, 'SetSlider')
            slider.attrib['name'] = name
            slider.attrib['size'] = "big"
            slider.attrib['value'] = str(round(value_new * big_size_modifier)) if size == "big" else str(value_new)

        save_xml(file_name, tree)

    except KeyError as e:
        if str(e) == "'bodyMorphs'":
            # Log the error, showing the file name and path
            error_message = f"Skipping file due to missing 'bodyMorphs': {file_path}"
            print(error_message)
            log_error(error_message)  # Write the error to an error log file
        else:
            raise  # Raise other unexpected KeyErrors


if __name__ == "__main__":
    try:
        # Recursively walk through directories
        for root, dirs, files in os.walk(os.getcwd()):
            # Skip the output directory to avoid processing the generated files
            if 'output' in dirs:
                dirs.remove('output')

            for file in files:
                if file.endswith('.jslot'):
                    file_path = os.path.join(root, file)
                    # Convert with appropriate arguments
                    if len(argv) > 1:
                        if len(argv) == 2:
                            convert_racemenu_2_bodyslide(file_path, float(argv[1]))
                        elif len(argv) == 3:
                            convert_racemenu_2_bodyslide(file_path, float(argv[1]), float(argv[2]))
                        elif len(argv) == 4:
                            convert_racemenu_2_bodyslide(file_path, float(argv[1]), float(argv[2]), argv[3])
                        else:
                            convert_racemenu_2_bodyslide(file_path, float(argv[1]), float(argv[2]), argv[3], argv[4])
                    else:
                        convert_racemenu_2_bodyslide(file_path)
    except Exception as e:
        print(f"Error: {e}")
