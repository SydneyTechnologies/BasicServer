from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

DESCRIPTION = "This is a basic example of how a server works and the type of files in which can be served as webcontent"
app = FastAPI(title="Basic Server", description=DESCRIPTION)



app.mount("/static", StaticFiles(directory="./static/"), name="static")
@app.get('/html', response_class=HTMLResponse, summary="Serve Html page")
def getHtml():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
@app.get("/study", summary="Nice looking html page about the backend study group")
def getStudyHtml():
    return FileResponse(path="./static/index.html", media_type="text/html")

@app.get("/video", summary="Serve a video file")
def serveVideo():
    return FileResponse(path="./greed.mp4", media_type="video/mp4")

@app.get("/json", summary="Serve Json")
def serveJson():
    return {"study group":"Backend developer study group"}


@app.get("/download")
def download():
    filePath = "./greed.mp4"
    return FileResponse(filename="g.mp4", path=filePath, media_type="video/mp4")

@app.get("/echo/{string}", summary="Echo what the person is saying")
def echoPlainText(string: str):
    return PlainTextResponse(content=string)

@app.get("/osi", summary="Take me to youtube video about OSI")
def redirectToYoutube():
    return RedirectResponse(url="https://www.youtube.com/watch?v=KHMwhjQrCmo")