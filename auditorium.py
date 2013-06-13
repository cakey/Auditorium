import collections

from plist_parser import XmlPropertyListParser

def get_itunes_artists():
    ITUNES_META_FILE = "C:\Users\cakey\Music\iTunes\iTunes Music Library.xml"

    with open(ITUNES_META_FILE) as f:
        meta_data = XmlPropertyListParser().parse(f)

    artists = collections.defaultdict(list)

    for track_id, track_data in meta_data['Tracks'].iteritems():
        if 'Disabled' not in track_data and 'Artist' in track_data:
            artist = track_data['Artist']
            artists[artist].append(track_data)

    # filter out artists that have a small number of tracks to reduce bad naming noise
    artists = {artist:tracks for artist, tracks in artists.iteritems() if len(tracks) >= 5}

    return artists

print get_itunes_artists().keys()