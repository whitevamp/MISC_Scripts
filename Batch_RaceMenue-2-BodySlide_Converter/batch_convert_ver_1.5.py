#ver1.5
import json
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as MD
from sys import argv


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

__version__ = "1.1.0"

# def load_json(file):
    # """Load and parse JSON file, handling any JSON errors."""
    # try:
        # with open(file, 'r') as handle:
            # parsed = json.load(handle)
        # return parsed
    # except json.JSONDecodeError as e:
        # # Log error message and skip the file
        # error_message = f"Skipping file due to JSONDecodeError at {file}: {str(e)}"
        # print(error_message)
        # log_error(error_message)
        # return None  # Return None for invalid JSON
def load_json(file):
    """Load and parse JSON file, handling any JSON errors and null characters."""
    try:
        with open(file, 'r', encoding='utf-8') as handle:
            content = handle.read()

        # Check for null characters and log their presence
        if '\x00' in content:
            log_message = f"Found null character at the end of the file: {file}"
            print(log_message)
            log_error(log_message)
            
            # Remove null characters
            content = content.replace('\x00', '')

        # Attempt to load the JSON data
        parsed = json.loads(content)
        return parsed

    except json.JSONDecodeError as e:
        error_message = f"Skipping file due to JSONDecodeError at {file}: {str(e)}"
        print(error_message)
        log_error(error_message)
        return None  # Return None for invalid JSON

    except Exception as e:
        # Catch other exceptions (e.g., IOError, etc.)
        error_message = f"Error processing file {file}: {str(e)}"
        print(error_message)
        log_error(error_message)
        return None


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


#def log_error(message):
#    """Append error message to an error log file, including script version."""
#    error_log_path = os.path.join(os.getcwd(), 'error_log.txt')
#    with open(error_log_path, 'a') as error_log:
#        error_log.write(f"Version {__version__}: {message}\n")
#        #error_log.write(message + '\n')
def log_error(message):
    """Append error message to an error log file. If the file is new, log the script version first."""
    error_log_path = os.path.join(os.getcwd(), 'error_log.txt')

    # Check if the error log file already exists and has content
    if not os.path.exists(error_log_path) or os.stat(error_log_path).st_size == 0:
        # If file doesn't exist or is empty, write the version at the top
        with open(error_log_path, 'a') as error_log:
            error_log.write(f"Script Version: {__version__}\n")

    # Now append the actual error message
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