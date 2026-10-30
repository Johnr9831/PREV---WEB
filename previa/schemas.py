from pydantic import BaseModel, Field


class Course(BaseModel):
    code: str
    name: str
    semester: int = Field(ge=1)
    credits: int = Field(gt=0)
