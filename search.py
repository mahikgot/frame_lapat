from google_images_search import GoogleImagesSearch
import argparse

print('Downloading...')
parser = argparse.ArgumentParser()
parser.add_argument('search')
args = parser.parse_args()
# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)

# define search params
# option for commonly used search param are shown below for easy reference.
# For param marked with '##':
#   - Multiselect is currently not feasible. Choose ONE option only
#   - This param can also be omitted from _search_params if you do not wish to define any value

term = args.search + ' cute'
_search_params = {
    'q': term,
    'num': 50,
    'filetype': 'jpg',
}


# search first, then download and resize afterwards:
gis.search(search_params=_search_params)
gis.next_page()
for image in gis.results():
    image.download('./'+_search_params['q'][:-5]+'/')  # download image
