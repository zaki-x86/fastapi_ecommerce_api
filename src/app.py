import sentry_sdk
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator

from src.addresses.router import router as router_addresses
from src.auth.router import router as router_auth
from src.config import settings
from src.countries.router import router as router_countries
from src.images.router import router as router_images
from src.orders.router import router as router_orders
from src.payments.router import router as router_payments
from src.products.router import router as router_products
from src.shipping_methods.router import router as router_shipping_methods
from src.shopping_carts.router import router as router_shopping_carts
from src.users.router import router as router_users
from src.variations.router import router as router_variations


app = FastAPI(title="Ecommerce API")

if settings.SENTRY_URL_NUMBER != "" and settings.SENTRY_PROJECT_NUMBER != "":
    sentry_sdk.init(
        dsn=f"https://{settings.SENTRY_URL_NUMBER}.ingest.us.sentry.io/{settings.SENTRY_PROJECT_NUMBER}",
        enable_tracing=True,
    )

router = APIRouter(prefix="/api")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://localhost:3000",
    "https://127.0.0.1:3000",
    "http://test",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="src/static"), "static")

router.include_router(router_auth)
router.include_router(router_users)
router.include_router(router_countries)
router.include_router(router_addresses)
router.include_router(router_payments)
router.include_router(router_variations)
router.include_router(router_products)
router.include_router(router_images)
router.include_router(router_shopping_carts)
router.include_router(router_shipping_methods)
router.include_router(router_orders)

app.include_router(router)

instrumentator = (
    Instrumentator(
        should_group_status_codes=False, excluded_handlers=["/metrics"]
    )
    .instrument(app)
    .expose(app)
)
