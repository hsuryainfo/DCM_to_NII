## Setup

### 1. Clone the repository and navigate to the project directory

```sh
git clone <your-repo-url>
cd DCM_to_NII
```

### 2. Create and activate a virtual environment

#### **On macOS/Linux:**
```sh
python3 -m venv venv
source venv/bin/activate
```

#### **On Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Set up your `.env` file (optional, for custom input folder)

Create a `.env` file in the project root with:
```
INPUT_ROOT=./input/dicom_sorted
```

---

## Usage

1. **Place your DICOM files** in the `input/dicom_sorted` directory (or as specified in `.env`).

2. **Run the converter:**

   #### **On macOS/Linux:**
   ```sh
   python main.py
   ```

   #### **On Windows:**
   ```sh
   python main.py
   ```

3. **Check the outputs:**
    - Sorted DICOMs: `output/organized_dicoms/`
    - Unknowns: `output/position_not_found/`
    - NIfTI files: `output/nifti/`
    - Logs: `logs/dicom2nifti.log`