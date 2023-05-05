
from youtubesearchpython import VideosSearch, ResultMode

videosSearch = VideosSearch('algebra', limit = 2)

print(videosSearch.result())

print('**************')
# get YT video suggestions
from youtubesearchpython import Suggestions

suggestions = Suggestions(language = 'en', region = 'US')

print(suggestions.get('algebra', mode = ResultMode.json))