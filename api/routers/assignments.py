from typing import List, Dict

from fastapi import APIRouter, Depends

from api.schemas import students, users, assignments
from api.utils import assignments as assignments_utils
from api.utils.dependencies import get_current_user

from app import settings

router = APIRouter(prefix="/assignments",)


@router.get("/", response_model=List[assignments.AssignmentBase])
async def get_assignments(user: users.User = Depends(get_current_user)):
    return await assignments_utils.get_assignments_by_user(user=user)


@router.get("/{assignment_id}", response_model=assignments.AssignmentBase)
async def assignments_details(assignment_id: int, user: users.User = Depends(get_current_user)):
    return await assignments_utils.get_assignments_details(assignment_id=assignment_id)


@router.get("/{assignment_id}/questions")
async def assignments_questions(assignment_id: int, skip: int = 0, limit: int = settings.QUESTION_PAGINATION_SIZE,
                                user: users.User = Depends(get_current_user)):
    records = await assignments_utils.get_assignments_questions(assignment_id=assignment_id)
    return {"total": len(records), "questions": records[skip:limit]}


@router.get("/quizzes", response_model=List[assignments.QuizzesBase])
async def get_assignments(user: users.User = Depends(get_current_user)):
    return await assignments_utils.get_assignments_by_user(user=user)


@router.get("/quizzes/{assignment_id}", response_model=assignments.QuizzesBase)
async def assignments_details(assignment_id: int, user: users.User = Depends(get_current_user)):
    return await assignments_utils.get_assignments_details(assignment_id=assignment_id)


@router.get("/quizzes/{assignment_id}/questions")
async def assignments_questions(assignment_id: int, skip: int = 0, limit: int = settings.QUESTION_PAGINATION_SIZE,
                                user: users.User = Depends(get_current_user)):
    records = await assignments_utils.get_assignments_questions(assignment_id=assignment_id)
    return {"total": len(records), "questions": records[skip:limit]}
