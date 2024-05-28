# PyShredder: Secure Shredding Tool
PyShredder is a Python-based desktop application that securely shreds files and folders, making data recovery virtually impossible. 
It provides multiple shredding methods, including the 3-pass DoD method, Gutmann method, random overwrite, and hybrid shred.

## Features
* Shred individual files or entire folders
* Choose from various shredding methods
* User-friendly graphical interface using PySimpleGUI
* Securely delete files beyond recovery
  
## Installation
1. Ensure you have Python installed (version 3.6 or higher).
2. Install the required dependencies:
```
pip install PySimpleGUI
```

3. Clone this repository:
```
git clone https://github.com/yourusername/shredder.git
cd shredder
```

## Usage
1. Run the shredder.py script:
```
python3 index.py

```

2. The main menu will appear, allowing you to choose between shredding a file or a folder. 
![image](https://github.com/pin-z/PyShredder/assets/76646611/d335b152-3997-49fd-b1ea-583a51d907f4)
3. Select the file or folder you want to shred.
4. Choose a shredding method (e.g., 3-pass DoD, Gutmann, etc.). 
![image](https://github.com/pin-z/PyShredder/assets/76646611/58d34c31-2cc6-479a-93f4-0b4abde79661)
5. Confirm the shredding process.
6. The selected file/folder will be securely shredded.
   
## Shredding Methods
* 3-pass DoD (Department of Defense): Overwrites the file with three passes of specific bit patterns.
* Gutmann Method: Uses a 35-pass algorithm for thorough data destruction.
* Random Overwrite: Overwrites the file with random data (configurable number of passes).
* Hybrid Shred: A combination of methods for enhanced security.
## Contributing
Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
