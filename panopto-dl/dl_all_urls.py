import os
from tqdm import tqdm
from app.PanoptoDownloader import download
import warnings
warnings.filterwarnings("ignore")

SAVE_PATH = "../recordings"


def callback(progress: int):
    """
    :param progress: Downloading progress. From 0 to 100
    """
    print(f"{progress} / 100")


def main():
    """
    TODO: This function is not working, fix the loop to download all recordings in 'urls.txt' file
    The UI app works fine, however
    """
    urls = open("urls.txt", "r").readlines()
    print("Downloading {} total videos...".format(len(urls)))
    print("-"*20)
    for i, url in tqdm(enumerate(urls), total=len(urls)):
        download_path = os.path.join(SAVE_PATH, "lecture_{}.mp4".format(i+1))
        try:
            download(
                url,
                download_path,
                callback
            )
            print("Download completed")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
