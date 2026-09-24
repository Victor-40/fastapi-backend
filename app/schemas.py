from typing import Literal

from pydantic import BaseModel, Field

CourseLevel = Literal["beginner", "intermediate", "advanced"]

class CourseRead(BaseModel):
    id: int
    title: str
    slug: str
    level: CourseLevel
    price: float

class LessonRead(BaseModel):
    id: int
    course_id: int
    title: str
    order: int

class CourseCreate(BaseModel):
    title: str = Field(min_length=3, max_length=80)
    slug: str = Field(min_length=3, max_length=60, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    level: CourseLevel
    price: float = Field(default=0, ge=0)

class CourseUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=80)
    slug: str | None = Field(default=None, min_length=3, max_length=60, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    level: CourseLevel | None = None
    price: float | None = Field(default=None, ge=0)