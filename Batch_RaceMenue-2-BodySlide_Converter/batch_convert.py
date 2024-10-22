# ver1.7.0
import json
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
from sys import argv
import configparser
import re

# BodySlide options, to be completed
bodyslide_elems = [
    # Added from post by sysdmp post URL https://www.nexusmods.com/skyrimspecialedition/mods/104641?tab=posts
    "7BLeg_v2",
    "AnalLoose_v2",
    "AnalPosition_v2",
    "AnalTexPosRe_v2",
    "AnalTexPos_v2",
    "AnkleSize",
    "AppleCheeks",
    "AreolaPull_v2",
    "AreolaSize",
    "ArmpitShape_v2",
    "Arms",
    "Back",
    "BackArch",
    "BackValley_v2",
    "BackWing_v2",
    "Belly",
    "BellyFrontDownFat_v2",
    "BellyFrontUpFat_v2",
    "BellySideDownFat_v2",
    "BellySideUpFat_v2",
    "BellyUnder_v2",
    "BigBelly",
    "BigButt",
    "BigTorso",
    "BreastCenter",
    "BreastCenterBig",
    "BreastCleavage",
    "BreastFlatness",
    "BreastFlatness2",
    "BreastGravity2",
    "BreastHeight",
    "BreastPerkiness",
    "Breasts",
    "BreastsConverage_v2",
    "BreastsFantasy",
    "BreastsGone",
    "BreastSideShape",
    "BreastsNewSH",
    "BreastsNewSHSymmetry",
    "BreastsPressed_v2",
    "BreastsSmall",
    "BreastsSmall2",
    "BreastsTogether",
    "BreastTopSlope",
    "BreastUnderDepth",
    "BreastWidth",
    "Butt",
    "ButtClassic",
    "ButtCrack",
    "ButtDimples",
    "ButtNarrow_v2",
    "ButtPressed_v2",
    "ButtSaggy_v2",
    "ButtShape2",
    "ButtSmall",
    "ButtUnderFold",
    "CalfFBThicc_v2",
    "CalfSize",
    "CalfSmooth",
    "CBPC",
    "ChestDepth",
    "ChestWidth",
    "ChubbyArms",
    "ChubbyButt",
    "ChubbyLegs",
    "ChubbyWaist",
    "Clavicle_v2",
    "Clit",
    "ClitSwell_v2",
    "CrotchBack",
    "CrotchGap",
    "Cutepuffyness",
    "DoubleMelon",
    "FeetFeminine",
    "ForearmSize",
    "Groin",
    "HipBone",
    "HipCarved",
    "HipForward",
    "HipNarrow_v2",
    "Hips",
    "HipUpperWidth",
    "Innieoutie",
    "KneeHeight",
    "KneeShape",
    "KneeTogether_v2",
    "LabiaBulgogi_v2",
    "LabiaCrumpled_v2",
    "LabiaMorePuffyness_v2",
    "LabiaNeat_v2",
    "Labiaprotrude",
    "Labiaprotrude2",
    "Labiaprotrudeback",
    "Labiapuffyness",
    "Labiaspread",
    "LabiaTightUp",
    "LegShapeClassic",
    "LegSpread_v2",
    "LegsThin",
    "MuscleAbs",
    "MuscleArms",
    "MuscleBack_v2",
    "MuscleButt",
    "MuscleLegs",
    "MuscleMoreAbs_v2",
    "MuscleMoreArms_v2",
    "MuscleMoreLegs_v2",
    "MusclePecs",
    "NavelEven",
    "NipBGone",
    "NippleBump_v2",
    "NippleCrease_v2",
    "NippleCrumpled_v2",
    "NippleDip",
    "NippleDistance",
    "NippleDown",
    "NippleInvert_v2",
    "NippleLength",
    "NippleManga",
    "NipplePerkiness",
    "NipplePerkManga",
    "NipplePuffy_v2",
    "NippleShy_v2",
    "NippleSize",
    "NippleSquash1_v2",
    "NippleSquash2_v2",
    "NippleThicc_v2",
    "NippleTip",
    "NippleTipManga",
    "NippleTube_v2",
    "NippleUp",
    "OldBaseShape",
    "PregnancyBelly",
    "PushUp",
    "RibsMore_v2",
    "RibsProminance",
    "RoundAss",
    "ShoulderSmooth",
    "ShoulderTweak",
    "ShoulderWidth",
    "SlimThighs",
    "SternumDepth",
    "SternumHeight",
    "ThighFBThicc_v2",
    "ThighInsideThicc_v2",
    "ThighOutsideThicc_v2",
    "Thighs",
    "TummyTuck",
    "UNPHip_v2",
    "VaginaHole",
    "Vaginasize",
    "VanillaSSEHi",
    "VanillaSSELo",
    "Waist",
    "WaistHeight",
    "WideWaistLine",
    "WristSize",
]

__version__ = "1.7.0"

def load_json(file):
    """Load and parse JSON file, handling any JSON errors and null characters."""
    try:
        with open(file, 'r', encoding='utf-8') as handle:
            content = handle.read()

        # Check for null characters and remove them
        if '\x00' in content:
            log_message = f"Found null character in: {file}"
            print(log_message)
            log_error(log_message)
            content = content.replace('\x00', '')  # Remove null characters

        # Parse the JSON content
        parsed = json.loads(content)
        return parsed

    except json.JSONDecodeError as e:
        # Handle JSON decoding errors
        error_message = f"Skipping file due to JSONDecodeError at {file}: {str(e)}"
        print(error_message)
        log_error(error_message)
        return None

    except Exception as e:
        # Handle all other exceptions
        error_message = f"Error processing file {file}: {str(e)}"
        print(error_message)
        log_error(error_message)
        return None

def save_xml(file, data, output_dir):
    """Save the XML file to the specified output directory."""
    try:
        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Save the XML data to the output directory
        output_path = os.path.join(output_dir, f"{file}.xml")
        with open(output_path, 'w') as handle:
            handle.write(prettify(data.getroot()))
    except Exception as e:
        error_message = f"Error saving XML file: {str(e)}"
        print(error_message)
        log_error(error_message)

def prettify(elem):
    """Format XML to be pretty-printed."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = MD.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

def log_error(message):
    """Log errors to an error_log.txt file."""
    error_log_path = os.path.join(os.getcwd(), 'error_log.txt')

    if not os.path.exists(error_log_path) or os.stat(error_log_path).st_size == 0:
        with open(error_log_path, 'a') as error_log:
            error_log.write(f"Script Version: {__version__}\n")

    with open(error_log_path, 'a') as error_log:
        error_log.write(message + '\n')

def convert_racemenu_2_bodyslide(file_path: str, small_size_modifier: float = 0.5, big_size_modifier: float = 1.5,
                                 group_name: str = None, body_name: str = None, output_dir: str = None):
    try:
        # Step 1: Read and handle null characters in the file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            file_content = f.read()
        
        if '\x00' in file_content:
            # Log the presence of null characters
            print(f"Found null character in: {file_path}")
            log_error(f"Found null character in: {file_path}")
            # Optionally remove null characters from the content
            file_content = file_content.replace('\x00', '')

        # Step 2: Process the JSON data after cleaning
        try:
            input_data = json.loads(file_content)
        except json.JSONDecodeError as e:
            error_message = f"Error decoding JSON in file: {file_path}, error: {str(e)}"
            print(error_message)
            log_error(error_message)
            return

        body_morph = input_data.get('bodyMorphs', [])
        size = 'small' if input_data['actor']['weight'] < 50 else 'big'

        for e in bodyslide_elems:
            if e not in [a['name'] for a in body_morph]:
                body_morph.append({
                    'name': e,
                    'keys': [{'value': 0}]
                })

        r = ET.Element('SliderPresets')
        tree = ET.ElementTree(r)
        root = tree.getroot()

        file_name = os.path.splitext(os.path.basename(file_path))[0]
        preset = ET.SubElement(root, 'Preset')

        # Set 'name' attribute for preset
        preset.attrib['name'] = file_name  # Always set the preset name as the file name

        # Set the 'set' attribute based on body_type for 3BA or other body types
        if body_type and body_type != 'SMMB':  # Ensure body_type is not None
            preset.attrib['set'] = body_type  # Use body_type directly for non-SMMB
        else:
            preset.attrib['set'] = body_name if body_name else f"{file_name} body"  # Use body_name for SMMB, or fallback

        # Set the group name according to body_type
        group_name = body_type if body_type else "DefaultGroup"  # Fallback to DefaultGroup if body_type is None
        group = ET.SubElement(preset, 'Group')
        group.attrib['name'] = group_name

        ###
        # added for future use maby.
        # for entry in body_morph:
        # # Check for 'keys' and set default if missing
        # keys = entry.get('keys', [{'value': 0}])  # Default value if 'keys' is missing
        
        # if not isinstance(keys, list):
            # error_message = f"Invalid 'keys' format in bodyMorph entry for '{entry.get('name', 'Unknown')}' in {file_path}"
            # print(error_message)
            # log_error(error_message)
            # continue  # Skip this entry if 'keys' format is incorrect
        
        # value = sum(key.get('value', 0) for key in keys)
        # name = entry['name']

        for entry in body_morph:
            if 'keys' not in entry or not isinstance(entry['keys'], list):
                error_message = f"Missing 'keys' in bodyMorph entry for '{entry.get('name', 'Unknown')}' in {file_path}. Entry: {entry}"
                print(error_message)
                log_error(error_message)
                continue

            value = sum(key.get('value', 0) for key in entry['keys'])
            name = entry['name']

            if name not in bodyslide_elems:
                bodyslide_elems.append(name)

            value_new = round(value * 100)
            # Small size slider
            slider_small = ET.SubElement(preset, 'SetSlider')
            slider_small.attrib['name'] = name
            slider_small.attrib['size'] = "small"
            slider_small.attrib['value'] = str(round(value_new * small_size_modifier)) if size == "small" else str(value_new)

            # Big size slider
            slider_big = ET.SubElement(preset, 'SetSlider')
            slider_big.attrib['name'] = name
            slider_big.attrib['size'] = "big"
            slider_big.attrib['value'] = str(round(value_new * big_size_modifier)) if size == "big" else str(value_new)

        # Save XML file, ensuring no None values in the attributes
        try:
            save_xml(file_name, tree, output_dir)
        except Exception as e:
            error_message = f"Error saving XML file: {str(e)}"
            print(error_message)
            log_error(error_message)

    except KeyError as e:
        if str(e) == "'bodyMorphs'":
            error_message = f"Skipping file due to missing 'bodyMorphs': {file_path}"
            print(error_message)
            log_error(error_message)
        else:
            raise

def load_config():
    """Load configuration settings from config.ini."""
    config = configparser.ConfigParser()
    config.read('config.ini')

    small_size_modifier = config.getfloat('Settings', 'small_size_modifier', fallback=0.5)
    big_size_modifier = config.getfloat('Settings', 'big_size_modifier', fallback=1.5)
    body_type = config.get('Settings', 'body_type', fallback='3BA')
    body_name = config.get('Settings', 'body_name', fallback=None if body_type != 'SMMB' else "SMMB High Poly SOS Body")

    # Set input and output directories to the script's current working directory
    default_output_dir = os.path.join(os.getcwd(), 'output', 'CalienteTools', 'BodySlide', 'SliderPresets')
    default_input_dir = os.getcwd()

    input_dir = config.get('Paths', 'input_dir', fallback=default_input_dir)
    output_dir = config.get('Paths', 'output_dir', fallback=default_output_dir)

    # Ensure directories are valid
    if not os.path.isabs(input_dir):
        input_dir = default_input_dir

    if not os.path.isabs(output_dir):
        output_dir = default_output_dir

    print(f"Input directory set to: {input_dir}")
    print(f"Output directory set to: {output_dir}")

    return small_size_modifier, big_size_modifier, body_type, body_name, input_dir, output_dir

if __name__ == "__main__":
    small_size_modifier, big_size_modifier, body_type, body_name, input_dir, output_dir = load_config()

    try:
        for root, dirs, files in os.walk(input_dir):
            if 'output' in dirs:
                dirs.remove('output')

            for file in files:
                if file.endswith('.jslot'):
                    file_path = os.path.join(root, file)

                    # Handle command-line arguments if provided
                    if len(argv) > 1:
                        body_type = argv[3] if len(argv) >= 4 else body_type
                        body_name = argv[4] if len(argv) == 5 and body_type == "SMMB" else body_name

                        if len(argv) == 2:
                            convert_racemenu_2_bodyslide(file_path, small_size_modifier, big_size_modifier, output_dir=output_dir)
                        elif len(argv) == 3:
                            convert_racemenu_2_bodyslide(file_path, small_size_modifier, big_size_modifier, output_dir=output_dir)
                        elif len(argv) >= 4:
                            convert_racemenu_2_bodyslide(file_path, small_size_modifier, big_size_modifier, body_type, body_name, output_dir=output_dir)
                    else:
                        # Use default config values
                        convert_racemenu_2_bodyslide(file_path, small_size_modifier, big_size_modifier, body_name=body_name, output_dir=output_dir)

    except Exception as e:
        print(f"Error: {e}")
