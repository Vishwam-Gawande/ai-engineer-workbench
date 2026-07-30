from sqlalchemy import (
    ForeignKey,
    String,
    Integer,
    Float,
    Text,
    JSON,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.db.base import Base


# -----------------------
# User
# -----------------------

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    traces = relationship("Trace", back_populates="user")
    prompts = relationship("Prompt", back_populates="user")
    experiments = relationship("Experiment", back_populates="user")


# -----------------------
# Trace
# -----------------------

class Trace(Base):
    __tablename__ = "traces"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    trace_name: Mapped[str] = mapped_column(String(255))

    status: Mapped[str] = mapped_column(String(50))

    model_name: Mapped[str] = mapped_column(String(100))

    latency_ms: Mapped[int] = mapped_column(Integer)

    total_tokens: Mapped[int] = mapped_column(Integer)

    total_cost: Mapped[float] = mapped_column(Float)

    user = relationship("User", back_populates="traces")

    spans = relationship("Span", back_populates="trace")


# -----------------------
# Span
# -----------------------

class Span(Base):
    __tablename__ = "spans"

    id: Mapped[int] = mapped_column(primary_key=True)

    trace_id: Mapped[int] = mapped_column(
        ForeignKey("traces.id")
    )

    parent_span_id: Mapped[int | None] = mapped_column(
        ForeignKey("spans.id"),
        nullable=True,
    )

    span_type: Mapped[str] = mapped_column(String(100))

    input: Mapped[dict] = mapped_column(JSON)

    output: Mapped[dict] = mapped_column(JSON)

    metadata_json: Mapped[dict] = mapped_column(
    "metadata",
    JSON,
    )

    latency_ms: Mapped[int] = mapped_column(Integer)

    tokens: Mapped[int] = mapped_column(Integer)

    trace = relationship("Trace", back_populates="spans")

    parent = relationship(
        "Span",
        remote_side=[id],
    )


# -----------------------
# Prompt
# -----------------------

class Prompt(Base):
    __tablename__ = "prompts"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    name: Mapped[str] = mapped_column(String(255))

    version: Mapped[int] = mapped_column(Integer)

    template: Mapped[str] = mapped_column(Text)

    user = relationship("User", back_populates="prompts")

    experiments = relationship(
        "Experiment",
        back_populates="prompt",
    )


# -----------------------
# Experiment
# -----------------------

class Experiment(Base):
    __tablename__ = "experiments"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    prompt_id: Mapped[int] = mapped_column(
        ForeignKey("prompts.id")
    )

    model_name: Mapped[str] = mapped_column(String(100))

    score: Mapped[float] = mapped_column(Float)

    notes: Mapped[str] = mapped_column(Text)

    user = relationship("User", back_populates="experiments")

    prompt = relationship(
        "Prompt",
        back_populates="experiments",
    )