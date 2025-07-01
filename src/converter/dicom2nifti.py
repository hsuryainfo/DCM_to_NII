
import os
import shutil
import pydicom
import SimpleITK as sitk
import logging


def setup_logging(log_folder):
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, "dicom2nifti.log")
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO
    )
   
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

def extract_sort_convert_dicoms(input_root, output_folder, unknown_folder, nifti_output_folder, log_folder):
    setup_logging(log_folder)
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(unknown_folder, exist_ok=True)
    os.makedirs(nifti_output_folder, exist_ok=True)

    for root, _, files in os.walk(input_root):
        folder_name = os.path.basename(root)
        for filename in files:
            if not filename.lower().endswith('.dcm'):
                continue

            filepath = os.path.join(root, filename)

            try:
                dicom_data = pydicom.dcmread(filepath)
            except Exception as e:
                msg = f"Error reading {filename}: {e}"
                print(msg)
                logging.error(msg)
                continue

            view = dicom_data.get("ViewPosition", None)
            side = dicom_data.get("ImageLaterality", None)

            if view and side:
                view = view.strip().upper()
                side = side.strip().upper()

                subfolder = os.path.join(output_folder, folder_name)
                os.makedirs(subfolder, exist_ok=True)
                
                new_name = f"{side}_{view}_{filename}"
                new_path = os.path.join(subfolder, new_name)
                shutil.copy2(filepath, new_path)
                msg = f"Saved {filename} as {new_name}"
                print(msg)
                logging.info(msg)
            else:
                unknown_path = os.path.join(unknown_folder, filename)
                shutil.copy2(filepath, unknown_path)
                msg = f"Moved {filename} to unknown folder (missing ViewPosition/ImageLaterality)"
                print(msg)
                logging.warning(msg)

    print("\nConverting sorted DICOMs to NIfTI...")
    logging.info("Starting DICOM to NIfTI conversion...")
    convert_dicom_to_nifti(output_folder, nifti_output_folder)

def convert_dicom_to_nifti(dicom_folder, output_folder):
    reader = sitk.ImageSeriesReader()

    for root, _, files in os.walk(dicom_folder):
        dcm_files = [f for f in files if f.lower().endswith('.dcm')]
        if not dcm_files:
            continue

        rel_path = os.path.relpath(root, dicom_folder)
        nii_subfolder = os.path.join(output_folder, rel_path)
        os.makedirs(nii_subfolder, exist_ok=True)

        try:
            for dcm_file in dcm_files:
                filepath = os.path.join(root, dcm_file)

                image = sitk.ReadImage(filepath)

                base_name = os.path.splitext(dcm_file)[0]
                output_path = os.path.join(nii_subfolder, base_name + ".nii.gz")

                sitk.WriteImage(image, output_path)
                msg = f"Converted to NIfTI: {output_path}"
                print(msg)
                logging.info(msg)

        except Exception as e:
            msg = f"Failed to convert {filepath}: {e}"
            print(msg)
            logging.error(msg)

#all input and output folders

if __name__ == "__main__":
    input_root = "DICOM sorted"                   
    output_folder = "organized_dicoms"              
    unknown_folder = "position_not_found"           
    nifti_output_folder = "output_nii"              
    log_folder = "logs"                             

    extract_sort_convert_dicoms(input_root, output_folder, unknown_folder, nifti_output_folder, log_folder)

