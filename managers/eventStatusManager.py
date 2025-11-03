class EventStatusManager:
    """Handles event status transitions like publishing and canceling."""

    def publish_event(self, event):
        event.status = "Published"

    def cancel_event(self, event):
        event.status = "Cancelled"
