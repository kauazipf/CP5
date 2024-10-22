from fastapi import FastAPI
from produtos import router as produtos_router
from fornecedores import router as fornecedores_router
from pedidos import router as pedidos_router

app = FastAPI()

# Incluindo os endpoints de cada módulo
app.include_router(produtos_router, prefix="/produtos", tags=["Produtos"])
app.include_router(fornecedores_router, prefix="/fornecedores", tags=["Fornecedores"])
app.include_router(pedidos_router, prefix="/pedidos", tags=["Pedidos"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


