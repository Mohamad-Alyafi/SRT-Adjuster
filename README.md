# SRT Adjuster

SRT Adjuster is a simple tool for adjusting the timing of subtitles in SRT files. You can add or subtract a specified number of seconds to synchronize your subtitles with the video.

## Features

- Adjust the timing of SRT subtitle files by adding or subtracting a specified number of seconds.
- User-friendly GUI for easy interaction.
- Supports various encodings for subtitle files.
- Save the adjusted SRT file with a specified name and location.

## Requirements

- Python 3.x
- Tkinter (should be included with Python standard library)
- chardet (`pip install chardet`)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Mohamad-Alyafi/SRT-Adjuster.git
   cd SRT-Adjuster
2. Install the required dependencies:
   pip install chardet
   
## Usage

1. Run the application:
   ```sh
     python srt_adjuster.py
   
3. Use the GUI to:
-  Select the SRT file you want to adjust.
-  Enter the number of seconds to delay or advance the subtitles.
-  Choose the location and name for the adjusted SRT file.
-  Click "Adjust" to process the file.

## GUI Overview

-  Select SRT File: Browse and select the SRT file you want to adjust.
-  Enter delay time (seconds): Enter the number of seconds to delay (positive) or advance (negative) the subtitles.
-  Save Adjusted File As: Choose the location and name for the adjusted SRT file.
-  Adjust: Click to process the SRT file with the specified delay.

## Error Handling

-	If there are any issues with the input file or the parameters, an error message will be displayed.

## Developer Info

-  Developed by: Mohamad Alyafi
-  Contact: mohamad.n.alyafi@gmail.com

## Contributing

- If you find any bugs or have feature suggestions, please open an issue or submit a pull request.


