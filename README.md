# Panopto-Video-DL

Toolkit to download recordings from Panopto.com

## Prerequisites
- Python >= 3.6

## Installation
1. Install JavaScript browser extension to get M3U8 file path
	- Install [TamperMonkey](https://www.tampermonkey.net/) Script-Manager browser extension  
		- [Chrome](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)  
		- [Firefox](https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/)  
		- [Other browser](https://www.tampermonkey.net/)  
	- Install this JavaScript script from [here](https://greasyfork.org/scripts/423661-panopto-video-dl)

2. Clone this repository to local path
	- `$ git clone https://github.com/samsonq/panopto-dl.git`
	- Install requirements to run application
		- `$ pip install -r requirements.txt`

3. Run application
	- Enter cloned repository
	- `$ cd panopto-dl`
	- `$ python main.py`
	- A UI (user-interface) should appear within a few seconds with instructions

## UI Application Usage  

1. Start application (see above section), the following UI should be displayed:
2. Open Panopto recording on web browser, and click the 'Download' button at the bottom left of the page. This will automatically copy a link for you:
3. Create a recordings folder in your local directory to store file recordings
	- `$ mkdir recordings`
	- The supported extensions of the downloaded recording include: `.mp4`, `.mkv`, `.flv`, `.avi`
4. Paste the copied link from step (2) into the application  
5. Enter the specified path to save the video recording
	- i.e. `./recordings/lecture.mp4`
6. Click the Download button and wait for recording to finish processing
	- After the progress bar reaches the end, the video recording should be saved in the specified path
