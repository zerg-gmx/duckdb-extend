from fastapi import  UploadFile, File, Form, APIRouter
from starlette.responses import JSONResponse

from main import app
from service.duckdb_support import DuckDBSupport

router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)

app.include_router(router)

duckdb_support = DuckDBSupport()


@router.post("/upload_csv")
async def upload_csv(db_name: str = Form(...),
                     table_name: str = Form(...),
                     file: UploadFile = File(...)):
    duckdb_support.upload_csv(db_name, table_name, file.file)
    return JSONResponse(content={"message": "CSV uploaded and table created successfully"})
