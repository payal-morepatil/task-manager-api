from pydantic import BaseModel, Field

class Task(BaseModel):
    title: str = Field(..., pattern='^[a-zA-Z0-9 ]+$', description='Title must be alphanumeric and can'
                                                                   'include spaces')
    description: str = Field(..., pattern='^[a-zA-Z0-9 ]+$', description='Description must be'
                                                        ' alphanumeric and can include spaces')
    status: str = Field(..., pattern='^[a-zA-Z0-9 ]+$', description='Title must be alphanumeric and '
                                                                    'can include spaces')