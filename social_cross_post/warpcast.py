from . import helpers
from . import configLog
from datetime import datetime
from .config import WARPCAST_ACCESS_TOKEN
from urllib.parse import urlparse
import os.path

logger, speed_logger = configLog.configure_logging()

from urllib.parse import urlparse

def post_to_warpcast(text, image_locations, alt_texts):
    text = helpers.strip_html_tags(text)
    logger.debug(f"Stripped text: {text}")
    
    images = []
    for idx, image_location in enumerate(image_locations):
        try:
            local_file_path = os.path.join("/tmp/social-cross-post", image_location)

            # Debug: log the current file path
            logger.debug(f"Processing image file: {local_file_path}")

            # Open the image file from its location
            with open(local_file_path, 'rb') as img_file:
                img_data = img_file.read()

            upload = client.com.atproto.repo.upload_blob(img_data)
            images.append(models.AppBskyEmbedImages.Image(alt=alt_texts[idx], image=upload.blob))
            logger.debug(f"Uploaded image: {upload.blob}")
        except Exception as e:
            # Exception handling: log the error and local file path
            logger.exception(f"Unable to process the image file at {local_file_path} for Bluesky. Error: {e}")
            return False

    embed = models.AppBskyEmbedImages.Main(images=images) if images else None
    facets = helpers.generate_facets_from_links_in_text(text) if helpers.URL_PATTERN.search(text) else None
    logger.debug(f"Embed: {embed}, Facets: {facets}")

    try:
        client.com.atproto.repo.create_record(
            models.ComAtprotoRepoCreateRecord.Data(
                repo=client.me.did,
                collection='app.bsky.feed.post',
                record=models.AppBskyFeedPost.Main(
                    createdAt=datetime.now().isoformat(), text=text, embed=embed, facets=facets
                ),
            )
        )
        logger.debug("Bluesky post created.")
    except Exception as e:
        logger.exception(f"Failed to create Bluesky post: {e}")
        return False

    return True
