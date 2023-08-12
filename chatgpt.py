import requests

def download_panopto_video(panopto_url, save_path):
    try:
        # Send a request to the Panopto URL
        response = requests.get(panopto_url, stream=True)
        response.raise_for_status()

        # Save the video in chunks
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print("Video downloaded and saved successfully!")

    except requests.exceptions.RequestException as e:
        print("Error while downloading the video:", e)


if __name__ == "__main__":
    panopto_video_url = "https://d2y36twrtb17ty.cloudfront.net/sessions/be03e19c-791e-438e-a226-af1000f23a6a/22879c3a-2d7b-45a5-bdfc-af1000f23a74-ce1e0cde-c6ad-493c-b8af-af740108032b.mp4"
    save_path = "video.mp4"
    download_panopto_video(panopto_video_url, save_path)
