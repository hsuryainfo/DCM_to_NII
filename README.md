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

**Virtual environment keys and usage:**

- `venv/` : The directory containing the virtual environment.
- `venv/bin/activate` : Script to activate the virtual environment on macOS/Linux.
- `venv/Scripts/activate` : Script to activate the virtual environment on Windows.
- `deactivate` : Command to exit the virtual environment.
- `venv/bin/python` or `venv/Scripts/python.exe` : Python interpreter inside the virtual environment.
- `venv/bin/pip` or `venv/Scripts/pip.exe` : Pip installer inside the virtual environment.

**Typical workflow:**
1. Activate the virtual environment as shown above.
2. Install dependencies using pip (see below).
3. Run your Python scripts while the environment is active.
4. Use `deactivate` to exit the environment when done.

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
    -