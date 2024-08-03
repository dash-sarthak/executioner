from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Union

from sqlalchemy import DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.operators import op

from database import Base


class Environment(Base):
    __tablename__ = "environments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    environment: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(ZoneInfo("Asia/Kolkata")),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(ZoneInfo("Asia/Kolkata")),
    )

    applications: Mapped[list["Application"]] = relationship(
        back_populates="environment"
    )

    def __repr__(self) -> str:
        return f"if: {self.id}, environment: {self.environment}"


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    application: Mapped[str] = mapped_column(String(50), nullable=False)
    module: Mapped[str] = mapped_column(String(50), nullable=False)
    environment_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("environments.id", ondelete="CASCADE")
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(ZoneInfo("Asia/Kolkata")),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now(ZoneInfo("Asia/Kolkata")),
    )

    environment: Mapped["Environment"] = relationship(back_populates="applications")

    __table_args__ = (
        UniqueConstraint("application", "module", name="uix_application_module"),
    )

    def __repr__(self) -> str:
        return f"if: {self.id}, environment: {self.environment}"
