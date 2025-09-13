"""
Simplified Spotify API service using aiohttp
"""
import os 
import logging
import aiohttp
import base64
from typing import Dict, Any, Optional
from datetime import datetime, timedelta

from dotenv import load_dotenv

load_dotenv

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


class SpotifyAPIService:
    """Simplified Spotify API service using aiohttp"""
    
    def __init__(self, client_id: str = None, client_secret: str = None):
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.base_url = "https://api.spotify.com/v1"
        self.token_url = "https://accounts.spotify.com/api/token"
        self._access_token = None
        self._token_expires_at = None
        self._session = None
    
    async def _get_session(self) -> aiohttp.ClientSession:
        """Get aiohttp session"""
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
            logging.info("Created aiohttp Session")
        else:
            logging.info("Reused aiohttp Session")
        return self._session
    
    async def _get_token(self) -> str:


        
        """Get access token"""
        logging.info("Getting access token")
        logging.info(self._access_token, self.client_id, self.client_secret)


        if (self._access_token and 
            self._token_expires_at and 
            datetime.now() < self._token_expires_at):
            return self._access_token
        
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
        
        headers = {
            "Authorization": f"Basic {auth_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        

        session = await self._get_session()

        async with session.post(self.token_url, headers=headers, data=data) as response:
            if response.status == 400:
                logging.error("Spotify API authentication failed. Please check your client_id and client_secret.")
                raise Exception("Invalid Spotify API credentials. Please set valid client_id and client_secret.")
            
            response.raise_for_status()
            token_data = await response.json()
            
            self._access_token = token_data["access_token"]
            expires_in = token_data.get("expires_in", 3600)
            self._token_expires_at = datetime.now() + timedelta(seconds=expires_in - 60)
            
            return self._access_token
    
    async def _request(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Send API request"""
        token = await self._get_token()
        headers = {"Authorization": f"Bearer {token}"}
        url = f"{self.base_url}{endpoint}"
        
        session = await self._get_session()
        async with session.get(url, headers=headers, params=params) as response:
            response.raise_for_status()
            return await response.json()
    
    async def search_tracks(self, query: str, limit: int = 20) -> Dict[str, Any]:
        """Search tracks"""
        params = {"q": query, "type": "track", "limit": limit}
        return await self._request("/search", params)
    
    async def get_playlist(self, playlist_id: str) -> Dict[str, Any]:
        """Get playlist"""
        return await self._request(f"/playlists/{playlist_id}")
    
    async def get_playlist_tracks(self, playlist_id: str) -> Dict[str, Any]:
        """Get playlist tracks"""
        return await self._request(f"/playlists/{playlist_id}/tracks")
    
    async def close(self):
        """Close aiohttp session"""
        if self._session and not self._session.closed:
            await self._session.close()