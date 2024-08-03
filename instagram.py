import logging
import requests
import json
from . import helpers
from .config import (INSTAGRAM_USER_ID, USER_ACCESS_TOKEN)
from concurrent.futures import ThreadPoolExecutor
from . import configLog

logger, speed_logger = configLog.configure_logging()

ig_user_id = INSTAGRAM_USER_ID
user_access_token = USER_ACCESS_TOKEN
base_url = f'https://graph.facebook.com/v13.0/{ig_user_id}'

def check_response(response):
    if response.status_code != 200:
        logging.error(f"Request failed with status {response.status_code}, response: {response.text}")
        return False
    logging.debug(f"Request succeeded with status {response.status_code}, response: {response.text}")
    return True

def post_to_ig(endpoint, payload):
    url = f'{base_url}/{endpoint}'
    logging.debug(f"Posting to URL: {url} with payload: {payload}")
    r = requests.post(url, data=payload)
    if not check_response(r):  # if the request failed
        return None  # return None to indicate failure
    result = json.loads(r.text)
    id = result.get('id')
    logging.debug(f"Post response ID: {id}")
    return id  # return the id if the request was successful


def create_item_container(image_url):
    payload = {
        'image_url': image_url,  
        'is_carousel_item': True,  
        'access_token': user_access_token  
    }  
    id = post_to_ig('media', payload)
    if id:
        logging.info('Item container created for image URL: %s', image_url)
    else:
        logging.error('Failed to create item container for image URL: %s', image_url)
    return id

def create_carousel_container(children, text):
    payload = {  
        'children': ','.join(children),
        'media_type': 'CAROUSEL',
        'caption': helpers.strip_html_tags(text) + ' #midjourney #aiart #aiartcommunity #generativeai #synthography #postphotography',
        'access_token': user_access_token  
    }  
    id = post_to_ig('media', payload)
    if id:
        logging.info('Carousel container created')
    else:
        logging.error('Failed to create carousel container')
    return id

def publish_carousel_container(creation_id):
    payload = {  
        'creation_id': creation_id,
        'access_token': user_access_token  
    }  
    id = post_to_ig('media_publish', payload)  
    if id:
        logging.info('Carousel container published')
    else:
        logging.error('Failed to publish carousel container')

def postInstagramCarousel(image_locations, text):
    logger.info('postInstagramCarousel function called with image locations: %s and text: %s', image_locations, text)
    if len(image_locations) == 1:
        return postInstagramSingleImage(image_locations[0], text)

    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        # Submit tasks to the executor
        futures = {executor.submit(create_item_container, image_url) for image_url in image_locations}
        # Gather the results as they become available
        children = [future.result() for future in futures if future.result() is not None]

    if children:
        carousel_id = create_carousel_container(children, text)
        if carousel_id:
            return publish_carousel_container(carousel_id)

    return False  # return False if the operation failed


def postInstagramSingleImage(image_url, text):
    logger.info('postInstagramSingleImage function called with image URL: %s and text: %s', image_url, text)
    media_id = create_item_container_single_image(image_url, text)
    if media_id:
        return publish_single_image_container(media_id, text)
    return False  # return False if the operation failed


def create_item_container_single_image(image_url, text):
    payload = {
        'image_url': image_url,
        'caption': helpers.strip_html_tags(text) + ' #midjourney #aiart #aiartcommunity #generativeai #synthography #postphotography',
        'access_token': user_access_token
    }
    id = post_to_ig('media', payload)
    if id:
        logging.info('Single item container created for image URL: %s', image_url)
    else:
        logging.error('Failed to create single item container for image URL: %s', image_url)
    return id

def publish_single_image_container(creation_id, text):
    payload = {
        'creation_id': creation_id,
        'caption': helpers.strip_html_tags(text) + ' #midjourney #aiart #aiartcommunity #generativeai #synthography #postphotography',
        'access_token': user_access_token
    }
    id = post_to_ig('media_publish', payload)
    if id:
        logging.info('Single image container published')
    else:
        logging.error('Failed to publish single image container')
