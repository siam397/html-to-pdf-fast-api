import io

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from weasyprint import HTML

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/html")
async def convert_html_to_pdf(q: str):
    try:
        html = HTML(string=q)
        pdf_bytes = html.write_pdf()
        return StreamingResponse(io.BytesIO(pdf_bytes), media_type="application/pdf",
                                 headers={"Content-Disposition": "inline; filename=output.pdf"})

    except Exception as e:
        # Handle any errors that might occur during the PDF generation
        raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")