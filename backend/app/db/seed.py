from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.models.models import (
    User,
    Prompt,
    Trace,
    Experiment,
)


def seed_database():
    db: Session = SessionLocal()

    try:
        # -----------------------------
        # Prevent duplicate seeding
        # -----------------------------
        if db.query(User).first():
            print("Database already seeded.")
            return

        # -----------------------------
        # User
        # -----------------------------
        user = User(
            email="demo@workbench.ai",
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        # -----------------------------
        # Prompts
        # -----------------------------
        prompts = [
            Prompt(
                user_id=user.id,
                name="Customer Support",
                version=1,
                template="You are a helpful support assistant.",
            ),
            Prompt(
                user_id=user.id,
                name="RAG QA",
                version=2,
                template="Answer only using retrieved documents.",
            ),
            Prompt(
                user_id=user.id,
                name="Summarizer",
                version=1,
                template="Summarize the following text.",
            ),
        ]

        db.add_all(prompts)
        db.commit()

        # -----------------------------
        # Traces
        # -----------------------------
        traces = [
            Trace(
                user_id=user.id,
                trace_name="Customer Chat",
                status="success",
                model_name="gpt-4.1-mini",
                latency_ms=210,
                total_tokens=980,
                total_cost=0.021,
            ),
            Trace(
                user_id=user.id,
                trace_name="Document QA",
                status="success",
                model_name="gpt-4.1-mini",
                latency_ms=320,
                total_tokens=1400,
                total_cost=0.034,
            ),
            Trace(
                user_id=user.id,
                trace_name="Agent Workflow",
                status="failed",
                model_name="gpt-4.1-mini",
                latency_ms=410,
                total_tokens=1800,
                total_cost=0.048,
            ),
            Trace(
                user_id=user.id,
                trace_name="Evaluation Run",
                status="success",
                model_name="gpt-4.1-mini",
                latency_ms=180,
                total_tokens=760,
                total_cost=0.018,
            ),
            Trace(
                user_id=user.id,
                trace_name="Prompt Replay",
                status="success",
                model_name="gpt-4.1-mini",
                latency_ms=250,
                total_tokens=1100,
                total_cost=0.026,
            ),
        ]

        db.add_all(traces)
        db.commit()

        # -----------------------------
        # Experiments
        # -----------------------------
        experiments = [
            Experiment(
                user_id=user.id,
                prompt_id=1,
                model_name="gpt-4.1-mini",
                score=0.92,
                notes="Baseline prompt.",
            ),
            Experiment(
                user_id=user.id,
                prompt_id=2,
                model_name="gpt-4.1-mini",
                score=0.95,
                notes="Improved retrieval prompt.",
            ),
            Experiment(
                user_id=user.id,
                prompt_id=3,
                model_name="gpt-4.1-mini",
                score=0.89,
                notes="Summarization experiment.",
            ),
        ]

        db.add_all(experiments)
        db.commit()

        print("Database seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()