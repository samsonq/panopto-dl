import os
import sys
from tqdm import tqdm

from panopto_dl.PanoptoDownloader import PanoptoDownloader


# save to local
LOCAL_FOLDER = "/Users/samsonqian/Desktop/MIT Panopto"

def callback(progress: int):
    """
    :param progress: Downloading progress. From 0 to 100
    """
    #print(f"{progress} / 100")
    return


if __name__ == "__main__":
    counter = 1
    with open("test.txt", "r") as f:
        lines = f.readlines()
        total_lines = len(lines)
        for url in tqdm(lines, total=total_lines, position=0):
            try:
                url = url.strip()
                PATH = os.path.join(LOCAL_FOLDER, url.split("/")[-1])
                PanoptoDownloader.download(url,
                                           PATH,
                                           callback)

            except Exception as e:
                print(e)

            print("Completed: {}/{}".format(counter, total_lines))
            counter += 1
