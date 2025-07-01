import sys
import os
from src.converter.dicom2nifti import extract_sort_convert_dicoms


if __name__ == "__main__":
    input_root = os.getenv("INPUT_ROOT", "./input/dicom_sorted")
    output_folder = os.getenv("OUTPUT_FOLDER", "./output/organized_dicoms")
    unknown_folder = os.getenv("UNKNOWN_FOLDER", "./output/position_not_found")
    nifti_output_folder = os.getenv("NIFTI_OUTPUT_FOLDER", "./output/nifti")
    log_folder = os.getenv("LOG_FOLDER", "./logs/dicom2nifti.log")

    extract_sort_convert_dicoms(
        input_root,
        output_folder,
        unknown_folder,
        nifti_output_folder,
        log_folder
    )