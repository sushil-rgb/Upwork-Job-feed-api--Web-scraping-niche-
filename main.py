from scraper import job_alerts
from fastapi import FastAPI


app = FastAPI()


@app.get("/jobs")
async def job_feed():
    return {
        "jobs": await job_alerts()
    }

