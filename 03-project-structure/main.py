if __name__ == "__main__":
    import uvicorn
    from app import app

    uvicorn.run(app, host="localhost", port=8000)
