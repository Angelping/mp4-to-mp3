import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file):
    # Check if the file exists
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return False

    # Check if the file is an MP4
    if not input_file.lower().endswith('.mp4'):
        print("Error: The input file is not an MP4 file.")
        return False

    try:
        # Load the video file
        video = VideoFileClip(input_file)

        # Extract the audio
        audio = video.audio

        # Generate output filename
        output_file = os.path.splitext(input_file)[0] + '.mp3'

        # Write the audio to an MP3 file
        audio.write_audiofile(output_file)

        # Close the video and audio objects
        audio.close()
        video.close()

        print(f"Conversion successful. Audio saved as '{output_file}'")
        return True

    except Exception as e:
        print(f"An error occurred during conversion: {str(e)}")
        return False

def main():
    while True:
        input_file = input("Enter the path to the MP4 file (or 'q' to quit): ")
        
        if input_file.lower() == 'q':
            break

        if convert_mp4_to_mp3(input_file):
            print("Conversion completed successfully.")
        else:
            print("Conversion failed. Please try again.")

        print()  # Empty line for readability

if __name__ == "__main__":
    main()
