from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

# =============================================================================
# External API Models (for parsing Spotify API responses)
# =============================================================================

class SpotifyArtist(BaseModel):
    """Spotify artist model (for parsing API responses)"""
    id: str
    name: str
    external_urls: Dict[str, str] = Field(default_factory=dict)
    # Can include other fields provided by Spotify
    href: Optional[str] = None
    type: Optional[str] = None
    uri: Optional[str] = None

class SpotifyAlbum(BaseModel):
    """Spotify album model (for parsing API responses)"""
    id: str
    name: str
    release_date: str
    images: List[Dict[str, Any]] = Field(default_factory=list)
    # Can include other fields provided by Spotify
    album_type: Optional[str] = None
    artists: Optional[List[SpotifyArtist]] = None
    external_urls: Optional[Dict[str, str]] = None
    href: Optional[str] = None
    type: Optional[str] = None
    uri: Optional[str] = None

class SpotifyTrack(BaseModel):
    """Spotify track model (for parsing API responses)"""
    id: str
    name: str
    artists: List[SpotifyArtist]
    album: SpotifyAlbum
    duration_ms: int
    popularity: int
    preview_url: Optional[str] = None
    external_urls: Dict[str, str] = Field(default_factory=dict)
    # Can include other fields provided by Spotify
    disc_number: Optional[int] = None
    explicit: Optional[bool] = None
    href: Optional[str] = None
    is_local: Optional[bool] = None
    track_number: Optional[int] = None
    type: Optional[str] = None
    uri: Optional[str] = None

class SpotifyPlaylist(BaseModel):
    """Spotify playlist model (for parsing API responses)"""
    id: str
    name: str
    description: Optional[str] = None
    owner: Dict[str, Any] = Field(default_factory=dict)
    tracks: Dict[str, Any] = Field(default_factory=dict)
    external_urls: Dict[str, str] = Field(default_factory=dict)
    # Can include other fields provided by Spotify
    collaborative: Optional[bool] = None
    href: Optional[str] = None
    images: Optional[List[Dict[str, Any]]] = None
    public: Optional[bool] = None
    snapshot_id: Optional[str] = None
    type: Optional[str] = None
    uri: Optional[str] = None


class Artist(BaseModel):
    """Artist model (for frontend use)"""
    id: str = Field(..., description="Artist ID")
    name: str = Field(..., description="Artist name")
    external_urls: Dict[str, str] = Field(default_factory=dict, description="External links")

class Album(BaseModel):
    """Album model (for frontend use)"""
    id: str = Field(..., description="Album ID")
    album_type: str = Field(..., description="Album type")
    name: str = Field(..., description="Album name")
    release_date: str = Field(..., description="Release date")
    images: List[Dict[str, Any]] = Field(default_factory=list, description="Album images")
    artists: Optional[List[Artist]] = Field(None, description="List of artists")

class Track(BaseModel):
    """Track model (for frontend use)"""
    id: str = Field(..., description="Track ID")
    name: str = Field(..., description="Track name")
    artists: List[Artist] = Field(..., description="List of artists")
    album: Album = Field(..., description="Album information")
    duration_ms: int = Field(..., description="Track duration in milliseconds")
    popularity: int = Field(..., description="Popularity score")
    preview_url: Optional[str] = Field(None, description="Preview URL")
    external_urls: Dict[str, str] = Field(default_factory=dict, description="External links")

class Playlist(BaseModel):
    """Playlist model (pure data structure)"""
    id: str = Field(..., description="Playlist ID")
    name: str = Field(..., description="Playlist name")
    tracks: List[Track] = Field(..., description="List of tracks")
    total_tracks: int = Field(..., description="Total number of tracks")


