import requests
import xbmcgui
import xbmcplugin

__url = sys.argv[0]
__handler = int(sys.argv[1])


items = requests.get("https://api.mxplay.com/v1/web/live/channels?device-density=2&userid=de6336ad-26f3-40bf-bffe-a2d2386a02b1&platform=com.mxplay.desktop&content-languages=hi,en,ta").json()
def channels():
    for item in items["channels"]:
        liz = xbmcgui.ListItem(label=item['title'])
        imageicon ='https://media-content.akamaized.net/'+item['imageInfo'][0]['url']
        liz.setArt({'icon': imageicon, 'thumb':imageicon})
        liz.setInfo('video', {'title':item['title']})
        url = item['stream']['mxplay']['hls']['main']
        xbmcplugin.addDirectoryItem(__handler, url, liz, False)
    xbmcplugin.endOfDirectory(__handler)
 
def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring
    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    channels()
 
if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])