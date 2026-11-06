# from app.core.config import get_settings
# settings = get_settings()
# print(f"App name{settings.app_name}")

# ------------------------------------------------------------------

# from app.services.ingestion import load_file,chunk_documents
# from pathlib import Path
# docs = load_file(Path("data/sample_kb/company_it_handbook.md"))
# chunks = chunk_documents(docs)
# print(len(chunks))

# ---------------------------------------------------------------------

# from app.rag.vectorstore import add_documents
# add_documents(chunks)
# print("Documents added to vectorstore")

import uvicorn

if __name__ =="__main__":
    uvicorn.run("app.main:app",host="127.0.0.1",port=8000,reload=True)