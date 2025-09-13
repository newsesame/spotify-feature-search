# """
# Playlist service
# """
# import asyncio
# from typing import List
# from .models import (
#     Track, Artist, Album,
#     SpotifyTrack, SpotifyArtist, SpotifyAlbum, SpotifyPlaylist
# )
# from .spotify_service import SpotifyAPIService
# import logging

# logger = logging.getLogger(__name__)

# class PlaylistService:
#     """Playlist service class"""
    
#     def __init__(self):
#         # Spotify API service
#         self.spotify_service = SpotifyAPIService()
    
#     async def _convert_spotify_track(self, track_data: dict) -> Track:
#         """Convert Spotify track data to our track model"""
#         try:
#             # First parse as Spotify model (validate data structure)
#             spotify_track = SpotifyTrack(**track_data)
            
#             # Convert to our model
#             artists = []
#             for spotify_artist in spotify_track.artists:
#                 artist = Artist(
#                     id=spotify_artist.id,
#                     name=spotify_artist.name,
#                     external_urls=spotify_artist.external_urls
#                 )
#                 artists.append(artist)
            
#             album = Album(
#                 id=spotify_track.album.id,
#                 name=spotify_track.album.name,
#                 release_date=spotify_track.album.release_date,
#                 images=spotify_track.album.images
#             )
            
#             track = Track(
#                 id=spotify_track.id,
#                 name=spotify_track.name,
#                 artists=artists,
#                 album=album,
#                 duration_ms=spotify_track.duration_ms,
#                 popularity=spotify_track.popularity,
#                 preview_url=spotify_track.preview_url,
#                 external_urls=spotify_track.external_urls
#             )
            
#             return track
            
#         except Exception as e:
#             logger.error(f"Failed to convert Spotify track data: {e}")
#             # If parsing fails, use fallback method
#             return self._convert_spotify_track_fallback(track_data)
    
#     def _convert_spotify_track_fallback(self, track_data: dict) -> Track:
#         """Fallback conversion method (used when main method fails)"""
#         artists = []
#         for artist_data in track_data.get("artists", []):
#             artist = Artist(
#                 id=artist_data.get("id", ""),
#                 name=artist_data.get("name", ""),
#                 external_urls=artist_data.get("external_urls", {})
#             )
#             artists.append(artist)
        
#         album_data = track_data.get("album", {})
#         album = Album(
#             id=album_data.get("id", ""),
#             name=album_data.get("name", ""),
#             release_date=album_data.get("release_date", ""),
#             images=album_data.get("images", [])
#         )
        
#         track = Track(
#             id=track_data.get("id", ""),
#             name=track_data.get("name", ""),
#             artists=artists,
#             album=album,
#             duration_ms=track_data.get("duration_ms", 0),
#             popularity=track_data.get("popularity", 0),
#             preview_url=track_data.get("preview_url"),
#             external_urls=track_data.get("external_urls", {})
#         )
        
#         return track
    
#     async def get_playlist_tracks_for_frontend(self, playlist_id: str) -> PlaylistTracksResponse:
#         """Get playlist tracks for frontend"""
#         try:
#             # Fetch playlist info and tracks in parallel
#             playlist_data, tracks_data = await asyncio.gather(
#                 self.spotify_service.get_playlist(playlist_id),
#                 self.spotify_service.get_playlist_tracks(playlist_id)
#             )
            
#             # Convert track data
#             tracks = []
#             for item in tracks_data.get("items", []):
#                 track_data = item.get("track", {})
#                 if track_data:
#                     track = await self._convert_spotify_track(track_data)
#                     tracks.append(track)
            
#             return PlaylistTracksResponse(
#                 playlist_id=playlist_id,
#                 playlist_name=playlist_data.get("name", ""),
#                 tracks=tracks,
#                 total_tracks=len(tracks),
#                 success=True,
#                 message="Playlist tracks retrieved successfully"
#             )
            
#         except Exception as e:
#             logger.error(f"Failed to get playlist tracks: {e}")
#             return PlaylistTracksResponse(
#                 playlist_id=playlist_id,
#                 playlist_name="",
#                 tracks=[],
#                 total_tracks=0,
#                 success=False,
#                 message=f"Failed to get playlist tracks: {str(e)}"
#             )
    
#     async def search_spotify_tracks_for_frontend(self, query: str, limit: int = 20) -> TrackSearchResponse:
#         """Search Spotify tracks for frontend"""
#         try:
#             search_result = await self.spotify_service.search_tracks(query, limit)
#             tracks = []
            
#             for track_data in search_result.get("tracks", {}).get("items", []):
#                 track = await self._convert_spotify_track(track_data)
#                 tracks.append(track)
            
#             return TrackSearchResponse(
#                 query=query,
#                 tracks=tracks,
#                 total=len(tracks),
#                 success=True,
#                 message="Track search completed successfully"
#             )
            
#         except Exception as e:
#             logger.error(f"Failed to search tracks: {e}")
#             return TrackSearchResponse(
#                 query=query,
#                 tracks=[],
#                 total=0,
#                 success=False,
#                 message=f"Failed to search tracks: {str(e)}"
#             )