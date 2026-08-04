from fastapi import HTTPException


class CompanyNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Company not found"
        )

class CompanyAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Company already exists"
        )        


class UserNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="User not found"
        )


class ExpenseNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Expense not found"
        )