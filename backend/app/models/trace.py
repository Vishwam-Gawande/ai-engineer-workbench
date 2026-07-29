from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Trace(Base):
    __tablename__ = "traces"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    trace_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    model: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    latency: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    tokens: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    cost: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )