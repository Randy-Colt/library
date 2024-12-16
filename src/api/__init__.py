from fastapi import APIRouter

from .authors.views import router as author_router
from .books.views import router as book_router
from .borrows.views import router as borrow_router

api_router = APIRouter(prefix='/api')

api_router.include_router(author_router)
api_router.include_router(book_router)
api_router.include_router(borrow_router)
