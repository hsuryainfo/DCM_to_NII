import sys
import os
from src.converter.dicom2nifti import extract_sort_convert_dicoms


if __name__ == "__main__":
    input_root = "DICOM sorted"
    output_folder = "organized_dicoms"
    unknown_folder = "position_not_found"
    nifti_output_folder = "output_nii"
    log_folder = "logs"

    extract_sort_convert_dicoms(
        input_root,
        output_folder,
        unknown_folder,
        nifti_output_folder,
        log_folder
    )