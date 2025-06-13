import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api

# Create the Inngest client
inngest_client = inngest.Inngest(
    app_id="fast_api_example",
    logger=logging.getLogger("uvicorn"),
)

# Create an Inngest function
@inngest_client.create_function(
    fn_id="my_function",
    trigger=inngest.TriggerEvent(event="app/my_function"),
)
async def my_function(ctx: inngest.Context, step: inngest.Step) -> str:
    ctx.logger.info(ctx.event)
    return "done"

# Create the FastAPI app that Vercel will call
app = FastAPI()

# Hook Inngest into the FastAPI app
inngest.fast_api.serve(app, inngest_client, [my_function])