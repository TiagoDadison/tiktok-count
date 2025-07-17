import sys
import asyncio
from datetime import datetime
from fastapi import FastAPI
from TikTokApi import TikTokApi

if sys.platform == "win32":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    except:
        pass

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "TikTok API is live on Render"}

@app.get("/tiktok")
async def get_tiktok_stats():
    ms_token = "Xz2IJLCB8ItiYwkvoFA_vD_DLcrle55BkbXasWfwT3rduvLZpAWt-Lctp-4O80OxrWtoJh6MIFqMPzZwS858-o3hKlrzXmx4JxhpAJ67gMOu0vr9QWR7h6j3oeVGu8Esp9dXmIEwh90XdH9bYc_wAw=="
    username = "raiamsantos9"
    cutoff_ts = int(datetime(2025, 5, 19).timestamp())

    total_views = 0
    video_count = 0

    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1)
        user = api.user(username=username)

        async for video in user.videos(count=1000):
            ts = int(video.as_dict.get("createTime", 0))
            views = int(video.as_dict.get("stats", {}).get("playCount", 0))
            if ts >= cutoff_ts:
                total_views += views
                video_count += 1

    return {
        "username": username,
        "total_views": total_views,
        "video_count": video_count
    }