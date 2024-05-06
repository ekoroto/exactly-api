import asyncio


def run_coroutine(coroutine):
    """Run the given coroutine in the existing event loop or a new one if no loop exists."""
    loop = asyncio.get_event_loop()

    try:
        if loop.is_closed():
            raise RuntimeError('Loop is closed')

        loop_already_running = loop.is_running()
    except RuntimeError:
        loop_already_running = False

    if loop_already_running:
        # If the loop is running, use ensure_future to schedule the coroutine to run.
        # This won't run the coroutine immediately but will schedule it to run soon.
        # Ensure that something is running the event loop for this to take effect.
        asyncio.ensure_future(coroutine)
        return None  # No immediate result can be obtained in this context.
    else:
        # If there's no running loop, create a new one and run the coroutine.
        return loop.run_until_complete(coroutine)
