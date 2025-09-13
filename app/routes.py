from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from app import spotify_service
from .models import  Track, Artist, Album, Playlist

# Create router
router = APIRouter(tags=["Spotify API"])

# Create playlist service instance

spotify_service = spotify_service.SpotifyAPIService()




@router.get("/spotify/playlists/{playlist_id}/separated")
async def get_playlist_tracks_separated(playlist_id: str):
    """Get playlist tracks using separated models - Playlist + ApiResponse"""
    print("Getting playlist tracks with separated models")

    try:
        # Get raw data from Spotify API
        result = await spotify_service.get_playlist_tracks(playlist_id)
        
        # Process the result for frontend using Pydantic models
        if result and "items" in result:
            tracks = []
            for item in result["items"]:
                track_data = item.get("track", {})
                if track_data:
                    # Convert to Pydantic models
                    
                    # Create Artist objects
                    artists = [
                        Artist(
                            id=artist.get("id", ""),
                            name=artist.get("name", ""),
                            external_urls=artist.get("external_urls", {})
                        )
                        for artist in track_data.get("artists", [])
                    ]
                    
                    # Create Album object
                    album_data = track_data.get("album", {})
                    album = Album(
                        id=album_data.get("id", ""),
                        name=album_data.get("name", ""),
                        album_type=album_data.get("album_type", ""),
                        release_date=album_data.get("release_date", ""),
                        images=album_data.get("images", [])
                    )
                    
                    # Create Track object
                    track = Track(
                        id=track_data.get("id", ""),
                        name=track_data.get("name", ""),
                        artists=artists,
                        album=album,
                        duration_ms=track_data.get("duration_ms", 0),
                        popularity=track_data.get("popularity", 0),
                        preview_url=track_data.get("preview_url"),
                        external_urls=track_data.get("external_urls", {})
                    )
                    tracks.append(track)
            
            # Create pure Playlist model (business data)
            playlist = Playlist(
                id=playlist_id,
                name="Playlist",  # You might want to get this from playlist info
                tracks=tracks,
                total_tracks=len(tracks)
            )
            

            
            return JSONResponse(
                status_code=200,

                content={"data": playlist.model_dump(),
                        "message": "Playlist tracks retrieved successfully"}
            )
        else:
            # Return error using ApiResponse

            return JSONResponse(
                status_code=404,
                content={"success":False,
                "message":"No tracks found in playlist",
                "data":None}
            )
            
    except Exception as e:
        # Return error using ApiResponse

        return JSONResponse(
            status_code=500,
            content=None
        )

@router.get("/test")
async def test_endpoint():
    """Test endpoint to verify server is working"""
    return {
        "message": "Server is working!", 
        "status": "ok",
        "endpoints": {
            "playlist_tracks": "/api/v1/spotify/playlists/{playlist_id}",
            "playlist_tracks_json": "/api/v1/spotify/playlists/{playlist_id}/json",
            "playlist_tracks_separated": "/api/v1/spotify/playlists/{playlist_id}/separated",
            "search_tracks": "/api/v1/spotify/search/tracks?query=Jay+Chou&limit=20"
        }
    }



