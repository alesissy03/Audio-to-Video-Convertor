import os
import subprocess

# Set the input folder where your .wav files are located
input_folder_path = "/mnt/d/Departamentul de muzica AZSMR Muntenia/Partituri orchestra/Audio"
# Set the output folder where you want to save the .mp4 files
output_folder_path = "/mnt/d/Departamentul de muzica AZSMR Muntenia/Partituri orchestra/Video"
# Set the path to the image you want to use as the background
background_image_path = "/mnt/d/Departamentul de muzica AZSMR Muntenia/Partituri orchestra/Audio/black.jpg"

# Make sure the output directory exists, or create it
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Make sure FFmpeg is installed and available in the system's PATH
def convert_wav_to_mp4(wav_file):
    # Get the file name without extension
    filename = os.path.basename(wav_file)
    mp4_file = os.path.join(output_folder_path, filename.replace(".wav", ".mp4"))
    
    # FFmpeg command to add background image and convert .wav to .mp4
    command = [
        "ffmpeg",
        "-loop", "1",                  # Loop the image to create a video
        "-framerate", "2",             # Set the frame rate of the video (you can adjust this)
        "-t", "3600",                  # Duration of the video in seconds (adjust to match the length of your audio file)
        "-i", background_image_path,   # Input background image
        "-i", wav_file,                # Input audio file
        "-c:v", "mpeg4",               # Video codec (MPEG-4)
        "-c:a", "aac",                 # Audio codec (AAC)
        "-b:a", "192k",                # Audio bitrate
        "-shortest",                   # Match the duration of the video to the audio
        "-y",                          # Overwrite output file if it exists
        mp4_file                       # Output file
    ]
    
    subprocess.run(command)

# Loop through all files in the input folder and convert .wav files to .mp4
for filename in os.listdir(input_folder_path):
    if filename.endswith(".wav"):
        wav_file_path = os.path.join(input_folder_path, filename)
        convert_wav_to_mp4(wav_file_path)
        print(f"Converted {filename} to {filename.replace('.wav', '.mp4')} and saved to {output_folder_path}")
