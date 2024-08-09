from fastapi import FastAPI, File, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from google.cloud import storage
from datetime import datetime
import time

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
# def upload_blob(bucket_name, source_file_name, destination_blob_name,folder):
#     """Uploads a file to the bucket.

#     Args:
#         bucket_name (str): The name of the bucket to upload to.
#         source_file_name (str): The path to the file to upload.
#         destination_blob_name (str): The name of the blob to create.
#     """

#     storage_client = storage.Client(project="cosmic-carving-431013-c0")
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(destination_blob_name)

#     blob.upload_from_filename(source_file_name)

#     print(f"File {source_file_name} uploaded to {destination_blob_name}.")


# upload_blob("demo-test-data-forge","../demo.csv","demo.csv")

def upload_file(folder, file: UploadFile = File(...)):
    if(file.size<5000):
        raise HTTPException(status_code=500)
    month = datetime.now().strftime("%B").lower()
    print(file.filename)
    bucket_name = "southamerica-west1-data-aut-4fcbc258-bucket"  
    destination_blob_name = f"dags/{folder}/{month}.json"

    storage_client = storage.Client(project="cosmic-carving-431013-c0")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(file.file) 

    


def upload_file_platform(folder,ext ,file: UploadFile = File(...)):
    if(file.size<5000):
        raise HTTPException(status_code=500)
    month = datetime.now().strftime("%B").lower()
    bucket_name = "southamerica-west1-data-aut-4fcbc258-bucket"  
    destination_blob_name = f"dags/{folder}/business_{month}.{ext}"

    storage_client = storage.Client(project="cosmic-carving-431013-c0")
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(file.file) 




@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/error")
async def read_root(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})


@app.post("/louisiana")
async def create_upload_file( request: Request, file: UploadFile = File(...)):
    try:
        upload_file("louisiana",file=file)
        return templates.TemplateResponse("success.html", {"request": request})
    except:
        return templates.TemplateResponse("error.html", {"request": request})



@app.post("/indiana")
async def res(request: Request,file: UploadFile = File(...)):
    try:
        upload_file("indiana",file=file)
        return templates.TemplateResponse("success.html", {"request": request})
    except:
        return templates.TemplateResponse("error.html", {"request": request})

@app.post("/google")
async def google(request: Request,file: UploadFile = File(...)):
    try:
        upload_file_platform("google","json",file=file)
        return templates.TemplateResponse("success.html", {"request": request})
    except:
        return templates.TemplateResponse("error.html", {"request": request})

@app.post("/yelpbusiness")
async def yelpbusiness(request: Request,file: UploadFile = File(...)):
    try:
        upload_file_platform("yelp","pkl",file=file)
        return templates.TemplateResponse("success.html", {"request": request})
    except:
        return templates.TemplateResponse("error.html", {"request": request})
@app.get("/success")
async def s(request:Request):
    return templates.TemplateResponse("success.html", {"request": request})

@app.post("/yelpreviews")
async def yelpreviews(request: Request,file: UploadFile = File(...)):
    try:
        upload_file("yelp",file=file)
        return templates.TemplateResponse("success.html", {"request": request})
    except:
        return templates.TemplateResponse("error.html", {"request": request})


async def redirect_after(response=None):
    time.sleep(2)
    return RedirectResponse("/")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

