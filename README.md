# DCM to NII Converter

This project provides tools to organize DICOM files and convert them to NIfTI format for medical imaging workflows.

## Features

- **Sorts DICOM files** by view and laterality.
- **Handles unknown/missing metadata** by moving such files to a separate folder.
- **Converts DICOM files to NIfTI (.nii.gz)** using SimpleITK.
- **Logs all operations** for traceability.

## Project Structure

```
DCM_to_NII/
├── main.py
├── src/
│   └── converter/
│       └── dicom2nifti.py
├── input/
│   └── dicom_sorted/         # Place your input DICOM files here
├── output/
│   ├── organized_dicoms/
│   ├── position_not_found/
│   └── nifti/
├── logs/
│   └── dicom2nifti.log
├── requirements.txt
└── .env
```

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your `.env` file** (optional, for custom input folder):
    ```
    INPUT_ROOT=./input/dicom_sorted
    ```

## Usage

1. **Place your DICOM files** in the `input/dicom_sorted` directory (or as specified in `.env`).

2. **Run the converter:**
    ```sh
    python main.py
    ```

3. **Check the outputs:**
    - Sorted DICOMs: `output/organized_dicoms/`
    - Unknowns: `output/position_not_found/`
    - NIfTI files: `output/nifti/`
    - Logs: `logs/dicom2nifti.log`

## Configuration

You can override default paths using environment variables or a `.env` file:
- `INPUT_ROOT`
- `OUTPUT_FOLDER`
- `UNKNOWN_FOLDER`
- `NIFTI_OUTPUT_FOLDER`
- `LOG_FOLDER`

## Requirements

- Python 3.x
- See `requirements.txt` for Python packages.

