# Auto-Instagram-Post

This project requires FFmpeg, a powerful multimedia framework, to handle audio and video processing tasks. FFmpeg enables various operations such as format conversion, editing, filtering, and streaming.

Before proceeding with the project, ensure that FFmpeg is installed on your system.

Installing FFmpeg on Linux:
1. Open a terminal.
2. Update the package lists by running the following command: `sudo apt update`
3. Install FFmpeg by running the following command: `sudo apt install ffmpeg` This command will install FFmpeg along with its dependencies.
4. After the installation is complete, you can verify the installation by checking the FFmpeg version: `ffmpeg -version` You should see the version information displayed in the terminal.

Installing FFmpeg on Windows:
1. Go to the FFmpeg website at https://ffmpeg.org/ and navigate to the "Download" section.
2. Scroll down and locate the "Get the Packages" section. You'll find a list of available packages for Windows.
3. Download the latest static build of FFmpeg for Windows by clicking on the "Windows" link next to "Static Builds."
4. Extract the downloaded ZIP file to a location of your choice.
5. Once extracted, you'll have a folder containing the FFmpeg binaries. To use FFmpeg from the command line, you need to add its location to the system's PATH environment variable.
6. Click "OK" on all the open windows to save the changes.
7. To verify the installation, open a command prompt and type: `ffmpeg -version` You should see the version information displayed in the command prompt.

##Installation
1. Git Clone the repo
2. Go in the cloned repo folder
3. Install the requirement file. Using `pip install -r requirements.txt`.
4. In main.py go to line number 136 and edit the USERNAME & PASSWORD variable with your username and password.
5. Create 4 Folders Named "DONE", "post", "reel" and tmp.
6. In DONE folder create 2 more folders "post" & "reel".
7. In tmp folder create a file hashtag.txt with all the hashtags you want to include in posts or reels.
8. In main "post" & "reel" folder add posts and reels you want to upload to instagram.
9. Just run the script and enjoy.
