from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary

async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummay summary",
    )
    await summary.save()
    return summary.id